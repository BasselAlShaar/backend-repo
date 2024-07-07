import yaml


class Server:
    def __init__(self, config):
        self.config = config

    def run(self):
        if self.config.get("run_localhost"):
            print("Running server in localhost mode")
        else:
            print("Running server in production mode")


with open("../fullstack-repo/config.yaml", "r") as file:
    config = yaml.safe_load(file)

server = Server(config)
server.run()
