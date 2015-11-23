# Fishbowl

> Simple time tracking

```sh
$ python -u fishbowl/fishbowl.py | \
    xargs -n1 -I {} \
    curl -d "{}" http://fishbowl-host.local/save
```

