env :=dev
compose_file := docker-compose.$(env).yml

login:
	docker login registry.gitlab.com

stack:
	docker stack $(cmd) $(options)

ls: cmd := ls
rm: cmd := rm
ps: cmd := ps
rm ps: options := nerd_herder_$(env)
deploy: cmd := deploy
deploy: options := --with-registry-auth -c $(compose_file) nerd_herder_$(env)
ls rm ps deploy: stack

service:
	docker service $(cmd) $(options)

sls: cmd := ls
sps: cmd := ps
sps: options := nerd_herder_$(env)_$(name)
slogs: cmd:= logs
slogs: options := -f nerd_herder_$(env)_$(name)
sls sps slogs: service

docker_compose:
	docker-compose -f $(compose_file) $(cmd)

build: cmd := build
push: cmd := push
up: cmd:= up -d
down: cmd:= down
restart: cmd:= restart $(name)
logs: cmd:= logs -f
exec: cmd:= exec $(name) $(c)
build push up down restart logs exec: docker_compose
