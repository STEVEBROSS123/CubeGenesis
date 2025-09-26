import ast
import hashlib
from typing import Dict

class SymbolTable:
    """Cache code blocks and assign symbols based on content."""

    def __init__(self) -> None:
        self._name_to_symbol: Dict[str, str] = {}
        self._symbol_to_code: Dict[str, str] = {}

    def _normalize(self, code: str) -> str:
        """Return a normalized representation of code using its AST."""
        tree = ast.parse(code)
        return ast.dump(tree, annotate_fields=True, include_attributes=False)

    def _hash(self, normalized: str) -> str:
        """Compute a SHA256 hash of normalized code."""
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    def register(self, name: str, code: str) -> str:
        """Store a code block under a name and return its symbol."""
        normalized = self._normalize(code)
        symbol = self._hash(normalized)
        self._name_to_symbol[name] = symbol
        self._symbol_to_code.setdefault(symbol, code)
        return symbol

    def get_symbol(self, name: str) -> str:
        """Retrieve the symbol for a registered name."""
        return self._name_to_symbol[name]

    def get_code(self, symbol: str) -> str:
        """Retrieve the original code for a symbol."""
        return self._symbol_to_code[symbol]
