# CubeGenesis
The cube that explodes into intelligent life.

## Symbol Table
This project now includes a simple way to remember chunks of code. Instead of reading the same code over and over, we turn each piece into a short symbol. Later, we can work with the symbol and look up the full code only when needed.

### Example
```python
from symbol_table import SymbolTable

table = SymbolTable()
code = """def greet(name):
    return f'Hello, {name}'
"""
symbol = table.register("greet", code)
print(symbol)            # short label for the code
print(table.get_code(symbol))  # original code
```
