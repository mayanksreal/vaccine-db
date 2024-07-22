# Vaccination Tracking System

Python-based application making use of Tkinter for GUI and MySQL-python-connector to connect to a local MySQL database, allowing user to perform CRUD operations. 

## Features

- **View Records**: Fetches and displays all vaccination records from the database.
- **Add Records**: Form to add a new vaccination record to the database.
- **Update Records**: Form to update an existing vaccination record in the database.
- **Delete Records**: Option to delete a vaccination record from the database.

## Requirements
- Python 3.x
- Tkinter
- MySQL Server (local)
- mysql-connector-python 

## Installation

1. Clone the repository:

```sh
git clone https://github.com/mayanksreal/vaccine-db.git
cd vaccine-db
```

2. Install dependencies

```sh
pip install mysql-connector-python
```

3. Init local DB

```sql
create database vaccine;
create table vaccination( name VARCHAR(30) NOT NULL,
    status VARCHAR(30) NOT NULL,
    date DATE,
    employeeid INT NOT NULL,
    PRIMARY KEY (employeeid));
```

4. Update MySQL username and password

```python
    host="localhost",
    user="USERNAME", #ex. root
    password="PASSWORD", #ex. pw

```

## Preview

1. Adding a new record  
   <p align="center">
     <img src="https://github.com/mayanksreal/vaccine-db/blob/main/preview/add.gif" width="800" />
   </p>

2. Deleting a record  
   <p align="center">
     <img src="https://github.com/mayanksreal/vaccine-db/blob/main/preview/del.gif" width="800" />
   </p>


