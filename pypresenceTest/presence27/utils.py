"""Util functions that are needed but messy."""
import json
import time


# Made by https://github.com/LewdNeko ;^)
def remove_none(d):
    for item in d.copy():
        if isinstance(d[item], dict):
            if len(d[item]):
                d[item] = remove_none(d[item])
            else:
                del d[item]
        elif d[item] is None:
            del d[item]
    return d
