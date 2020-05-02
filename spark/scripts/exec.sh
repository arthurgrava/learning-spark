#!/bin/bash

SCRIPT=$1
if [ -z "${SCRIPT}" ]; then
    echo "Provide a script to run"
    exit 1
fi

MASTER=$2
if [ -z "${MASTER}" ]; then
    echo "Master not provided, using local. (Try spark://10.5.0.2:7077)"
    MASTER='local[*]'
fi

APP_NAME=$(basename ${SCRIPT})

echo "Executing ${SCRIPT} on ${MASTER}"

MASTER=${MASTER} APP_NAME=${APP_NAME} spark-submit ${SCRIPT}
