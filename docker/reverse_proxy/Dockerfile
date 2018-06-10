FROM nerd_herder_frontend:latest as frontend
RUN yarn build
FROM nerd_herder_nerd_herder:latest as backend
RUN python manage.py collectstatic --no-input
FROM abiosoft/caddy:0.11.0-no-stats

COPY --from=frontend /usr/src/nerd_herder/frontend/build /var/www/nerd_herder/
COPY --from=backend /usr/src/nerd_herder/static /var/www/nerd_herder/static
COPY ./Caddyfile.prod /etc/Caddyfile
