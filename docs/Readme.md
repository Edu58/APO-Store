# APO-Store

An e-commerce REST API built with Django.

## Getting Started

````
git clone https://github.com/Edu58/APO-Store.git
````
````
cd APO-Backend
````
````
python3 -m venv venv
````

````
source venv/bin/acivate
````

````
pip install -r requirements.txt
````

````
python3 manage.py runserver
````

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [RabbitMQ](https://www.rabbitmq.com/)
- [Redis](https://redis.io/)
- [PotsgreSQL](https://www.postgresql.org/)

### Installing

- Setup RabbitMQ on your machine. You can follow RabbitMQ [documentation](https://www.rabbitmq.com/install-debian.html) for this.

- Setup Redis on your machine. You can follow Redis [documentation](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)

- clone the repository
````
git clone https://github.com/Edu58/APO-Store.git
````

- Navigate into teh APO-Backend directory
````
cd APO-Backend
````

- Create a virtual environment
````
python3 -m venv venv
````

- Activate the virtual environment
````
source venv/bin/acivate
````

- Install all the required packages from the provided requirements.txt file
````
pip install -r requirements.txt
````

- Create a .env file in the APO-Backend directory
````
touch .env
````

- Add the following configuration inside the .env file
````
SECRET_KEY='<add your django secret key here>'
DEBUG=<will either be True or False>
DB_TYPE="postgresql"
DB_NAME=<you database name>
DB_USER=<your database username>
DB_PASSWORD=<you database password>
ALLOWED_HOSTS=<allowed hosts e.g. 127.0.0.1>
````

- Start the project from the APO-Backend directory
````
python3 manage.py runserver
````

- View the Swagger API documentation by entering the following url in your browser URL bar. Make sure the server is running
````
http://127.0.0.1:8000/api/v1/docs/swagger/
````

- View the Redoc API documentation by entering the following url in your browser URL bar. Make sure the server is running
````
http://127.0.0.1:8000/api/v1/docs/redoc/
````

## Running the tests

- From the APO-Backed folde run the following command
````
python3 manage.py test
````

## Built With

  - [Django](https://www.djangoproject.com/)
  - [Django Rest Framework](https://www.django-rest-framework.org/)
  - [RabbitMQ](https://www.rabbitmq.com/)
  - [Redis](https://redis.io/)
  - [PotsgreSQL](https://www.postgresql.org/)
  - [Celery](https://docs.celeryq.dev/en/stable/index.html)

## Contributing

Contributions are very much welcome. Feel free to clone this repository and make changes that you think would benefit anyone using this project. After this create a pull request, it will be reviewed and accepted if it is deemed worthy.

Contributions to create a working front end are also welcome.

## Authors

  - **Edwin Karimi** -
    [Edu58](https://github.com/Edu58)

See also the list of
[contributors](https://github.com/PurpleBooth/a-good-readme-template/contributors)
who participated in this project.

## License

This project is licensed under the MIT License see the [LICENSE.md](LICENSE) file for
details

## Acknowledgments

  - Hat tip to anyone whose code is used
