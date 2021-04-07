# Git Resource Fork Hooks

Helper scripts to allow Git to understand files with resource forks, as commonly used in classic Mac OS development. The scripts rely on the `Rez` and `DeRez` tools that still (as of 2021) ship with Xcode, which turn can convert resource forks to a textual (`.r`) format. Besides allowing cross-platform transport of resource forks, `.r` files diff nicely, especially if using resource definitions to generate more structured output ([example](https://github.com/mihaip/git-resource-fork-hooks/commit/47256b609872500200f4957cc3658b967071d36b)).

## Installation

To install, copy the hooks into the .git/hooks directory of your repository:

```
cp hooks/derez-resource-forks.py .git/hooks/pre-commit
cp hooks/rez-resource-forks.py .git/hooks/post-checkout
cp hooks/rez-resource-forks.py .git/hooks/post-merge
```

## Dependencies

- Xcode (tested with Xcode 12.4 on Catalina, but the Rez and DeRez tools have not changed in years and thus should work with almost any version)
- Python 2 (used since it ships with macOS and thus removes a need for a separate install)

## Notes

After doing the initial checkout of a repo with such files, you may need to manually run the `.git/hooks/post-checkout` script manually (because the hooks were not yet set).

## Local Development

For local development (e.g. for testing out things with the `examples` directory):
```
ln -sf ../../hooks/derez-resource-forks.py .git/hooks/pre-commit
ln -sf ../../hooks/rez-resource-forks.py .git/hooks/post-checkout
ln -sf ../../hooks/rez-resource-forks.py .git/hooks/post-merge
```
