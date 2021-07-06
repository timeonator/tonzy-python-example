# tonzy-python-example
## Installation
Assuming that you have python 3.9 installed the following do the following to get the API setup.
     git clone https://github.com/timeonator/tonzy-python-example
     move to the cloned directory (tonzy-python-example
     python3 -m venv <.venv>
     source .venv/Scripts/activate
     python -m pip install --upgrade pip
     pip install -r requirements.txt

## Running The API
I use a bash shell and start the app api with the following:
     flask run
The api is still under development and runs on the localhost at port 5000. I'm using visual studio for my dev environment and testing the api with Thunder Client https://www.thunderclient.io/. I am still new to this plugin so I don't have any of the api tests in the repository yet. Postman will work.

    flask run
    
## API Spec
This API is uses two record =_types to manage the underlying data, moves and outcomes. 

#### outcome record_type
The outcomes record_type contains the results for game rounds and is indexed by <round>
```
data={'winner':<user>},
plain={'round':<round>}
```

#### moves record_type
The moves record_type contains private data indicating how the given user moved for a given round.
```
     data={'move':<move>},
     plain={'round':<round>,'user':<user>}
```
Players data is shared by each player with the judge but not among the players.
     
### GET /status/<user>/<round>
returns the record for the given <user> and <round> assuming that one exists otherwise returns a record not found message
#### Example
     /status/alicia/1
Assuming that alicia won roun 1 the endpoint will find a record_type outcomes containing
     {
     "winner": "alicia"
     }

### PUSH /winner/<judge>/<user>/<round>
writes a record indicating that <user> won <round>

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


