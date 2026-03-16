from __future__ import annotations
import ast
import operator as op
from dataclasses import dataclass

_ALLOWED_BINOPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
}

_ALLOWED_UNARYOPS = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}

def _safe_eval(expr: str) -> float:
    """
    Safely evaluate a math expression containing numbers, + - * / and parentheses.
    Raises ValueError / ZeroDivisionError for invalid input.
    """
    if not expr or expr.strip() == "":
        raise ValueError("Empty expression")

    try:
        node = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise ValueError("Malformed expression") from e

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return float(n.value)
        # Python <3.8 compatibility not needed, but keep robust
        if hasattr(ast, "Num") and isinstance(n, ast.Num):  # pragma: no cover
            return float(n.n)

        if isinstance(n, ast.BinOp) and type(n.op) in _ALLOWED_BINOPS:
            left = _eval(n.left)
            right = _eval(n.right)
            return _ALLOWED_BINOPS[type(n.op)](left, right)

        if isinstance(n, ast.UnaryOp) and type(n.op) in _ALLOWED_UNARYOPS:
            return _ALLOWED_UNARYOPS[type(n.op)](_eval(n.operand))

        if isinstance(n, ast.ParenExpr):  # Python 3.12+ internal, just in case
            return _eval(n.expression)

        raise ValueError("Unsupported expression")

    return _eval(node)

@dataclass
class Calculator:
    """
    Model: core calculator logic.
    """
    expression: str = ""

    def add_to_expression(self, char: str) -> None:
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("char must be a single character")
        self.expression += char

    def remove_last_character(self) -> None:
        self.expression = self.expression[:-1]

    def clear_expression(self) -> None:
        self.expression = ""

    def calculate(self):
        """
        Returns:
          - numeric result (int or float) if valid
          - string error message if invalid
        """
        try:
            result = _safe_eval(self.expression)
            # Format: if close to int, show int
            if abs(result - round(result)) < 1e-12:
                return int(round(result))
            return result
        except ZeroDivisionError:
            return "Error: division by zero"
        except Exception:
            return "Error: invalid expression"

    def get_expression(self) -> str:
        return self.expression
