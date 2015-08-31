# Copyright (c) 2015, Matt Layman

import logging

from werkzeug.serving import run_simple

from httpony.application import make_app


def main():
    """Serve up some ponies."""
    hostname = 'localhost'
    port = 8000
    print (
        "Making all your dreams for a pony come true on http://{0}:{1}.\n"
        "Press Ctrl+C to quit."
    ).format(hostname, port)

    # Hush, werkzeug.
    logging.getLogger('werkzeug').setLevel(logging.CRITICAL)

    # TODO: app factory
    # TODO: plugin manager
    # TODO: env
    # TODO: args
    # TODO: request
    app = make_app()
    run_simple(hostname, port, app)


if __name__ == '__main__':
    main()
