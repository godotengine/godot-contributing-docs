# ReadTheDocs redirect tools

The scripts located in this directory help in creating and maintaining redirects on [Read the Docs](https://readthedocs.io).
Also refer to Read the Docs [API documentation](https://docs.readthedocs.io/en/stable/api/index.html).

Note that RTD redirects only apply in case of 404 errors, and to all branches and languages:
<https://docs.readthedocs.io/en/stable/user-defined-redirects.html>.
If this ever changes, we need to rework how we manage these (likely adding per-branch logic).

`convert_git_renames_to_csv.py` creates a list of renamed files in Git to create redirects for.
`create_redirects.py` is used to actually manage redirects on ReadTheDocs.

These tools should be kept in sync with [godot-docs](https://github.com/godotengine/godot-docs/tree/master/_tools/redirects).
