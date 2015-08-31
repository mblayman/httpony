from httpie.cli import parser
from httpie.context import Environment
from werkzeug.wrappers import Response

from httpony import __version__


def make_app():
    """Make a WSGI app that has all the HTTPie pieces baked in."""
    env = Environment()
    httpie_args = parser.parse_args(args=['/'], env=env)
    server = 'HTTPony/{0}'.format(__version__)

    def application(environ, start_response):
        response = Response(headers={'Server': server})
        return response(environ, start_response)

    return application
