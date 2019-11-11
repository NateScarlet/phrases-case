# phrases case

[![build status](https://github.com/NateScarlet/phrases-case/workflows/Python%20package/badge.svg)](https://github.com/NateScarlet/phrases-case/actions)
[![version](https://img.shields.io/pypi/v/phrases-case)](https://pypi.org/project/phrases-case/)
![python version](https://img.shields.io/pypi/pyversions/phrases-case)
![wheel](https://img.shields.io/pypi/wheel/phrases-case)

Convert phrases between different cases.

Not using `re` module.

```python
>>> import phrases_case
>>> phrases_case.snake('camelCase')
'camel_case'
>>> phrases_case.snake('camelCase', separator='-')
'camel-case'
>>> phrases_case.hyphen('camelCase')
'camel-case'
>>> phrases_case.space('camelCase')
'camel case'
>>> phrases_case.camel('snake_case')
'snakeCase'
>>> phrases_case.pascal('snake_case')
'SnakeCase'
```
