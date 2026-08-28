# python-serialization

Converting Python objects to and from storable formats: JSON, Pickle, CSV, and XML. Each task is a standalone module covering one format — basic JSON dump/load, a custom class serialized with `pickle`, a CSV-to-JSON converter, and a dictionary-to-XML (and back) converter — all wrapped in error handling so a missing file or bad input fails gracefully instead of crashing.

## Notable files

| File | Description |
|---|---|
| `task_00_basic_serialization.py` | Serialize/deserialize a plain dict to/from a JSON file |
| `task_01_pickle.py` | `CustomObject` class that can `serialize()`/`deserialize()` itself with `pickle` |
| `task_02_csv.py` | `convert_csv_to_json()` — reads a CSV with `csv.DictReader`, writes it out as JSON |
| `task_03_xml.py` | `serialize_to_xml()` / `deserialize_from_xml()` — dict ↔ XML with `ElementTree` |
| `main_02.py` | Driver script that runs the CSV → JSON conversion on `data.csv` |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
