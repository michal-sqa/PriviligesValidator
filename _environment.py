class Environment:

    def __init__(self, server_and_port):
        self.server_and_port = server_and_port

uat = Environment('none')

environments = {}
environments['uat'] = uat