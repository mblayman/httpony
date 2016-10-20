# Copyright (c) 2016, Matt Layman

from __future__ import print_function

from httpie.cli import parser
from httpie.context import Environment
from httpie.output import streams
from requests.models import Request
from werkzeug.wrappers import Response
from werkzeug.wrappers import Request as WerkzeugRequest

from httpony import __version__


def make_app():
    """Make a WSGI app that has all the HTTPie pieces baked in."""
    env = Environment()
    args = parser.parse_args(args=['/'], env=env)
    args.output_options = 'HB'  # Output only requests.
    server = 'HTTPony/{0}'.format(__version__)

    def application(environ, start_response):
        # The WSGI server puts content length and type in the environment
        # even when not provided with the request. Drop them if they are empty.
        if environ.get('CONTENT_LENGTH') == '':
            del environ['CONTENT_LENGTH']
        if environ.get('CONTENT_TYPE') == '':
            del environ['CONTENT_TYPE']

        wrequest = WerkzeugRequest(environ)
        data = wrequest.get_data()
        request = Request(
            method=wrequest.method,
            url=wrequest.url,
            headers=wrequest.headers,
            data=data,
        )
        prepared = request.prepare()

        stream = streams.build_output_stream(
            args, env, prepared, response=None, output_options=args.output_options)
        streams.write_stream(stream, env.stdout, env.stdout_isatty)

        # When there is data in the request, give the next one breathing room.
        if data:
            print("\n", file=env.stdout)

        # Make dreams come true.
        response = Response(headers={'Server': server})
        return response(environ, start_response)

    return application
