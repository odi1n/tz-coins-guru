# Tz coins guru

## Warning

User authorization is done. You need to register the user, log in and you can interact with the API

## Run project

1. Clone project: `git clone PROJECT_PATH`
2. Open directory project: `cd PROJECT_PATH`
3. Change file: `.env.example` in `.env`
4. Set Tokens in file `.env`
5. Docker build: `docker-compose build`
6. Docker up: `docker-compose up`

## Endpoind

|Link|Request|Infomation|
|:---|:---:|:---|
|/api/v1/signup|POST|Create User|
|/api/v1/login|POST|Login User|
|/api/v1/user|GET|Get user me|
|/api/v1/accounts|POST|Addition twitter link user|
|/api/v1/accounts/:twitter_username|GET|Get information on username twitter|
|/api/v1/accounts/status/:session_id|GET|Get information on status|
|/api/v1/tweets/:twitter_id|GET|Get Tweet on twitter id usernames|
