FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html book-cover.jpg share.jpg robots.txt /usr/share/nginx/html/
EXPOSE 80
