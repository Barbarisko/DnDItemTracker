FROM node:18-alpine3.17 as build
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build

FROM nginx
COPY --from=build /app/dist /var/www/html/

EXPOSE 80
EXPOSE 443
CMD ["nginx","-g","daemon off;"]