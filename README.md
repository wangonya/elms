# Leave Management System [![Build Status](https://travis-ci.com/wangonya/elms.svg?branch=master)](https://travis-ci.com/wangonya/elms)

Simple leave management system.

A user should be able to 
* [ ] register & login to the system through the first page of the application
* [ ] see eligibility details (like how many days of leave he/she is eligible for etc)
* [ ] see leave history
* [ ] apply for leave, specifying the from and to dates, reason for taking leave, address for communication while on leave, etc. 
Email should be sent automatically to admin
* [ ] see current leave applications 
* [ ] withdraw leave application (which has not been approved yet)
* [ ] cancel leave (which has been already approved) - will need to be approved by the **admin**
* [ ] **admin** - see the leave applications that are submitted for approval
* [ ] **admin** - approve/reject the leave applications. Email should be sent automatically to user

## Tech Stack

* Backend - Python (Flask)
* Database - PostgreSQL
* Frontend - Angular
* Testing - pytest
* CI - Travis


