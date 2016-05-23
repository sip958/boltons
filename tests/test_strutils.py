# -*- coding: utf-8 -*-

import uuid

from boltons import strutils


def test_asciify():
    ref = u'Beyoncé'
    b = strutils.asciify(ref)
    assert len(b) == len(b)
    assert b[-1:].decode('ascii') == 'e'


def test_indent():
    to_indent = '\nabc\ndef\n\nxyz\n'
    ref = '\n  abc\n  def\n\n  xyz\n'
    assert strutils.indent(to_indent, '  ') == ref


def test_is_uuid():
    assert strutils.is_uuid(uuid.uuid4()) == True
    assert strutils.is_uuid(uuid.uuid4(), version=1) == False
    assert strutils.is_uuid(str(uuid.uuid4())) == True
    assert strutils.is_uuid(str(uuid.uuid4()), version=1) == False
    assert strutils.is_uuid(set('garbage')) == False


def test_range2list():
    assert strutils.range2list("1,3,5-8,10-11,15") == [1, 3, 5, 6, 7, 8, 10, 11, 15]

    assert strutils.range2list("1,3,5-8,10-11,15,") == [1, 3, 5, 6, 7, 8, 10, 11, 15]
    assert strutils.range2list(",1,3,5-8,10-11,15") == [1, 3, 5, 6, 7, 8, 10, 11, 15]
    assert strutils.range2list(" 1, 3 ,5-8,10-11,15 ") == [1, 3, 5, 6, 7, 8, 10, 11, 15]
    assert strutils.range2list("3,1,5-8,10-11,15") == [1, 3, 5, 6, 7, 8, 10, 11, 15]

    assert strutils.range2list("5-8") == [5, 6, 7, 8]
    assert strutils.range2list("8-5") == [5, 6, 7, 8]

def test_list2range():
    assert strutils.list2range([1, 3, 5, 6, 7, 8, 10, 11, 15]) == '1,3,5-8,10-11,15'
    assert strutils.list2range([5, 6, 7, 8]) == '5-8'

    assert strutils.list2range([1, 3, 5, 6, 7, 8, 10, 11, 15], delim_space=True) == '1, 3, 5-8, 10-11, 15'
    assert strutils.list2range([5, 6, 7, 8], delim_space=True) == '5-8'
