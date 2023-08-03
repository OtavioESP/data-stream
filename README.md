# STREAM
A data stream service made using uvicorn and FastApi with python 3.8

This repository is a training that i made to practice data stream and its initial concepts such as a solution for big data transfers.

The projects consists of a local HTTP API, and a client to use the server.
It can also be consumed by your browser, Postman or anything that can make a HTTP request.

The server main functionality is to read a large .CSV file that will not be present in the this repo.

There are two routes for you to use, both streams data from the server to the client.

* - /get-word/your word here
-  The server will stream to the client until he finds the first word in the file

* - /all-words
- The server will stream all the data from the CSV file to client


# Requirements
* Python 3.8.x

# Run
* pip install -r requirements.txt
* In consts.py file change the HOST, PORT, FILE and DEBUG for you respective needs
* HOST should be the host you want to run ex: `192.168.1.0` or `localhost`
* PORT should be the server port you want to run ex: `8000`, `8001`, `3030`
  Check if there is already something running on the port of preference.
* DEBUG should be True if you want the server to print the data, else it wont
* FILE should be the location from the repository ex: './MY_FILE.csv'
* python main.py

# Now server is running and can be consumed
  
