# Orders App

This repository contains the source code for the Orders App, a simple application for managing orders. It is a test project that aims to fulfill specific technical requirements.

Technical Requirements:

- Create two applications: Store and Warehouse.
- The Store application should provide functionality for creating orders through the admin page.
- The Warehouse application should be able to receive orders through the REST API and update the information back to the Store.
- Whenever an order is created in the Store, it should be synchronized with the Warehouse. If any information is changed in the Warehouse, it should update the corresponding information in the Store (e.g., status).
- The applications should communicate exclusively through REST API and should not share the same database. Each application should have its own separate database.
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)

## Installation

To install and run this project, follow these steps:

1. Clone the repository: 
```sh
$ git clone https://github.com/ruslanhq/orders_app.git
$ cd orders_app
```
2. Rename *.env.example* to *.env*:
```sh
$ mv .env.example .env
```
3. Run command for up docker containers and start application:
```sh
$ make up
```

## Usage

After running the application (about 30 second), navigate to the specified local URL in your web browser. From there, you can create, update, and delete orders.

[Store app](http://127.0.0.1:8000/admin/)

[Warehouse app](http://127.0.0.1:8001/admin/)

**On the login page, enter the following credentials:**

`Username: admin`

`Password: admin`


## Endpoints

The Orders App provides the following endpoints:

1. **PUT api/store/order/update/**: Updates an existing order. The request body should contain the updated order details.
2. **POST api/warehouse/order/create/**: Creates a new order. The request body should contain the order details.
3. **PUT api/warehouse/order/update/**: Updates an existing order. The request body should contain the updated order details.
