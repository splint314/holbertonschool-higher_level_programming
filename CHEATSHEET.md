# 🧠 Cheat Sheet

Every concept touched by this repo, explained in plain English with a real-world analogy — grouped by the subdirectory it comes from.

## 🗄️ Databases & ORM (`python-object_relational_mapping/`)

- **Raw SQL (MySQLdb)** — issuing SQL statements directly through a database driver's cursor. Like ordering food in the kitchen's native language instead of through a waiter: more control, but one typo and the chef has no idea what you meant.
- **SQL injection & parameterized queries** — concatenating user input straight into a SQL string lets an attacker smuggle in their own commands; using placeholders (`%s`) lets the driver escape the input safely instead. Like filling in blanks on a pre-printed mail form (safe) versus letting a stranger scribble anything they want onto the envelope address (dangerous).
- **ORM (SQLAlchemy)** — mapping Python classes to database tables so you query with objects and attributes instead of hand-written SQL. Like hiring a translator at a foreign business meeting: you speak Python, they speak SQL to the database on your behalf.
- **Declarative Base & models** — a base class (`Base = declarative_base()`) that every table-mapped class inherits from, so SQLAlchemy knows which Python classes describe which tables. Like a company org chart template: every department (table) is drawn with the same shape and rules so the whole org (database) stays legible.
- **Foreign keys & relationships** — a column in one table (`City.state_id`) pointing to the primary key of another (`State.id`), linking related rows together. Like a library card-catalog entry that references a shelf number: the card doesn't contain the whole shelf, just a pointer to where it lives.
- **`create_engine` & connection strings** — a single string (`mysql+mysqldb://user:pass@host/db`) describing how and where to connect, wrapped into a reusable engine object. Like a hotel's switchboard number: dial once, and it knows how to route you to the right room every time.
- **Session (unit of work)** — a workspace that tracks pending changes before committing them to the database. Like a shopping cart: you add and remove items freely, and nothing is charged until checkout (`commit()`).
- **Query filtering (`.filter()`, `.like()`)** — chaining conditions onto a base query object instead of writing a `WHERE` clause by hand. Like narrowing a search on a shopping site by clicking filters one at a time, each one refining the same result set.
- **JOIN queries** — combining rows from two tables on a matching column, whether written as raw SQL or as a multi-model ORM query. Like stapling a customer's shipping-address form to their order form because they share the same customer ID.

## 📦 Serialization (`python-serialization/`)

- **Serialization / deserialization (JSON)** — converting an in-memory object into a storable or transmittable format, then converting it back. Like vacuum-sealing a meal for shipping, then unwrapping and reheating it on arrival.
- **Pickle** — Python's own binary format for saving almost any Python object, including custom class instances, but only Python can reliably read it back. Like writing a diary in personal shorthand: fast to write, useless to anyone without your notebook.
- **CSV parsing (`csv.DictReader` / `DictWriter`)** — reading or writing tabular text as rows of key-value pairs instead of raw strings split by commas. Like a spreadsheet where every row already remembers its own column headers, so you never count columns by hand.
- **XML serialization (`ElementTree`)** — representing structured data as nested tagged elements (`<data><name>...</name></data>`) instead of flat key-value pairs. Like a shipping label with boxes nested inside boxes, each one labeled with what's inside, rather than one flat packing list.

## 🌐 REST APIs & Security (`restful-api/`)

- **REST API** — a set of URL endpoints that respond to HTTP verbs with structured data. Like a restaurant menu: fixed items (endpoints) you order (request) and receive a plate (response) for.
- **HTTP methods (GET / POST)** — GET asks for existing data without changing anything; POST sends new data to be created or processed. Like reading a notice board (GET) versus pinning a new notice to it (POST).
- **HTTP status codes** — a numeric shorthand for what happened to a request. Traffic lights for computers: 200 means go, 404 means the road doesn't exist, 401 means you weren't let past the gate, 403 means you were recognized but still refused entry.
- **`requests` (API client)** — a Python library for making outbound HTTP calls and reading the response. Like placing a phone order with another business and writing down what they tell you back.
- **`http.server` (hand-rolled server)** — building a web server from the standard library by handling each HTTP verb yourself (`do_GET`) and writing the response by hand. Like running a lemonade stand solo: you personally greet every customer and prepare exactly what goes back to them, no framework staff to help.
- **Flask** — a micro web framework that maps URL routes to Python functions and handles the HTTP plumbing for you. Like hiring a receptionist who reads each visitor's request and routes it to the right department automatically.
- **Basic Auth vs JWT** — Basic Auth checks a username/password on every single request; JWT issues a signed token once that proves identity afterward. Basic Auth is showing your ID at every door; a JWT is a wristband from the entrance that gets you into every room afterward without re-checking ID.
- **Password hashing (`werkzeug.security`)** — storing a one-way scrambled version of a password instead of the password itself, then comparing hashes on login. Like a shredded document: you can confirm two copies were identical by comparing the confetti, but you can't reconstruct the original page from it.
- **Role-based access control** — checking not just who a user is, but what they're allowed to do (`role == "admin"`) before granting access. Like a concert wristband that gets everyone into the venue, but only the VIP color gets you backstage.

## 🖥️ JavaScript Fundamentals (`javascript-warm_up/`)

- **`process.argv` (CLI arguments)** — the array Node.js fills with whatever was typed after the script name on the command line. Like the order slip a customer hands over at checkout: everything after the item name is an instruction for how to prepare it.
- **Functions & recursion** — a function that calls itself on a smaller version of the problem until it reaches a base case. Like Russian nesting dolls: you keep opening the doll inside the doll until you hit the smallest one, then work your way back out.
- **Array methods (`map`, `sort`)** — transforming every element of an array into a new one, or reordering them, without writing a manual loop. Like an assembly line: every item passes through the same stamping machine (`map`), then gets sorted onto the right shelf by size (`sort`).
- **Objects (mutable key-value pairs)** — a JavaScript object holds named properties that can be read and reassigned after creation. Like a whiteboard covered in nametags: you can walk up and erase and rewrite any single label without redoing the whole board.
- **`module.exports` / `exports`** — marking specific functions or values as the public interface of a file so other files can `require()` them. Like a shop's storefront window: only what's put on display is visible to customers walking by, the back room stays private.
- **Loops (`for`, `for...in`)** — repeating a block of code once per item in a collection, or a fixed number of times. Like a mail carrier walking down a street, dropping something into every mailbox in order.
- **`parseInt` / `isNaN` & type coercion** — converting a string from the command line into a number, and checking whether that conversion actually produced a valid number. Like a bouncer checking IDs at a door: `parseInt` tries to read the ID, `isNaN` flags the ones that are obviously fake.

## 🌍 DOM Manipulation (`javascript-dom_manipulation/`)

- **DOM selection (`querySelector`)** — finding a specific element on a live web page using a CSS-style selector. Like calling out a seat number in a theater to pick one specific person out of the crowd.
- **Event listeners (`addEventListener`)** — attaching a function that runs automatically when something happens (a click, etc.) instead of calling it directly. Like a doorbell: nothing happens until someone presses it, then the chime fires on its own.
- **`classList` (add / toggle)** — adding, removing, or flipping CSS classes on an element to change its appearance without touching its other attributes. Like a light switch on a wall: flipping it doesn't rewire the house, it just changes one state on an existing fixture.
- **`createElement` / `appendChild`** — building a new DOM node in memory, then attaching it into the visible page tree. Like assembling a piece of furniture in the garage, then carrying it inside and placing it in the room.
- **`fetch` & Promises** — making an asynchronous network request and reacting once the response eventually arrives, without freezing the page while waiting. Like ordering food at a counter and getting a buzzer: you sit back down and keep chatting, and get notified only when the order is actually ready.

---

⬅ back to [README.md](README.md)
