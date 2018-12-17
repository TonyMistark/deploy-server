import tornado.ioloop
import tornado.web
from app.urls import urls


def make_app():
    return tornado.web.Application(urls)


if __name__ == "__main__":
    port = 8887
    address = "0.0.0.0"
    print("start server %s:%s" % (address, port))
    app = make_app()
    app.listen(port=port, address=address)
    tornado.ioloop.IOLoop.current().start()
