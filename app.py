from fastmcp import FastMCP

app = FastMCP("My MCP Server")
@app.tool
def add(n1:int , n2:int) -> int:
    """ADD Two numbers"""
    return n1 + n2