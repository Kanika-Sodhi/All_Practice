# Code test solution for data engineering candidates

## Purpose

Ingesting people and place table in respective database and make the insights from the ingested data.

Tables - person and place two tables are there with primary foreing relation between them.


### Building the images

This will build all of the images referenced in the Docker Compose file with ingestion container and summary container

```
docker-compose build
```

### Starting MySQL

To start up the MySQL database. This will will take a short while to run the database’s start-up scripts.

```
docker-compose up database
```

if you want to connect to the MySQL database via the command-line client. This may be useful for looking at the database schema or data.

```
docker-compose run database mysql --host=database --user=codetest --password=swordfish codetest
```

### scripts
to run people and place schema files

```
docker-compose run database mysql --host=database --user=codetest --password=swordfish codetest people_space_schema.sql
```

Then make sure that the containers have been built with `docker-compose build` and run one or more of the sample programmes with:

```
docker-compose run ingestion-container
docker-compose run summary-container
```

the programme loads data from the data/people.csv and data/place.csv file into that table, 
and exports data from the database table to a JSON file in the data folder. Note that the scripts do not truncate the table, 
so each one you run will add additional content.

### Cleaning up

To tidy up, bringing down all the containers and deleting them.

```
docker-compose down
```
