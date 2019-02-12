from app.handlers.hexo_handlers import HexoHandler
from app.handlers.ss_port_handlers import SSPortHandler, UpdateSSPortHandler


urls = [
        (r"/hexo/", HexoHandler),
        (r"/ss/port/", SSPortHandler),
        (r"/ss/port/update/", UpdateSSPortHandler),
    ]
