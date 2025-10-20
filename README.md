# MCP Math Server

A toy MCP (Model Context Protocol) server written in Python that provides mathematical functions. Built with **FastMCP** for modern, type-safe tool development.

**All tool descriptions and input schemas are automatically generated from Python docstrings and type annotations** - no manual schema writing required!

### Key Features

- **Automatic Schema Generation**: Tool input schemas are automatically generated from Python `Annotated` type hints - define your parameters once with Python types, get JSON Schema for free
- **Documentation from Docstrings**: Tool descriptions come from function docstrings, and parameter descriptions are extracted from `Annotated` type hint strings
- **Type Safety**: Full type hints and validation for all operations
- **Clean Architecture**: Simple, straightforward function definitions with no boilerplate
- **Automatic Validation**: FastMCP handles type checking and parameter validation automatically

### How It Works

FastMCP automatically converts your Python code into MCP tool definitions:

```python
from typing import Annotated

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
```

This becomes an MCP tool with:
- **Tool name**: `add`
- **Tool description**: "Add two numbers together. Returns the sum of a and b." (from docstring)
- **Input schema**: JSON Schema with `a` and `b` as number fields with descriptions (from `Annotated` type hints)
- **Validation**: Automatic type checking and validation

### Project Structure

```
mcp_server_test/
├── mcp_math_server/
│   ├── __init__.py
│   └── server.py
├── pyproject.toml
└── README.md
```