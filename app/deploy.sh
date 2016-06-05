#!/usr/bin/env bash

echo "pulling new changes from GH"
ssh $DEPLOY_USER@$DEPLOY_HOST 'cd badger-app && git pull'

echo "rebuilding web container"
ssh $DEPLOY_USER@$DEPLOY_HOST 'cd badger-app && docker-compose build web'

echo "restarting web container"
ssh $DEPLOY_USER@$DEPLOY_HOST 'cd badger-app && docker-compose -f docker-compose.yml -f production.yml up --no-deps -d web'

echo "success!"

exit 0