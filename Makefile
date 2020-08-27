PKG_NAME     := $(shell python setup.py --name)
PKG_VERSION  := $(shell python setup.py --version)
PKG_ORG      := vapor-ware
IMAGE_NAME   := netbox_virtual_circuit_plugin
COMPOSE_FILE := dev/docker-compose.yml

.PHONY: clean deploy docker github-tag migrate release test version help
.DEFAULT_GOAL := help

changelog:  ## Generate a changelog file from GitHub Issue Tracker
	github_changelog_generator -u ${PKG_ORG} -p ${PKG_NAME}

clean:  ## Clean up build artifacts
	rm -rf build/ dist/ *.egg-info

deploy: docker  ## Run a local development deployment of the plugin with NetBox
	docker-compose -f ${COMPOSE_FILE} -p ${IMAGE_NAME} up

docker:  ## Build a local docker image
	docker-compose -f ${COMPOSE_FILE} -p ${IMAGE_NAME} build

github-tag:  ## Create and push a tag with the current version
	git tag -a v${PKG_VERSION} -m "${PKG_NAME} version v${PKG_VERSION}"
	git push -u origin v${PKG_VERSION}

migrate: docker  ## Run makemigrations in Django and produce a migration file locally
	docker-compose -f ${COMPOSE_FILE} -p ${IMAGE_NAME} run -u root netbox sh -c "python manage.py makemigrations ${IMAGE_NAME}"

release: clean  ## Package and distribute the current release to PyPI
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

test: ## Run unit tests
	docker-compose -f ${COMPOSE_FILE} -p ${IMAGE_NAME} run netbox sh -c "python manage.py test ${IMAGE_NAME}"

version:  ## Print the version
	@echo "${PKG_VERSION}"

help:  ## Print usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
