from fastmcp import FastMCP
import math
mcp = FastMCP("simple calculator server")

@mcp.tool
async def add(a: int, b: int) -> int:
    """
    Add two numbers together.

    Args:
        a (int): The first number to add.
        b (int): The second number to add.

    Returns:
        int: The sum of a and b.

    """
    return a + b

@mcp.tool
async def subtract(a: int, b: int) -> int:
    """
    Subtract one number from another.

    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.

    Returns:
        int: The difference of a and b.

    """
    return a - b

@mcp.tool
async def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers together.

    Args:
        a (int): The first number to multiply.
        b (int): The second number to multiply.

    Returns:
        int: The product of a and b.

    """
    return a * b

@mcp.tool
async def divide(a: int, b: int) -> int:
    """
    Divide one number by another.

    Args:
        a (int): The number to divide.
        b (int): The number to divide by.

    Returns:
        int: The quotient of a and b.

    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b

@mcp.tool
async def power(base: float, exponent: float) -> float:
    """Raise a base number to an exponent."""
    return math.pow(base, exponent)

@mcp.tool
async def square_root(x: float) -> float:
    """Calculate the square root of a positive number."""
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(x)

@mcp.tool
async def modulo(a: float, b: float) -> float:
    """Calculate the remainder of division (a % b)."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b


if __name__ == '__main__':
    mcp.run(transport='http', host='0.0.0.0', port=8000)


