#!/bin/bash

source config.sh

docker run \
    --name=nichtparajitsi \
    --rm=true \
    -p 127.0.0.1:5901:5901 \
    -v $PWD/nichtparajitsi.py:/home/nichtparajitsi.py \
    -e NICHTPARA_INSTANCE=$NICHTPARA_INSTANCE \
    -e NICHTPARA_USR=$NICHTPARA_USR \
    -e NICHTPARA_PWD=$NICHTPARA_PWD \
    -e JITSI_INSTANCE=$JITSI_INSTANCE \
    -d \
    nichtparajitsi
