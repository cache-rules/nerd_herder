env :=dev

ifeq ($(env), staging)
  compose_file=docker-compose.stg.yml
else ifeq ($(env), prod)
  compose_file=docker-compose.prod.yml
else
  compose_file=docker-compose.dev.yml
endif

login:
	docker login registry.gitlab.com

stack:
	docker stack $(cmd) $(options)

ls: cmd := ls
rm: cmd := rm
ps: cmd := ps
rm ps: options := nerd_herder_$(env)
deploy: cmd := deploy
deploy: options := -c $(compose_file) nerd_herder_$(env)
ls rm ps deploy: stack

docker_compose:
	docker-compose -f $(compose_file) $(cmd)

build: cmd := build
push: cmd := push
up: cmd:= up -d
down: cmd:= down
restart: cmd:= restart $(name)
logs: cmd:= logs -f
build push up down restart logs: docker_compose

slogs:
	docker service logs -f nerd_herder_$(name)
