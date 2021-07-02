from os import path
import e3db


def main():
    users = {
        'alicia'  :"24ef2bdf480eafa4613affeafb26d4f2ca451288593198af6499577d909a6b45",
        'bruce'   :"72d7a1bf16dbacfaf564bbc8474747d262d73693f2602793eec82d6cf3d65734",
        'clarence':"c04990702e09f1ded991317929bee0da7305d2c699c21c3a1fd3e2332619bc11"
    }

    for client_name, token in users.items():
        public_key, private_key = e3db.Client.generate_keypair()

        client_info = e3db.Client.register(token, client_name, public_key, private_key, backup=True)

        api_key_id = client_info.api_key_id
        api_secret = client_info.api_secret
        client_id = client_info.client_id

        config = e3db.Config(
            client_id,
            api_key_id,
            api_secret,
            public_key,
            private_key,
            # public_signing_key,
            # private_signing_key
        )

        # Optionally, if you want to save this Configuration to disk, do the following:
        config.write(client_name)

    def read_client_id(name):
        config = e3db.Config.load(name)
        return config.client_id

    def config_sharing(grantor, grantee, record_type):
        client = e3db.Client(e3db.Config.load(grantor))
        client.share(record_type,read_client_id('grantee'))    

    config_sharing('clarence', 'alicia', 'winner')
    config_sharing('clarence', 'bruce',  'winner')

    config_sharing('alicia', 'clarence', 'player1')
    config_sharing('bruce',  'clarence', 'player2')



