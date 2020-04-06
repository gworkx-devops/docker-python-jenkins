## HOW TO BUILD A DOCKER IMAGE

+ Building an API based Python WebApp - Flask or Bottle image:

```sh
#! /bin/bash

#
# baking a python/jenkins docker image
#
# docker image build --no-cache -f Dockerfile.jenkins -t gworkx/python:jenkins .


# image baking - python/jenkins
#
docker image build -f Dockerfile.jenkins -t gworkx/python:jenkins .

#
# push the image to a remote registry
#
docker push gworkx/python:jenkins
```

## HOW TO SPIN A CONTAINER FROM THE IMAGE

+ To instantiate a standalone docker container from the image execute:

```sh
#! /bin/bash

#
# start python web server with bottle or flask module
#
docker container run -d --name python-app-01 -p 8000:8000 -v $PWD/app-code:/app:ro gworkx/python:jenkins
```

## HOW TO DEPLOY MICROSERVICES WITH DOCKER SWARM

+ Setup a single node docker swarm cluster:

```sh
#! /bin/bash

#
# initialize single node swarm cluster
#
docker swarm init
```

+ To orchestrate docker microservices deployment execute:

```sh
#! /bin/bash

#
# orchestrate microservice deployment
#
docker stack deploy -c docker-compose.yml conda
```
