SUDO ?= sudo
SPARK_VERSION ?= 2.4.5
HADOOP_VERSION ?= 2.7

include .environment

build:
	${SUDO} docker build -t spark-base:latest -f spark-base/Dockerfile \
		--build-arg SPARK_VERSION=${SPARK_VERSION} \
		--build-arg HADOOP_VERSION=${HADOOP_VERSION} .
	${SUDO} docker build -t spark-master:latest -f spark-master/Dockerfile .
	${SUDO} docker build -t spark-worker:latest -f spark-worker/Dockerfile .

start:
	${SUDO} docker-compose up -d

stop:
	${SUDO} docker-compose stop

ssh:
	${SUDO} docker exec -it spark_master_1 /bin/bash
