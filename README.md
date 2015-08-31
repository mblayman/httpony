# HTTPony

HTTPony (pronounced aych-tee-tee-pony) is a simple HTTP server
that pretty prints HTTP requests to a terminal.
It is a useful aide for developing clients that send HTTP requests.
HTTPony acts as a sink for a client
so that a developer can understand what the client is sending.

For example, this HTTPie request:

```bash
$ http :8000/pony
HTTP/1.0 200 OK
Content-Length: 0
Content-Type: text/plain; charset=utf-8
Date: Mon, 31 Aug 2015 03:22:38 GMT
Server: HTTPony/0.1
```

Shows in HTTPony as:

```bash
$ httpony
Making all your dreams for a pony come true on http://localhost:8000.
Press Ctrl+C to quit.

GET /pony HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:8000
User-Agent: HTTPie/0.9.2
```

Astute readers will point out that HTTPie can show request output with `-v`,
but HTTPony will output for any client that talks HTTP.
Many libraries do not quickly show their request output.

To get started:

```bash
$ pip install httpony
```

This project is heavily indebted to [HTTPie][pie].
Thanks for making a great alternative to cURL.

[pie]: http://httpie.org/
