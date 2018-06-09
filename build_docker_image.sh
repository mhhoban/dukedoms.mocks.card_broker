#!/bin/bash
SERVICE=mock_card_broker
docker build --build-arg service=$SERVICE \
--tag "mhhoban/dukedoms-mock-card-broker:latest" .
