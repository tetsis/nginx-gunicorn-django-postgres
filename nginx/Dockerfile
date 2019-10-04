FROM nginx:1.12.2-alpine
ADD nginx/nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /var/www/static
ADD src/static /var/www/static/