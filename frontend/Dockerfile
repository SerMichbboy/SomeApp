FROM node:18

WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все файлы в контейнер
COPY . /app/

# Логируем содержимое папки /app/src для проверки
RUN ls -la /app/src

# Строим приложение
RUN npm run build

# Открываем порт для фронтенда
EXPOSE 3000

# Запускаем приложение
CMD ["npm", "start", "--", "--port", "80"]
