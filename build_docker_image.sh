#!/bin/bash
./oas_setup.sh
SERVICE=card_broker
docker build --build-arg service=$SERVICE \
--tag "mhhoban/dukedoms-card-broker:candidate" .
