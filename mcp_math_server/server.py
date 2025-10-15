#!/usr/bin/env python3
"""
MCP Math Server - A modern MCP server providing comprehensive math functions.

This server demonstrates FastMCP functionality by exposing various mathematical
operations as tools with automatic schema generation and validation.
Organized into categories: basic arithmetic, advanced operations, and number theory.
"""

import math
from typing import Annotated
from datetime import datetime

import click
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

# Initialize FastMCP server
mcp = FastMCP("mcp-math-server")

# Server start time for health check
_server_start_time = datetime.now()


# =============================================================================
# HEALTH CHECK ENDPOINT
# =============================================================================


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    """Health check endpoint.
    
    Returns server status, uptime, and version information.
    """
    uptime = datetime.now() - _server_start_time
    uptime_seconds = int(uptime.total_seconds())
    uptime_str = str(uptime).split('.')[0]  # Remove microseconds
    
    return JSONResponse({
        "status": "healthy",
        "server": "mcp-math-server",
        "uptime": uptime_str,
        "uptime_seconds": uptime_seconds,
        "timestamp": datetime.now().isoformat()
    })


# =============================================================================
# BASIC ARITHMETIC OPERATIONS
# =============================================================================


@mcp.tool()
def add(
    a: Annotated[float, "First number"],
    b: Annotated[float, "Second number"],
) -> str:
    """Add two numbers together.
    
    Returns the sum of a and b.
    """
    result = a + b
    return f"Result: {result}"


@mcp.tool()
def subtract(
    a: Annotated[float, "First number"],
    b: Annotated[float, "Second number"],
) -> str:
    """Subtract the second number from the first number.
    
    Returns the difference (a - b).
    """
    result = a - b
    return f"Result: {result}"


@mcp.tool()
def multiply(
    a: Annotated[float, "First number"],
    b: Annotated[float, "Second number"],
) -> str:
    """Multiply two numbers together.
    
    Returns the product of a and b.
    """
    result = a * b
    return f"Result: {result}"


@mcp.tool()
def divide(
    a: Annotated[float, "Numerator"],
    b: Annotated[float, "Denominator"],
) -> str:
    """Divide the first number by the second number.
    
    Returns the quotient (a / b). Raises an error for division by zero.
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    result = a / b
    return f"Result: {result}"


# =============================================================================
# ADVANCED MATHEMATICAL OPERATIONS
# =============================================================================


@mcp.tool()
def power(
    base: Annotated[float, "Base number"],
    exponent: Annotated[float, "Exponent"],
) -> str:
    """Raise a number to the power of another number.
    
    Returns base raised to the power of exponent (base^exponent).
    """
    result = base ** exponent
    return f"Result: {result}"


@mcp.tool()
def sqrt(
    x: Annotated[float, "Number to find square root of (must be non-negative)"],
) -> str:
    """Calculate the square root of a number.
    
    Returns the square root of x. The input must be non-negative.
    """
    if x < 0:
        return "Error: Cannot calculate square root of negative number"
    result = math.sqrt(x)
    return f"Result: {result}"


@mcp.tool()
def logarithm(
    x: Annotated[float, "Number to find logarithm of (must be positive)"],
    base: Annotated[float, "Base of the logarithm (default: e for natural log)"] = math.e,
) -> str:
    """Calculate the logarithm of a number with a specified base.
    
    Returns log_base(x). Defaults to natural logarithm if base not specified.
    """
    if x <= 0:
        return "Error: Logarithm requires a positive number"
    if base <= 0 or base == 1:
        return "Error: Logarithm base must be positive and not equal to 1"
    result = math.log(x, base)
    return f"Result: {result}"


@mcp.tool()
def absolute(
    x: Annotated[float, "Number to find absolute value of"],
) -> str:
    """Calculate the absolute value of a number.
    
    Returns |x|, the non-negative value of x without regard to its sign.
    """
    result = abs(x)
    return f"Result: {result}"


@mcp.tool()
def modulo(
    a: Annotated[float, "Dividend"],
    b: Annotated[float, "Divisor"],
) -> str:
    """Calculate the remainder of division.
    
    Returns the remainder when a is divided by b (a mod b).
    """
    if b == 0:
        return "Error: Modulo by zero is not allowed"
    result = a % b
    return f"Result: {result}"


# =============================================================================
# NUMBER THEORY OPERATIONS
# =============================================================================


@mcp.tool()
def factorial(
    n: Annotated[int, "Non-negative integer to calculate factorial of"],
) -> str:
    """Calculate the factorial of a non-negative integer.
    
    Returns n! = n × (n-1) × (n-2) × ... × 2 × 1.
    """
    if n < 0:
        return "Error: Factorial is only defined for non-negative integers"
    result = math.factorial(n)
    return f"Result: {result}"


@mcp.tool()
def gcd(
    a: Annotated[int, "First integer"],
    b: Annotated[int, "Second integer"],
) -> str:
    """Calculate the greatest common divisor of two integers.
    
    Returns the largest positive integer that divides both a and b.
    """
    result = math.gcd(a, b)
    return f"Result: {result}"


@mcp.tool()
def lcm(
    a: Annotated[int, "First integer"],
    b: Annotated[int, "Second integer"],
) -> str:
    """Calculate the least common multiple of two integers.
    
    Returns the smallest positive integer that is divisible by both a and b.
    """
    result = math.lcm(a, b)
    return f"Result: {result}"


@mcp.tool()
def is_prime(
    n: Annotated[int, "Integer to check for primality (must be >= 2)"],
) -> str:
    """Check if a number is prime.
    
    Returns whether n is a prime number (only divisible by 1 and itself).
    """
    if n < 2:
        return f"Error: {n} is less than 2. Primality is only defined for integers >= 2"
    
    # Check for primality using trial division
    if n == 2:
        return f"{n} is prime"
    if n % 2 == 0:
        return f"{n} is not prime"
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return f"{n} is not prime (divisible by {i})"
    
    return f"{n} is prime"


@mcp.tool()
def is_even(
    n: Annotated[int, "Integer to check"],
) -> str:
    """Check if a number is even.
    
    Returns whether n is divisible by 2.
    """
    return f"{n} is {'even' if n % 2 == 0 else 'odd'}"


# =============================================================================
# ENTRY POINT
# =============================================================================


@click.command()
@click.option(
    "--host",
    default="0.0.0.0",
    help="Host to bind the server to (default: 0.0.0.0)",
    show_default=True,
)
@click.option(
    "--port",
    default=5000,
    type=int,
    help="Port to run the server on (default: 5000)",
    show_default=True,
)
def main(host: str, port: int) -> None:
    """Run the MCP Math Server.
    
    A modern MCP server providing comprehensive math functions including
    basic arithmetic, advanced operations, and number theory tools.
    """
    click.echo(f"Starting MCP Math Server on {host}:{port}")
    mcp.run(port=port, host=host, transport="streamable-http")


if __name__ == "__main__":
    main()

