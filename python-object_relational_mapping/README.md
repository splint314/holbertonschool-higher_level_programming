# python-object_relational_mapping

Talking to a MySQL database two ways: first with raw SQL through `MySQLdb`, then through the SQLAlchemy ORM. The early scripts connect with a cursor and run hand-written `SELECT` queries (including a side-by-side of an unsafe string-formatted query vs. a parameterized, injection-safe one). The later scripts define `State` and `City` as SQLAlchemy model classes (`model_state.py`, `model_city.py`, linked by a foreign key) and perform the same fetch/filter/insert/update/delete operations as Python method calls through a `Session`.

## Notable files

| File | Description |
|---|---|
| `model_state.py` | `State` SQLAlchemy model (declarative base, `id`, `name`) |
| `model_city.py` | `City` SQLAlchemy model, linked to `State` via `state_id` foreign key |
| `0-select_states.py` → `5-filter_cities.py` | Raw `MySQLdb` queries: select all, filter by prefix, filter by exact name, safe vs. unsafe filtering, city↔state JOINs |
| `7-model_state_fetch_all.py` → `9-model_state_filter_a.py` | ORM reads: fetch all, fetch first, filter with `.like()` |
| `10-model_state_my_get.py` | ORM lookup by name |
| `11-model_state_insert.py` | ORM insert (`session.add` + `commit`) |
| `12-model_state_update_id_2.py` | ORM update of an existing row |
| `13-model_state_delete_a.py` | ORM delete of matching rows |
| `14-model_city_fetch_by_state.py` | ORM JOIN across `City` and `State` |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
