FROM node:18-alpine3.17 as build
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build

FROM nginx
COPY --from=build /app/dist /var/www/html/
COPY --from=build /app/site.conf /etc/nginx/sites-enabled/

EXPOSE 80
CMD ["nginx","-g","daemon off;"]