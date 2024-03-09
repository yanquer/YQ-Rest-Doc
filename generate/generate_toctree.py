# coding: utf-8
import copy
import os.path

from generate.util import load_yaml, scan_docs_dir, write_toc_tree
SPE = '='*20
TEMPLATE = "\n\
.. toctree::\n\
    :maxdepth: 2\n\
    :caption: Contents: {}\n\
    :glob:\n\
    :numbered:\n\
\n\
    docs/{}\
"

HEAD = "\n\
.. Study Document documentation master file, created by\n\
   sphinx-quickstart on Sun Nov 20 17:25:22 2022.\n\
   You can adapt this file completely to your liking, but it should at least\n\
   contain the root `toctree` directive.\n\
\n\
Welcome to Study Document's documentation!\n\
==========================================\n\n\
"

FOOT = "\n\n\
Indices and tables\n\
==================\n\
\n\
* :ref:`genindex`\n\
* :ref:`modindex`\n\
* :ref:`search`\n\n\
"


class DocsToc(object):
    doc_index_rst_path: str
    doc_dir: str
    exclude_dir: list


def create_one(dir_: str):
    _dir_ = os.path.join(DocsToc.doc_dir, dir_)
    _dir_index = os.path.join(_dir_, 'index.rst')
    if os.path.exists(_dir_index):
        _toc_tree_dir: str = os.path.join(dir_, 'index')
        _template: str = copy.copy(TEMPLATE).format(f'{dir_}', _toc_tree_dir)
    else:
        _toc_tree_dir: str = os.path.join(dir_, '*')
        _template: str = copy.copy(TEMPLATE).format(f'{dir_}', _toc_tree_dir)
    return _template


def create_toc_trees(dirs: list):
    rst_toc_text = HEAD + \
                   '\n'.join([create_one(dir_) for dir_ in dirs]) + \
                   FOOT
    write_toc_tree(DocsToc.doc_index_rst_path, rst_toc_text)


def main():
    conf: dict = load_yaml('generate/doc.yaml')
    for attr in DocsToc.__dict__['__annotations__']:
        setattr(DocsToc, attr, conf.get(attr, None))
    toc_dir = set(scan_docs_dir(DocsToc.doc_dir)).difference(set(DocsToc.exclude_dir))
    # print(toc_dir)
    toc_dir = list(toc_dir)
    toc_dir.sort()
    create_toc_trees(toc_dir)
    print("生成toc tree索引完成")

