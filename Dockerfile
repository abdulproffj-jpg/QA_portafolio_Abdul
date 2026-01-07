# Use a lightweight Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json if exists
COPY package*.json ./

# Install dependencies (skip if no package.json)
RUN if [ -f package.json ]; then npm install; fi

# Copy all files
COPY . .

# Expose port
EXPOSE 3000

# Start app (adjust if your site uses another command)
CMD ["npx", "http-server", ".", "-p", "3000"]
