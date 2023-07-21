<h1 align="center">Booking Playground</h1>

## Description
Booking PlayGround is an internet service that facilitates sports facility bookings and payments. It allows users to search for sports venues based on sport type, date, cost, and facility features. 

Users can book training hours online, ensuring a reliable and transparent reservation process visible to administrators and other users. Booking PlayGround does not charge any additional fees or commissions and enables direct payment to the sports organizations. 

Its goal is to streamline the dialogue between users and sports facilities, making the booking process fast and convenient.

## Demo
progres...

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

3. Create environment to the example(.env.example).

   For a quick start, you only need to add SECRET_KEY. Use the service [djecrety.ir](https://djecrety.ir/) (or similar) to create it.
   ```sh
    $ cp .env.example .env
    $ nano/vim .env
    ```

4. Run

    ```sh
    $ make run_dev
   or
    $ docker compose -f docker-compose.dev.yml up
    ```
   

## License

[MIT](LICENSE)

Feel free to contact us via email [sblvkr@gmail.com](mailto:sblvkr@gmail.com).