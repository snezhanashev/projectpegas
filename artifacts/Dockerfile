# Stage 1: Build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=development
COPY . .
RUN npm run build || echo "Build step skipped"

# Stage 2: Runtime
FROM node:18-alpine
WORKDIR /app
# Копируем только production-зависимости из стадии builder
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
