# STREAM
A data stream service made using uvicorn and FastApi using python 3.8

This repository is a training that i made to practice data stream and its initial concepts such as a solution for big data transfers.

The projects consists of a local API with HTTP server, and a client to use the server.
It can also be consumed by your browser, Postman or anithing that can make a HTTP request on a server.

The server main functionality is to read a large .CSV file that will not be present in the this repo.

There are two routes for you to use, both streams data from the server to the client.
1 - /get-word/<your word here>
* The server will stream to the client until he finds the first word in the file

2 - /all-words
* The server will stream all the data from the CSV file to client


# Requirements
* Python 3.8.x

# Run
* pip install -r requirements.txt
* In consts.py file change the HOST, PORT and FILE for you respective needs
* FILE variable should be the location from the repository ex: './MY_FILE.csv'
* python main.py

# Now server is running and can be consumed
  
