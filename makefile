DOCKER_COMPOSE_FILE := ./deployment/docker-compose.yml
DOCKER_SERVICE_NAME := app

.DEFAULT_GOAL := help


.PHONY: run-docker
run-docker:
	@echo "========== Starting Docker Compose Process =========="
	@echo "========== 1. Stopping and removing containers, and cleaning up unused images =========="
	docker-compose -f $(DOCKER_COMPOSE_FILE) down
	docker image prune -f
	@echo "========== 2. Building and starting the Docker service ($(DOCKER_SERVICE_NAME)) =========="
	docker-compose -f $(DOCKER_COMPOSE_FILE) up --build -d $(DOCKER_SERVICE_NAME)
	@echo "========== 3. Checking the status of the Docker service ($(DOCKER_SERVICE_NAME)) =========="
	docker-compose -f $(DOCKER_COMPOSE_FILE) ps
	@echo "========== Docker Compose Process Complete =========="