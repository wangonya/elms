# Leave Management System [![Build Status](https://travis-ci.com/wangonya/elms.svg?branch=master)](https://travis-ci.com/wangonya/elms)

Simple leave management system.

## [Frontend](https://github.com/wangonya/elms-frontend.git)

## Api Routes
### Auth
* [x] `POST /register` - create a user account
* [x] `POST /login` - login user

### Leave Management
* [x] `POST /leaves` - post a leave request
* [x] `GET /leaves` - fetch all leave requests
* [x] `GET /leaves/uid` - fetch specific user leave requests
* [x] `PATCH /leaves/leaveid/withdraw` - withdraw leave request
* [x] `PATCH /leaves/leaveid/cancel` - cancel leave request

## Tech Stack

* Backend - Python (Flask)
* Database - SQLite
* Frontend - HTML / CSS/ JS
* Testing - pytest
* CI - Travis
* Hosting - Heroku


