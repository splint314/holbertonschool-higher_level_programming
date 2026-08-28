# restful-api

Building a REST API from three different angles: consuming one as a client, then building one from scratch with the standard library, then building one with Flask — first open, then secured with Basic Auth and JWT. It progresses from making outbound HTTP requests and saving the results, to handling raw HTTP verbs by hand, to a Flask app with JSON routes, and finally to authentication, password hashing, and role-based access control.

## Notable files

| File | Description |
|---|---|
| `task_02_requests.py` | API client using `requests`: fetch posts from JSONPlaceholder, print titles, save results to `posts.csv` |
| `task_03_http_server.py` | A hand-rolled API using `http.server` / `BaseHTTPRequestHandler`, with `/`, `/data`, `/status`, `/info` routes |
| `task_04_flask.py` | The same kind of API rebuilt with Flask: `/data`, `/status`, `/users/<username>`, `POST /add_user` |
| `task_05_basic_security.py` | Flask API secured with `flask_httpauth` (Basic Auth), `flask_jwt_extended` (JWT login/protected routes), hashed passwords, and an admin-only role check |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
