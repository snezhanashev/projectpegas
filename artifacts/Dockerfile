# Stage 1: Build (установка dev-зависимостей для линтера)
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=development

# Stage 2: Runtime (только production-зависимости и код)
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
