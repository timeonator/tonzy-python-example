import e3db
from e3db.types import Search

client = e3db.Client(e3db.Config.load('clarence'))

record_type='winner'

query = Search(include_data=True).match(record_types=[record_type])
results = client.search(query)
print("records returned", len(results))
for record in results:
    print("record id", record.meta.record_id)
    client.delete(record.meta.record_id,record.meta.version)

query = Search(include_data=True).match(record_types=[record_type])
results = client.search(query)
print("records returned", len(results))
for record in results:
    print("record id", record.meta.record_id)



