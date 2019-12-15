sudo docker container run -d --name python-app-01 -p 8000:8000 -v $PWD/app-code:/app:ro gworkx/datascience:conda-workshop-latest
