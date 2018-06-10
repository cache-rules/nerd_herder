FROM node:9.11-alpine

WORKDIR /usr/src/nerd_herder/frontend


COPY frontend/package.json .
COPY frontend/yarn.lock .

RUN yarn install

COPY frontend/src/ ./src/
COPY frontend/public/ ./public/

EXPOSE 3000
