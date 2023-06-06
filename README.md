# Requirements
 - Docker

# Instalation

To install the application run below commands in terminal:

> git clone https://github.com/MarkSkof/aplikacija
>
> cd aplikacija 
> 
> docker-compose up -d

# Usage

## Populating database with data

Application uses [JSON Placeholder](https://jsonplaceholder.typicode.com) to get data to populate the database.
To populate the database send a POST request to endpoint http://127.0.0.1:8000/api/populate_database/. Request can be 
sent with tools such as Postman, VisualStudio with  Thunder Client extension or by using Python requests library.

Example of using Python requests library to populate database:
```python
import requests
requests.request("POST", "http://127.0.0.1:8000/api/populate_database/")
```

## Retrieving data

To retriv all entries from database tables, send a GET request to endpoint http://127.0.0.1:8000/api/<table_name>/.
Replace <table_name> with a name of the table you wish to retriv data from.

Example of retrieving all entries from post table:
```python
import requests
requests.request("GET", "http://127.0.0.1:8000/api/post/", data={"title": "new post",
                                                                 "body": "new body",
                                                                 "userId": 1})
```

## Creating new entries

To create new entry in database, send a POST request to endpoint http://127.0.0.1:8000/api/<table_name>/.
Replace <table_name> with a name of the table in wish you wish to create new entry.

Example of creating new entry in post table:
```python
import requests
requests.request("POST", "http://127.0.0.1:8000/api/post/", )
```

## Updating and deleting data

To update data send a PUT request and to delete data send DELETE request to endpoint
http://127.0.0.1:8000/api/<table_name>/<entry_id>/. Replace <table_name> with a name of the table and <entry_id> with
the id of an entry you wish to update or delete.

Example of deleting an entry with id 1 from post table:
```python
import requests
requests.request("DELETE", "http://127.0.0.1:8000/api/post/1/")
```

Example of updating ana entry with id 1 from post table:
```python
import requests
requests.request("PUT", "http://127.0.0.1:8000/api/post/1/", data={"title": "updated post",
                                                                   "body": "updated body",
                                                                   "userId": 1})
```

## Retrieving a single post and all its comments

To retriv a single post with all of its comments sen a GET request to endpoint http://127.0.0.1:8000/api/post/<post_id>/.
Replace <post_id> with an id of the post which you want to retriv.

Example of retrieving a post with id 1 and all of its comments:
```python
import requests
requests.request("GET", "http://127.0.0.1:8000/api/post/1/comments/")
```


## Retrieving all posts of a specific user

To retriv all posts that were mad by a specific user send a GET request to endpoint
http://127.0.0.1:8000/api/user/<user_id>/posts/. Replace <user_id> with an id of a user who's
comments you wish to retriv.

Example of retrieving posts of a user with id 1:
```python
import requests
requests.request("GET", "http://127.0.0.1:8000/api/user/1/posts/")
```
























