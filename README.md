# pre-commit-demo
This is a demo repository for installing a pre-commit hook for executing black for Python code refactoring

Steps:
1. Install `pre-commit` using `pip install pre-commit`
2. create `.pre-commit-config.yaml` in project root and add required repos
3. run `pre-commit install` on root to install the hooks
4. run `pre-commit uninstall` to uninstall hooks
5. run `pre-commit run --all-files` to manually run the hooks

more info on this @https://pre-commit.com/#usage


## Automatically generating docstrings using `pyment`
1. run `pip install pyment` to install pyment
2. run `pyment -o google .` for generating atomic google docstrings. Files are not overwritten (.patch files are created)
3. run `pyment -o google -w .` for overwriting existing `.py` files with atomic google docstrings.

more info on this @https://github.com/dadadel/pyment
possibly you might wanna remove `*.py.patch` files
