# MCP Math Server

A toy MCP (Model Context Protocol) server written in Python that provides mathematical functions. Built with **FastMCP** for modern, type-safe tool development.

<!-- mcp-name: io.github.oodapow/mcp-math-server -->

## Features

This server provides the following math operations as MCP tools:

- **add** - Add two numbers
- **subtract** - Subtract two numbers
- **multiply** - Multiply two numbers
- **divide** - Divide two numbers
- **power** - Raise a number to a power
- **sqrt** - Calculate square root
- **factorial** - Calculate factorial of a non-negative integer
- **gcd** - Find greatest common divisor
- **lcm** - Find least common multiple
- **is_prime** - Check if a number is prime

## Installation

### Using pip

```bash
pip install -e .
```

### Development Installation

```bash
pip install -e ".[dev]"
```

## Usage

### Running the Server

```bash
mcp-math-server
```

Or run directly with Python:

```bash
python -m mcp_math_server.server
```

### Using with MCP Clients

Configure your MCP client to use this server. Example configuration:

```json
{
  "mcpServers": {
    "math": {
      "command": "mcp-math-server"
    }
  }
}
```

## Example

Once connected, you can use the math tools:

- Add numbers: `add(a=5, b=3)` → Result: 8
- Check prime: `is_prime(n=17)` → 17 is prime
- Calculate factorial: `factorial(n=5)` → Result: 120

## Development

This is a simple toy server for testing and demonstration purposes.

### Key Features

- **Pydantic Models**: Each tool uses Pydantic models for input validation and automatic JSON schema generation
- **Type Safety**: Full type hints and validation for all operations
- **Clean Architecture**: Separation of concerns with dedicated input models
- **Automatic Validation**: Pydantic handles parameter validation (e.g., `n >= 0` for factorial, `x >= 0` for sqrt)

### Project Structure

```
mcp_server_test/
├── mcp_math_server/
│   ├── __init__.py
│   └── server.py
├── pyproject.toml
└── README.md
```

## License

MIT
