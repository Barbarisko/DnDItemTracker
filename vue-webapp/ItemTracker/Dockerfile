FROM node:18-alpine3.17 as build
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build

FROM nginx
COPY --from=build /app/dist /var/www/html/
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx","-g","daemon off;"]