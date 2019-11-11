# phrases_case

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
