import e3db
from e3db.types import Search


def read_client_id(name):
    config = e3db.Config.load(name)
    return config['client_id']