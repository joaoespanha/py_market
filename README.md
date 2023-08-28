# Py Market

Welcome to the Py Market  app! This app is designed to solve your the problem of a market place to connect sellers and buyers

## Getting Started

Follow these steps to set up and run the Py_market app on your local machine.

### Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Docker

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:joaoespanha/py_market.git
   ```
2. Navigate to the app directory:

    ```bash
    cd py_market
    ```

2. Configure your docker-compose to define your MySql container credentials:
    - Change the MYSQL_PASSWORD db service variable to your desired password
    - Change the MYSQL_ROOT_PASSWORD db service variable to your desired  root password

2. Configure your .env to define your MySql container credentials:
    - Change the MYSQL_PASSWORD variable to your desired password
    - Rename the file from '.env.example' to '.env'

2. Run your docker compose:
    ```bash
    docker-compose up -d
    ```
3. Atatch terminal ondocker py_market web container:
    ```bash
    docker exec -it py_market_web /bin/bash
    ```
3. Run database migrations inside the container:
    ```bash
    python3 manage.py migrate
    ```
3. Create a admin user via terminal inside the container:
    ```bash
    python3 manage.py createsuperuser
    ```
3. Run the app on browser:
    http://localhost:8000/

3. Log In:
    - If you want to log as admin use your super user credetials on log in page
    - If you want to sig up as a new user click on the sign up utton and fill the user form

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/fix: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request.


## Created by: [Joao Espanha's GitHub](https://github.com/joaoespanha)

