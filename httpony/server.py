# Copyright (c) 2016, Matt Layman

import logging

from httpie.plugins import plugin_manager
from werkzeug.serving import run_simple

from httpony.application import make_app


def main():
    """Serve up some ponies."""
    hostname = 'localhost'
    port = 8000
    print (
        "Making all your dreams for a pony come true on http://{0}:{1}.\n"
        "Press Ctrl+C to quit.\n"
    ).format(hostname, port)

    # Hush, werkzeug.
    logging.getLogger('werkzeug').setLevel(logging.CRITICAL)

    plugin_manager.load_installed_plugins()
    app = make_app()
    run_simple(hostname, port, app)


if __name__ == '__main__':
    main()
