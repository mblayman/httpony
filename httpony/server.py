# Copyright (c) 2015, Matt Layman

import logging
from wsgiref.simple_server import demo_app

from werkzeug.serving import run_simple


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

    # TODO: Stop using the demo app.
    run_simple(hostname, port, demo_app)


if __name__ == '__main__':
    main()
