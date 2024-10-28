from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework import status
from .models import UserToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        # Вызываем метод родительского класса для получения токенов
        response = super().post(request, *args, **kwargs)

        # Получаем пользователя по его имени или почте из запроса
        username = request.data.get('username')  # Или используйте 'email', если вы регистрируете по email
        user = CustomUser.objects.filter(username=username).first()

        # Проверяем, что пользователь аутентифицирован
        if user is None:
            raise IsAuthenticated("Пользователь не найден.")

        # Сохраняем токены в базе данных
        tokens, _ = UserToken.objects.get_or_create(user=user)
        tokens.access_token = response.data['access']
        tokens.refresh_token = response.data['refresh']
        tokens.save()

        return Response({
            'access': tokens.access_token,
            'refresh': tokens.refresh_token
        })


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Проверяем, аутентифицирован ли пользователь
        if request.user.is_anonymous:
            return Response(
                {'detail': 'Authentication credentials were not provided.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        response = super().post(request, *args, **kwargs)

        # Обновляем токены в базе данных
        try:
            user_token = UserToken.objects.get(user=request.user)
            user_token.access_token = response.data['access']
            user_token.save()
        except UserToken.DoesNotExist:
            pass  # Обработка случая, если токен не найден

        return response




class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_token = UserToken.objects.get(user=request.user)
            user_token.delete()  # Удаляем токены
            return Response(
                {'message': 'Logout successful.'},
                status=200
            )
        except UserToken.DoesNotExist:
            return Response(
                {'message': 'User not logged in.'},
                status=401  # Используем 401 вместо 400
            )

        