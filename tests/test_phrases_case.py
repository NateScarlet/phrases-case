# -*- coding=UTF-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import doctest
import sys

import pytest

import phrases_case


@pytest.mark.skipif(sys.version_info < (3,), reason="requires python3")
def test_doc():
    doctest.testmod(phrases_case)


@pytest.mark.parametrize(
    'v,expected', [
        ('space case', 'space_case'),
        ('snake_case', 'snake_case'),
        ('hyphen-case', 'hyphen_case'),
        ('camelCase', 'camel_case'),
        ('PascalCase', 'pascal_case'),
    ]
)
def test_snake(v, expected):
    assert phrases_case.snake(v) == expected


@pytest.mark.parametrize(
    'v,expected', [
        ('space case', 'SpaceCase'),
        ('snake_case', 'SnakeCase'),
        ('hyphen-case', 'HyphenCase'),
        ('camelCase', 'CamelCase'),
        ('PascalCase', 'PascalCase'),
    ]
)
def test_pascal(v, expected):
    assert phrases_case.pascal(v) == expected


@pytest.mark.parametrize(
    'v,expected', [
        ('space case', 'spaceCase'),
        ('snake_case', 'snakeCase'),
        ('hyphen-case', 'hyphenCase'),
        ('camelCase', 'camelCase'),
        ('PascalCase', 'pascalCase'),
    ]
)
def test_camel(v, expected):
    assert phrases_case.camel(v) == expected


@pytest.mark.parametrize(
    'v,expected', [
        ('space case', 'space case'),
        ('snake_case', 'snake case'),
        ('hyphen-case', 'hyphen case'),
        ('camelCase', 'camel case'),
        ('PascalCase', 'pascal case'),
    ]
)
def test_space(v, expected):
    assert phrases_case.space(v) == expected


@pytest.mark.parametrize(
    'v,expected', [
        ('space case', 'space-case'),
        ('snake_case', 'snake-case'),
        ('hyphen-case', 'hyphen-case'),
        ('camelCase', 'camel-case'),
        ('PascalCase', 'pascal-case'),
    ]
)
def test_hyphen(v, expected):
    assert phrases_case.hyphen(v) == expected
