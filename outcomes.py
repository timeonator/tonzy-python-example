import e3db
from e3db.types import Search
from tzutils import read_client_id

# sharing causes an error once a record has been written
    # raise errors[response.status_code]e3db.exceptions.
    # ConflictError: Error during API operation: 
    # Conflict error: Existing item cannot be modified: HTTP 409
# But the initial share worked without error and functionally.
# So leave this commented out until issue is resolved. Alternately
# setup sharing as part of the game setup.
client = e3db.Client(e3db.Config.load('clarence'))
# client.share('outcome',read_client_id('alicia'))
# client.share('outcome',read_client_id('bruce'))

client.write('outcomes', data={'bruce':'scissors'}, plain={'round':'0'})