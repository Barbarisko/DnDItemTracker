#!/bin/bash

# Get the value of the ENV_VAR environment variable
ENV_VAR_VALUE=${ENV_VAR:-default_value}

# Create or overwrite the file with the text containing the environment variable value
cat > /etc/nginx/test_nginx.conf << EOF

user  nginx;
worker_processes  auto;


events {
    worker_connections  1024;
}


http {
  server {
    listen 80;

    location /api/ {
      proxy_pass http://$BACKEND_ADRESS/;
      proxy_set_header Host \$host;
      proxy_set_header X-Real-IP \$remote_addr;
    }

    location / {
      root /var/www/html/;
      include /etc/nginx/mime.types;
      index index.html;
    }
  }
}
EOF


