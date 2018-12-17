from app.handlers.hexo_handlers import HexoHandler


urls = [
        (r"/hexo/update/", HexoHandler),
    ]