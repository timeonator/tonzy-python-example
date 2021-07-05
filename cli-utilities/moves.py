import e3db
from e3db.types import Search
from tzutils import read_client_id

# client = e3db.Client(e3db.Config.load('alicia'))
# client.share('moves',read_client_id('clarence'))
# client = e3db.Client(e3db.Config.load('bruce'))
# client.share('moves',read_client_id('clarence'))


client = e3db.Client(e3db.Config.load('bruce'))
client.write('moves', data={'bruce':'scissors'}, plain={'round':'1'})

client = e3db.Client(e3db.Config.load('alicia'))
client.write('moves', data={'alicia':'scissors'}, plain={'round':'1'})
