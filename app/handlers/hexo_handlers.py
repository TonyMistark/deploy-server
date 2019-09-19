import os
from app.handlers.base import HandlerBase
from config import HexoConfig


class HexoHandler(HandlerBase):
    def get(self):
        os.system(f"sh {HexoConfig.hexo_server_deploy_abs_path}")
        self.write("<h1> update hexo server success.")

    def post(self):
        os.system(f"sh {HexoConfig.hexo_server_deploy_abs_path}")
        self.write("<h1> update hexo server success!")
