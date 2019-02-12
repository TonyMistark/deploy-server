import os
from app.handlers.base import HandlerBase


class SSPortHandler(HandlerBase):
    def get(self):
        port = "8888"
        # os.system("sh ~/sh/update_ss_port_deploy.sh")
        self.write(f"<h1> ss port {port}")


class UpdateSSPortHandler(HandlerBase):
    def get(self):
        port = "8888"
        os.system("sh ~/sh/update_ss_port_deploy.sh")
        self.write(f"<h1> update ss port to {port}")

    def post(self):
        port = "8000"
        # os.system("sh ~/sh/update_ss_port_deploy.sh")
        self.write(f"<h1> update ss port to {port}")

