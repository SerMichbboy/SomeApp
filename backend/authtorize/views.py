from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from .models import UserToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class CustomTokenObtainPairView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = CustomUser.objects.filter(username=username,).first()
        if user is None:
            return Response(
                {'detail': 'Invalid username or email.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Нужно реализовать хранение пароля
        if not user.check_password(password):
            return Response(
                {'detail': 'Invalid credentials.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        tokens, created = UserToken.objects.get_or_create(user=user)
        tokens.access_token = access_token
        tokens.refresh_token = str(refresh)
        tokens.save()

        return Response({
            'access': access_token,
            'refresh': str(refresh)
        })


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Проверяем, аутентифицирован ли пользователь
        if request.user.is_anonymous:
            return Response(
                {
                    'detail': 'Authentication credentials were not provided.'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        response = super().post(request, *args, **kwargs)

        try:
            user_token = UserToken.objects.get(user=request.user)
            user_token.access_token = response.data['access']
            user_token.save()
        except UserToken.DoesNotExist:
            pass

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
                status=401
            )
        