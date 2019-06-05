FROM registry.gitlab.com/cache-rules/nerd_herder_ops/frontend:0.6-beta as frontend
RUN yarn build
FROM registry.gitlab.com/cache-rules/nerd_herder_ops/nerd_herder:0.8-beta as backend
RUN SECRET_KEY=WORKAROUND_FOR_COLLECTSTATIC python manage.py collectstatic --no-input
FROM abiosoft/caddy:1.0.0-no-stats

COPY --from=frontend /usr/src/nerd_herder/frontend/build /var/www/nerd_herder/
COPY --from=backend /usr/src/nerd_herder/static /var/www/nerd_herder/static
COPY ./Caddyfile /etc/Caddyfile
