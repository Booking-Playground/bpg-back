<h1 align="center">Booking Playground</h1>

## Tech stack
1. Python 3.9.16
2. Django 3.2.20
3. DRF 3.14.0
4. Postgres 13
5. Nginx 1.24.0
6. Docker

## Installing and running locally

1. Install [Docker](https://www.docker.com/get-started)

2. Clone the repo

    ```sh
    $ git clone https://github.com/sblvkr/booking_sports.git
    $ cd booking_sports
    ```

3. Create environment to the example(.env.example)
    ```sh
    $ nano/vim .env
    ```

4. Run

    ```sh
    $ make run_dev_docker
   or
    $ docker compose -f docker-compose.dev.yml up
    ```
   

## License

[GNU](LICENSE)

Feel free to contact us via email [sblvkr@gmail.com](mailto:sblvkr@gmail.com).