# Music-Aggregator

## How to run
`docker-compose.yaml` - development config\
`docker-compose.prod.yaml` - production config

1. With containers:
```commandline
sudo docker-compose -f <docker-compose config> up -d --build
```
Application will available on http://localhost.
2. Without containers
    * Run mongodb
    * (Optionally) Run SQL db
    * Set environment variables:
        - FLASK_APP=project/app:run()
        - FLASK_ENV=(development|production)
        - (Optionaly) DATABASE_URL=postgresql://flask_user:flask_password@postgres:5432/flask_dev
        - MONGODB_DATABASE=flaskdb_dev
        - MONGODB_USERNAME=flaskuser
        - MONGODB_PASSWORD=flaskuserpassword
        - MONGODB_HOSTNAME=mongodb
    * Run application: 
      ```commandline
      python -m flask run -h 0.0.0.0 -p 5000
      ```

## Deployment

Latest version deployed at http://104.248.206.229/
