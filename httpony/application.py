from httpie.context import Environment
from werkzeug.wrappers import Response


def make_app():
    """Make a WSGI app that has all the HTTPie pieces baked in."""
    env = Environment()

    def application(environ, start_response):
        response = Response()
        return response(environ, start_response)

    return application
