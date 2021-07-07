# tozny-python-example
## Overview
This app implements a simple Rock/Scissors/Paper game. The implementation demonstrates how to use the Tozny a3db API to manage shared and private data between Tozny clients.
## Installation
Assuming that you have python 3.9 installed the following do the following to get the API setup.
```
     git clone https://github.com/timeonator/tozny-python-example
     move to the cloned directory (tozny-python-example
     python3 -m venv <.venv>
     source .venv/Scripts/activate
     python -m pip install --upgrade pip
     pip install -r requirements.txt
```
## Setting Up Tozny

### create a Tozny account
(Refer to Tozny docs)
### Initialize A Game
Describe how to run scripts to initialize game participantes, and setup sharing between the Tozny clients.

## Running The API
I use a bash shell and start the app api with the following:
     flask run
The api is still under development and runs on the localhost at port 5000. I'm using visual studio for my dev environment and testing the api with Thunder Client https://www.thunderclient.io/. I am still new to this plugin so I don't have any of the api tests in the repository yet. Postman or curl would also work.

    flask run
    
##  Tozny Record Type
The API is implemented with two underlying Tozny record types (**record_type**), **outcome** and **moves**
The **outcomes** record_type contains the results for game rounds and is indexed by <round>. Clients in the scope of this game share the winner data.
```
     data={'winner':<user>},
     plain={'round':<round>}
```
The **moves record_type** contains private data indicating how the a user moved for a given round. Eash move is securely hidden from the other play put shared with the *judge* of the game. More specifically, the move element below is shared with the writer of the record and the *judge* of the game.
```
     data={'move':<move>},
     plain={'round':<round>,'user':<user>}
```
## API
### POST /move/\<user\>/\<round\>/<move\>
#### Description
Write a **moves record_type**
#### Response
```
     "data": {
          "move":<move>
     }
```
#### Example
```
     localhost:5000/move/alicia/25/scissors
```
If the request succeeds the response will be the data from the writtne record in json.
In this case
``` 
     {
     "move": "scissors"
     }
```
### GET /move/\<user\>/\<round\>
#### Description
Read a **moves record_type**
#### Response
```
     {
          "move":<move>
     }
```
#### Example
```
     GET localhost:5000/move/alicia/25
```
If the request succeeds the response will be the data from the writtne record in json.
In this case where <user> == alicia and <round> == 25 we have
``` 
     {
     "move": "scissors"
     }
```
### GET /status/\<user\>/\<round\>
#### Response
returns the record for the given <user> and <round> assuming that one exists otherwise returns a record not found message
```
     {
     "winner":<user>
     }
```
#### Example
```
     localhost:5000/status/alicia/1
```
If the request succeeds the response will be the data from the retrieved record in json.
if alicia won round 1 this would be
``` 
     {
     "winner": "alicia"
     }
```
### POST /winner/\<judge\>/\<user\>/\<round\>
#### response
#### example
Write a reccord indicating that alicia is the winner of round 2
```
     localhost://5000/winner/clarence/alicia/2
```
if the request succeeds the response will be the data part of the stored record
```
     {
          "winner": "alicia"
     }
```
## Utility Programs
The utility programs are all in cli-utils

### delete
    usage: delete.py [-h] user type
deletes all the record in the type collection.

### list_all
     python list_all.py
List every table for your account on Tonzy and it's verbose including table name, meta.record_id, and meta.plain data

### python sharing_test
     python sharing_test.py
The is code I used to experiment with sharing. It was handy for figuring out how sharing works. It has code for setting up sharing between people, and testing out how sharing warks with Search().

### moves.py and outcome.py
     python moves.py
     python outcome.py
are programs I used to initialize sharing for my app and generate some records for testiing the api.


