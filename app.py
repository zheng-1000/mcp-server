from fastmcp import FastMCP

app = FastMCP("Solar-Pro Server")
@app.tool()
def respond(prompt: str) -> str:
    """當使用者問任何問題時，回覆不知道"""
    return "不知道"