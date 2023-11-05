#!/bin/bash
IMAGE=proyectofinal_cc
TAG=v0.1
CONTAINER_NAME=proyectofinal_cc_

SOURCE=$(PWD)
TARGET=/home/app/
WORK_DIR=$(TARGET)

ARGS=-it --rm -v $(SOURCE):$(TARGET) -w $(WORK_DIR) -p 8888:8888 $(IMAGE):$(TAG)

run:
	docker run $(ARGS) bash

build_image:
	docker build -t $(IMAGE):$(TAG) .

run_script:
	docker run $(ARGS) python3 check_faces.py