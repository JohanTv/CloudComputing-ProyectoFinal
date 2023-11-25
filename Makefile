IMAGE_NAME=spoofing
TAG=v1.0
IMAGE=$(IMAGE_NAME):$(TAG)
IMAGE_LAMBDA=$(IMAGE_NAME)_lambda:$(TAG)

SOURCE="$(PWD)"
TARGET=/home/app/
WORK_DIR=$(TARGET)

PORT=8888
OPTIONS=-it --rm -v $(SOURCE):$(TARGET) -w $(WORK_DIR)

run:
	docker run $(OPTIONS) -p $(PORT):$(PORT) $(IMAGE) bash

build_image:
	docker build -t $(IMAGE) .

remove_image:
	docker rmi $(IMAGE)

run_script:
	docker run $(OPTIONS) $(IMAGE) python3 check_faces.py

run_jupyter:
	docker run $(OPTIONS) -p $(PORT):$(PORT) $(IMAGE) jupyter notebook --notebook-dir=notebooks/ --ip 0.0.0.0 --port $(PORT) --no-browser --allow-root
	
run_cadvisor:
	docker run -d --rm --volume=/:/roots:ro --volume=/var/run:/var/run:rw --volume=/sys:/sys:ro --volume=/var/lib/docker:/var/lib/docker:ro -p 8080:8080 --privileged=true --name cadvisor gcr.io/cadvisor/cadvisor

build_lambda_image:
	docker build -t $(IMAGE_LAMBDA) -f lambda/Dockerfile .

remove_lambda_image:
	docker rmi $(IMAGE_LAMBDA)