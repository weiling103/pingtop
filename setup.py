# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="pingtop",
    version="0.2.0",
    py_modules=['ping'],
    description="Top like ping tool.",
    author="laixintao",
    author_email="laixintaoo@gmail.com",
    url="https://github.com/laixintao/pingtop",
    entry_points={"console_scripts": ["pingtop = pingtop:multi_ping"]},
    scripts=["pingtop.py"],
    install_requires=["panwid", "click"],
)
