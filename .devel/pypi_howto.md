Versions:

1.0.9.9001  # development release
1.1.0       # major release


# source distribution + platform-less wheels:

```
rm -f dist/*
python3 setup.py sdist
pip wheel -w dist . --no-deps
```

# upload to pypi:

```
twine upload dist/*
```
