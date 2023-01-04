IMAGE_NAME ?= sapphire
export IMAGE_NAME

vars:
	@echo IMAGE_NAME=${IMAGE_NAME}

image:
	docker build -f build/Dockerfile -t ${IMAGE_NAME} . --force-rm=True

run:
	docker-compose -f ./build/docker-compose.yml up web

clean:
	docker-compose -f ./build/docker-compose.yml down -v
	docker-compose -f ./build/docker-compose.yml rm -s -v -f
