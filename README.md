# MIAC project

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dbdae2f9a98d48af88f45a4c11991c55)](https://app.codacy.com/gh/KochankovID/MIAC?utm_source=github.com&utm_medium=referral&utm_content=KochankovID/MIAC&utm_campaign=Badge_Grade_Settings)
[![deepcode](https://www.deepcode.ai/api/gh/badge?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybTEiOiJnaCIsIm93bmVyMSI6IktvY2hhbmtvdklEIiwicmVwbzEiOiJNSUFDIiwiaW5jbHVkZUxpbnQiOmZhbHNlLCJhdXRob3JJZCI6MjkyMTMsImlhdCI6MTYyMzQ5MTE4NH0.xy5jziE9VhAexK_1yy1CTxfq01YGCvXoy9X2VzrS9U4)](https://www.deepcode.ai/app/gh/KochankovID/MIAC/_/dashboard?utm_content=gh%2FKochankovID%2FMIAC)

### Requirements

- Python3
- Docker

### Install packages (only for start without docker)

`pip install -r ./miac/requirements.txt`

## How to run docker-compose

1. Create .env file in docker-compose directory (one can rename .env.example)
2. Fill .env file with the following variables (you don't need to do in explicitly if you use .env.example):
   * `SECRET_KEY` = django secret key
   * `DEBUG` = enable or disable debug in django
   * `REDIS_URL` = url for connection to redis (django cache)
   * `REDIS_SESSION_URL` = url for connection to redis (django sessions cache)
   * `DATABASE_URL` = url for connection to postgresql
   * `DB_NAME` = database name
   * `DB_USER` = database username
   * `DB_PASSWORD` = database password
   * `DB_PORT` = port of the database in your local network
   * `REDIS_PORTS` = port of the redis in your local network
3. Run `docker-compose up` in the root repository folder