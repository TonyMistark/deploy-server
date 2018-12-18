import os
from app.handlers.base import HandlerBase


class HexoHandler(HandlerBase):
    def get(self):
        os.system("sh ~/sh/hexo_server_deploy.sh")
        self.write("<h1> update hexo server success")

    def post(self):
        os.system("sh ~/sh/hexo_server_deploy.sh")
        self.write("<h1> update hexo server success")
