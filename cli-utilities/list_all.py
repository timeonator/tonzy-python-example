import e3db
from e3db.types import Search
import game_utils

client = e3db.Client(e3db.Config.load('clarence'))


query = Search(include_data=True, include_all_writers = True)
results = client.search(query)
print("records returned", len(results))
for record in results:
    print("record id", record.meta.record_id, record.meta.record_type)
    print("plain data", record.meta.plain)
    print("record data", record.data)
