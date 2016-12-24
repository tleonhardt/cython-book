#!/usr/bin/env python
from PyAddFunction import Add

def test_add(capsys):
    assert 3 == Add(1,2)
