# javascript-dom_manipulation

Vanilla JavaScript for manipulating a live web page: selecting elements, listening for clicks, toggling CSS classes, creating new elements, and fetching data from an API to render it into the DOM. Each script targets a small HTML page (not included here) and builds up from a one-line style change to asynchronous `fetch` calls against the SWAPI and a translation API.

## Notable files

| File | Description |
|---|---|
| `0-script.js` | Selects an element and changes its style directly |
| `1-script.js`, `2-script.js` | Click listeners that add a CSS class via `classList.add` |
| `3-script.js` | Click listener that toggles between two CSS classes |
| `4-script.js` | Creates a new `<li>` element and appends it to a list |
| `5-scripts.js` | Updates an element's `textContent` on click |
| `6-script.js` | `fetch`es a Star Wars character by ID and displays its name |
| `7-script.js` | `fetch`es a list of films and renders them as list items |
| `8-script.js` | `fetch`es a translated greeting and displays it |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.
