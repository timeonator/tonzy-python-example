import e3db
from e3db.types import Search

def read_client_id(name):
    config = e3db.Config.load(name)
    return config['client_id']

def write_record(user, record_type, data):
    client = e3db.Client(e3db.Config.load(user))
    record_id = client.write(record_type, data)
    return(record_id)

def read_record_by_id(user, id):
    client = e3db.Client(e3db.Config.load(user))
    return client.read(id)

def read_record_all(user, record_type):
    client = e3db.Client(e3db.Config.load(user))
    query = Search(include_data=True,include_all_writers = True).match(record_types=[record_type])   
    for record in client.search(query):
        print("record id", record.meta.record_id)
        if (record_type=='history' or record_type=='creepy'):           
            print(record.data)
        else:
            print("unkown record type")
        # 

def print_record_list(list):
    for record in list:
        print("record id", record.meta.record_id)
        print(record)

def print_all():
    results = client.search(Search())
    print_results("Getting all records", results)

def print_results(message, results):
    print(message)
    print([i.meta.plain for i in results])
    print()


if (__name__ == "__main__"):
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
       
    read_parser = subparsers.add_parser('read')
    read_parser.add_argument("user")
    read_parser.add_argument("type")

    read_parser.set_defaults(func=read_record_all)

    args = parser.parse_args()
    args.func(args)



