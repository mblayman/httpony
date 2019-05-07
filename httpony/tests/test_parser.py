# Copyright (c) 2019, Matt Layman and contributors

import pytest

from httpony import server


def make_argv(arguments=None):
    """Make an argument list suitable for the parse function."""
    argv = ["httpony"]
    if arguments:
        argv.extend(arguments)
    return argv


def test_listen_default():
    argv = make_argv()
    args = server.parse(argv)
    assert args.listen == "localhost"


def test_listen():
    argv = make_argv(["--listen", "0.0.0.0"])
    args = server.parse(argv)
    assert args.listen == "0.0.0.0"


def test_port_default():
    argv = make_argv()
    args = server.parse(argv)
    assert args.port == 8000


def test_port():
    argv = make_argv(["--port", "8080"])
    args = server.parse(argv)
    assert args.port == 8080


def test_invalid_port():
    argv = make_argv(["--port", "broken"])
    with pytest.raises(SystemExit):
        server.parse(argv)
