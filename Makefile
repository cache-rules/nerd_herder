env :=dev

docker_compose:
	docker-compose $(options) $(cmd)

up: cmd := up -d
down: cmd := down
build: cmd := build
start: cmd := start $(name)
restart: cmd := restart $(name)
stop: cmd := stop $(name)
logs: cmd := logs -f
bash: cmd := exec $(name) ls -l /var/www/nerd_herder/

ifeq ($(env), staging)
	options := -f docker-compose.yml -f docker-compose.stg.yml
else ifeq ($(env), prod)
	options := -f docker-compose.yml -f docker-compose.prod.yml
else
	options :=
endif

up down build start restart stop logs bash: docker_compose
