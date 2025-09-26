import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from symbol_table import SymbolTable


def test_same_code_same_symbol():
    table = SymbolTable()
    code = "def add(a, b):\n    return a + b"
    sym1 = table.register("first", code)
    sym2 = table.register("second", code)
    assert sym1 == sym2


def test_different_code_different_symbol():
    table = SymbolTable()
    code1 = "def add(a, b):\n    return a + b"
    code2 = "def add(a, b):\n    return a - b"
    sym1 = table.register("add", code1)
    sym2 = table.register("sub", code2)
    assert sym1 != sym2


def test_retrieve_code():
    table = SymbolTable()
    code = "def square(x):\n    return x * x"
    symbol = table.register("square", code)
    assert table.get_code(symbol) == code
