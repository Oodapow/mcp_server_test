#!/usr/bin/env python3
"""
Test client for MCP Math Server using FastMCP client with HTTP transport.
"""

import asyncio
from fastmcp.client import Client, StreamableHttpTransport


async def test_math_server():
    """Test the MCP Math Server using FastMCP client via HTTP."""
    
    # Configure the server URL
    server_url = "http://localhost:5000/mcp"
    
    print("=" * 50)
    print("MCP Math Server Test Client (HTTP)")
    print("=" * 50)
    print(f"Connecting to: {server_url}")
    print()
    
    # Create transport and client
    transport = StreamableHttpTransport(server_url)
    client = Client(transport)
    
    async with client:
        print("✓ Connected successfully!")
        print()
        
        # List available tools
        print("Listing available tools...")
        tools = await client.list_tools()
        print(f"✓ Found {len(tools)} tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")
        print()
        
        # Test 1: Add two numbers
        print("Test 1: Testing add(5, 3)...")
        result = await client.call_tool("add", arguments={"a": 5, "b": 3})
        print(f"Response: {result.content[0].text}")
        if "8" in result.content[0].text:
            print("✓ Add tool works correctly (5 + 3 = 8)")
        else:
            print("✗ Add tool failed")
        print()
        
        # Test 2: Multiply two numbers
        print("Test 2: Testing multiply(4, 7)...")
        result = await client.call_tool("multiply", arguments={"a": 4, "b": 7})
        print(f"Response: {result.content[0].text}")
        if "28" in result.content[0].text:
            print("✓ Multiply tool works correctly (4 × 7 = 28)")
        else:
            print("✗ Multiply tool failed")
        print()
        
        # Test 3: Square root
        print("Test 3: Testing sqrt(16)...")
        result = await client.call_tool("sqrt", arguments={"x": 16})
        print(f"Response: {result.content[0].text}")
        if "4" in result.content[0].text:
            print("✓ Square root tool works correctly (√16 = 4)")
        else:
            print("✗ Square root tool failed")
        print()
        
        # Test 4: Prime check
        print("Test 4: Testing is_prime(17)...")
        result = await client.call_tool("is_prime", arguments={"n": 17})
        print(f"Response: {result.content[0].text}")
        if "is prime" in result.content[0].text:
            print("✓ Prime check tool works correctly (17 is prime)")
        else:
            print("✗ Prime check tool failed")
        print()
        
        # Test 5: Division by zero (error handling)
        print("Test 5: Testing error handling with divide(10, 0)...")
        result = await client.call_tool("divide", arguments={"a": 10, "b": 0})
        print(f"Response: {result.content[0].text}")
        if "Error" in result.content[0].text or "zero" in result.content[0].text.lower():
            print("✓ Error handling works correctly")
        else:
            print("✗ Error handling failed")
        print()
        
        # Test 6: Power
        print("Test 6: Testing power(2, 10)...")
        result = await client.call_tool("power", arguments={"base": 2, "exponent": 10})
        print(f"Response: {result.content[0].text}")
        if "1024" in result.content[0].text:
            print("✓ Power tool works correctly (2^10 = 1024)")
        else:
            print("✗ Power tool failed")
        print()
        
        # Test 7: Factorial
        print("Test 7: Testing factorial(5)...")
        result = await client.call_tool("factorial", arguments={"n": 5})
        print(f"Response: {result.content[0].text}")
        if "120" in result.content[0].text:
            print("✓ Factorial tool works correctly (5! = 120)")
        else:
            print("✗ Factorial tool failed")
        print()
        
        # Test 8: GCD
        print("Test 8: Testing gcd(48, 18)...")
        result = await client.call_tool("gcd", arguments={"a": 48, "b": 18})
        print(f"Response: {result.content[0].text}")
        if "6" in result.content[0].text:
            print("✓ GCD tool works correctly (gcd(48, 18) = 6)")
        else:
            print("✗ GCD tool failed")
        print()
        
        print("=" * 50)
        print("All tests completed!")
        print("=" * 50)


def main():
    """Main entry point."""
    try:
        asyncio.run(test_math_server())
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

