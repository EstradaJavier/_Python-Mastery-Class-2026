# PyScript Local Setup Notes

These notes document the workflow used to get the `basic_pyscript.html` and `advanced_pyscript.html` files working correctly in a local development setup.

## What worked

The HTML pages loaded correctly after the following sequence was used:

1. Open the project folder in IntelliJ.
2. Save the HTML files in the project.
3. Start a local Python web server from the project directory:
   ```bash
   python3 -m http.server
   ```
4. Wait a few moments for the page and PyScript resources to load in the browser.
5. Open the local page in the browser.
6. Run or refresh after saving changes in IntelliJ.
7. Confirm that the PyScript sections render correctly in the browser.

## Why this worked

PyScript works more reliably when the HTML files are served over HTTP instead of being opened directly as raw local files in the browser. The local server created by `python3 -m http.server` provided the environment needed for the PyScript resources to load properly.[cite:31]

The pages were also corrected to use JavaScript DOM access through `from js import document` rather than `from pyscript.web import page`, which avoids the `ModuleNotFoundError` seen earlier and follows the documented DOM interaction approach for PyScript.[cite:114][cite:123]

## Helpful local URLs

After starting the local server, pages can be tested with URLs like:

- `http://localhost:8000/basic_pyscript.html`
- `http://localhost:8000/advanced_pyscript.html`

## Suggested file name

A good file name for the `docs` directory is:

`pyscript-local-setup-notes.md`

## Optional Git workflow after testing

Once the pages are confirmed working locally, they can be pushed to GitHub with:

```bash
git add basic_pyscript.html advanced_pyscript.html docs/pyscript-local-setup-notes.md
git commit -m "Add working PyScript pages and setup notes"
git push origin main
```
