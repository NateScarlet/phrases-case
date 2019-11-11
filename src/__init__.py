# -*- coding=UTF-8 -*-
"""Convert phrases between different cases.  """
__version__ = '0.1.0'

ASCII_UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SEPERATORS = '-_ '


def snake(v: str, seperator='_') -> str:
    """Convert phrases case to snake case.

    Args:
        v (str): Phrases to convert.
        seperator (str, optional): phrase seperator. Defaults to '_'.

    Returns:
        str: Converted Phrases.

    >>> snake('space case')
    'space_case'
    >>> snake('snake_case')
    'snake_case'
    >>> snake('hyphen-case')
    'hyphen_case'
    >>> snake('camelCase')
    'camel_case'
    >>> snake('PascalCase')
    'pascal_case'
    """
    ret = ''
    for char in v:
        if char in ASCII_UPPERCASE:
            ret += seperator
            ret += char.lower()
        elif char in SEPERATORS:
            ret += seperator
        else:
            ret += char
    if ret[0] in SEPERATORS:
        ret = ret[1:]
    return ret


def _split(v: str, delimiters=SEPERATORS):
    ret = []
    pos = 0
    for index, i in enumerate(v + delimiters[0]):
        if i in delimiters:
            if index > pos:
                ret.append(v[pos:index])
            pos = index + 1
    return ret


def pascal(v: str) -> str:
    """Convert text to pascal case.

    Args:
        v (str): Phrases to convert.

    Returns:
        str: Converted Phrases.

    >>> pascal('space case')
    'SpaceCase'
    >>> pascal('snake_case')
    'SnakeCase'
    >>> pascal('hyphen-case')
    'HyphenCase'
    >>> pascal('camelCase')
    'CamelCase'
    >>> pascal('PascalCase')
    'PascalCase'
    """
    return ''.join(x[0].title() + x[1:] for x in _split(v))


def camel(v: str) -> str:
    """Convert text to camel case.

    Args:
        v (str): Phrases to convert.

    Returns:
        str: Converted Phrases.

    >>> camel('space case')
    'spaceCase'
    >>> camel('snake_case')
    'snakeCase'
    >>> camel('hyphen-case')
    'hyphenCase'
    >>> camel('camelCase')
    'camelCase'
    >>> camel('PascalCase')
    'pascalCase'
    """

    ret = pascal(v)
    if ret:
        ret = ret[0].lower() + ret[1:]
    return ret


def space(v: str) -> str:
    """Shortcut for snake(v, seperator=' ')

    Args:
        v (str): Phrases to convert.

    Returns:
        str: Converted Phrases.

    >>> space('space case')
    'space case'
    >>> space('snake_case')
    'snake case'
    >>> space('hyphen-case')
    'hyphen case'
    >>> space('camelCase')
    'camel case'
    >>> space('PascalCase')
    'pascal case'
    """
    return snake(v, seperator=' ')


def hyphen(v: str) -> str:
    """Shortcut for snake(v, seperator='-')

    Args:
        v (str): Phrases to convert.

    Returns:
        str: Converted Phrases.

    >>> hyphen('space case')
    'space-case'
    >>> hyphen('snake_case')
    'snake-case'
    >>> hyphen('hyphen-case')
    'hyphen-case'
    >>> hyphen('camelCase')
    'camel-case'
    >>> hyphen('PascalCase')
    'pascal-case'
    """
    return snake(v, seperator='-')
