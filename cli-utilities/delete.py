import e3db

from e3db.types import Search
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("user")
    parser.add_argument("type")
    args = parser.parse_args()    
    user =args.user
    record_type = args.type
    delete(user,record_type)
    
def delete(user,record_type):
    try:
        client = e3db.Client(e3db.Config.load(user))
    except:
        print(user + " is not a registered player")
        quit()

    query = Search(include_data=True).match(record_types=[record_type])
    results = client.search(query)
    print("deleting " + str(len(results)) + " records from " + record_type)
    for record in results:
        print("record id", record.meta.record_id)
        client.delete(record.meta.record_id,record.meta.version)

if (__name__ == "__main__"):
    main()



