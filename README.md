# tonzy-python-example
## Installation
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
Unfortunately I haven't got the spec ready yet but fortunately it's simple so far so you can probably read app.py and figure it out for now.


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


