## HOW TO BUILD A DOCKER IMAGE

+ Building an API based Python WebApp - Flask or Bottle image:

```sh
#! /bin/bash

#
# baking a python/conda docker image
#
# docker image build --no-cache -f Dockerfile.conda -t gworkx/datascience:conda-workshop-latest .


# image baking - python/conda
#
docker image build -f Dockerfile.conda -t gworkx/datascience:conda-workshop-latest .

#
# push the image to a remote registry
#
docker push gworkx/datascience:conda-workshop-latest
```

## HOW TO SPIN A CONTAINER FROM THE IMAGE

+ To instantiate a docker container from the image execute the following steps:

```sh
#! /bin/bash

#
# start python web server with bottle or flask module
#
docker container run -d --name python-app-01 -p 8000:8000 -v $PWD/app-code gworkx/datascience:conda-workshop-latest
```
