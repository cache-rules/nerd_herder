ARG FRONTEND_IMAGE=registry.gitlab.com/cache-rules/nerd_herder_ops/frontend:latest
ARG BACKEND_IMAGE=registry.gitlab.com/cache-rules/nerd_herder_ops/nerd_herder:latest

FROM ${FRONTEND_IMAGE} as frontend
RUN yarn build

FROM ${BACKEND_IMAGE} as backend
RUN SECRET_KEY=WORKAROUND_FOR_COLLECTSTATIC python manage.py collectstatic --no-input

FROM abiosoft/caddy:1.0.0-no-stats

COPY --from=frontend /usr/src/nerd_herder/frontend/build /var/www/nerd_herder/
COPY --from=backend /usr/src/nerd_herder/static /var/www/nerd_herder/static
COPY ./Caddyfile /etc/Caddyfile
