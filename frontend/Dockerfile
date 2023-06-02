FROM node:lts-alpine3.12 as build

WORKDIR /app/frontend/

COPY package.json .
COPY yarn.lock .

RUN yarn install

COPY . .

RUN yarn build

# The second stage
# Copy React static files and start nginx
FROM nginx:stable-alpine
COPY --from=build /app/frontend/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]