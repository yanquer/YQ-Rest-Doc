# coding: utf-8
import os

import yaml


def load_yaml(name):
    with open(name, 'r') as f:
        return yaml.full_load(f)


def write_toc_tree(name, data):
    with open(name, 'w') as f:
        f.write(data)


def scan_docs_dir(name):
    if not os.path.isdir(name):
        return
    return os.listdir(name)
