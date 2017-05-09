from wsgiref.simple_server import make_server
from app import app


if __name__ == "__main__":
    host, port = "", 8080
    httpd = make_server(host=host, port=port, app=app)
    print("serving on port {}".format(port))
    httpd.serve_forever()