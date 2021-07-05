import e3db
from e3db.types import Search
from tzutils import read_client_id

# recordbruce=game_utils.write_record('bruce','game', data = {
#     'name': 'bruce',
#     'round': '2',
#     'move': 'scissor'

# })
# recordalicia=game_utils.write_record('alicia','game', data = {
#     'name': 'alicia',
#     'round': '2',
#     'move': 'scissor'    
# })
# clientalicia = e3db.Client(e3db.Config.load('alicia'))
# clientalicia.share('game',"de1ec27d-599c-4f67-b31e-c37e7ea3e15d")
# clientbruce = e3db.Client(e3db.Config.load('bruce'))
# clientbruce.share('game',"de1ec27d-599c-4f67-b31e-c37e7ea3e15d")
def doit(q):
    
    results = client.search(q)
    print("Number of Records: ", results.total_results)
    for record in results:
        print("record id", record.meta.record_id, record.meta.record_type)
        print("plain data", record.meta.plain)
        print("record data", record.data)
    print('\n\n')

client = e3db.Client(e3db.Config.load('clarence'))
# client.share('outcome',read_client_id('alicia'))
# client.share('outcome',read_client_id('bruce'))

data = {
    'sugar':'sweet',
    'mice':'little feet'
}

# client.write('outcome', data, plain={'not':'yummy'})

client = e3db.Client(e3db.Config.load('clarence'))
query=Search(include_data=True,include_all_writers = True ).match(condition="AND", record_types=['outcome'], plain={'round':'1'})
print("Clarence Reads Data");
doit(query)

client = e3db.Client(e3db.Config.load('alicia'))
query=Search(include_data=True,include_all_writers = True ).match(condition="AND",record_types=['outcome'], plain={'round':'2'})
print("Alicia Reads Data");
doit(query)

client = e3db.Client(e3db.Config.load('bruce'))
query=Search(include_data=True,include_all_writers = True ).match(condition="AND",record_types=['outcome'], plain={'round':'3'})
print("Bruce Read's Data");
doit(query)

