# Copyright (c) 2019, Matt Layman and contributors

import argparse
import logging
import sys

from httpie.plugins import plugin_manager
from werkzeug.serving import run_simple

from httpony.application import make_app


def main(argv=sys.argv):
    args = parse(argv)
    """Serve up some ponies."""
    hostname = args.listen
    port = args.port
    print(
        "Making all your dreams for a pony come true on http://{0}:{1}.\n"
        "Press Ctrl+C to quit.\n".format(hostname, port)
    )

    # Hush, werkzeug.
    logging.getLogger("werkzeug").setLevel(logging.CRITICAL)

    plugin_manager.load_installed_plugins()
    app = make_app()
    run_simple(hostname, port, app)


def parse(argv):
    """Parse the user arguments."""
    parser = build_parser()

    # argparse expects the executable to be removed from argv.
    args = parser.parse_args(argv[1:])

    return args


def build_parser():
    """Build the parser that will have all available commands and options."""
    description = (
        "HTTPony (pronounced aych-tee-tee-pony) is a simple HTTP "
        "server that pretty prints HTTP requests to a terminal. It "
        "is a useful aide for developing clients that send HTTP "
        "requests. HTTPony acts as a sink for a client so that a "
        "developer can understand what the client is sending."
    )
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-l", "--listen", help="set the IP address or hostname", default="localhost"
    )
    parser.add_argument("-p", "--port", help="set the port", default=8000, type=int)

    return parser


if __name__ == "__main__":
    main()
