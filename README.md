# 🚀 holbertonschool-higher_level_programming

> From SQL and ORMs to REST APIs and the browser DOM — Python and JavaScript exercises for building real applications.

> 🎓 Part of the Software Engineering curriculum at **Holberton School Toulouse**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white)

## 📖 About

This repository covers the "higher level" part of the curriculum: talking to a MySQL database directly and through the SQLAlchemy ORM, serializing data with JSON, Pickle, CSV, and XML, building and securing REST APIs with `http.server` and Flask (including Basic Auth and JWT), and manipulating the DOM and writing everyday scripts in JavaScript. Each folder is a self-contained set of task scripts, mostly Python 3 with a JavaScript wing for the browser and Node exercises.

## 📂 Project Structure

| Directory | Description |
|---|---|
| `python-object_relational_mapping/` | Raw MySQLdb queries, then the same operations via SQLAlchemy models (`State`, `City`) |
| `python-serialization/` | JSON, Pickle, CSV→JSON, and XML serialization/deserialization |
| `restful-api/` | An API client (`requests`), a hand-rolled server (`http.server`), a Flask API, and Flask with Basic Auth + JWT |
| `javascript-warm_up/` | Node.js fundamentals: arguments, loops, objects, arithmetic |
| `javascript-dom_manipulation/` | Vanilla JS DOM selection, event listeners, class toggling, `fetch` |

## 🧠 Cheat Sheet

- **ORM (SQLAlchemy)** — mapping Python classes to database tables so you query with objects instead of raw SQL strings. Like using a translator at a foreign meeting: you speak Python, it speaks SQL to the database for you.
- **Raw SQL (MySQLdb)** — sending SQL statements directly to the database driver. The equivalent of ordering in the restaurant's native language instead of through a translator: more control, more room for typos.
- **Session (SQLAlchemy)** — a workspace that tracks pending changes before committing them to the database. Like a shopping cart: you add and remove items freely, and nothing is charged until checkout (`commit()`).
- **Serialization (JSON/Pickle/XML)** — converting an in-memory object into a format that can be saved or sent elsewhere. Like vacuum-sealing a meal: the food (data) is compacted into a shippable package, then reconstituted later.
- **CSV parsing (`csv.DictReader`)** — reading tabular text as rows of key-value pairs. A spreadsheet where each row already knows its own column headers.
- **REST API** — a set of URL endpoints that respond to HTTP verbs (GET, POST) with structured data. Like a restaurant menu: fixed items (endpoints) you order (request) and receive a plate (response) for.
- **HTTP status codes** — a numeric shorthand for what happened to a request. Traffic lights for computers: 200 means go, 404 means the road doesn't exist, 401 means you weren't let past the gate.
- **Basic Auth vs JWT** — Basic Auth checks a username/password on every request; JWT issues a signed token once that proves identity afterward. Basic Auth is showing your ID at every door, a JWT is a wristband from the entrance that gets you into every room after.
- **DOM manipulation (`querySelector`, `classList`)** — finding and modifying elements of a live web page from JavaScript. Like a stage manager who can walk on set and rearrange props while the show is running.
- **`fetch` / Promises** — making an asynchronous network request and reacting once the response arrives, without freezing the page. Ordering food and continuing your conversation instead of standing frozen at the counter until it's ready.

## 📬 Contact

- 💬 Discord: kevin_rigal
- 📧 Email: kevinrigal.contact@gmail.com
- 🐙 GitHub: [@sharingankid](https://github.com/sharingankid)
