PKG_NAME     := $(shell python setup.py --name)
PKG_VERSION  :=  $(shell python setup.py --version)
IMAGE_NAME   := netbox_virtual_circuit_plugin
COMPOSE_FILE := dev/docker-compose.yml

.PHONY: clean deploy docker release version help
.DEFAULT_GOAL := help

clean:  ## Clean up build artifacts
	rm -rf build/ dist/ *.egg-info

deploy:  ## Run a local development deployment of the plugin with NetBox
	docker-compose -f ${COMPOSE_FILE} -p ${IMAGE_NAME} up

docker:  ## Build a local docker image
	docker-compose -f ${COMPOSE_FILE} -p ${IMAGE_NAME} build

release: clean  ## Package and distribute the current release to PyPI
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

version:  ## Print the version
	@echo "${PKG_VERSION}"

help:  ## Print usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
