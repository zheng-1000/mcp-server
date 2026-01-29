from fastmcp import FastMCP
from keyss import api_key

client = OpenAI(
    base_url="https://203.64.104.13:8000/v1",
    api_key=api_key,
)

app = FastMCP("My MCP Server")

@app.tool
def add(n1:int , n2:int) -> int:
    """ADD Two numbers"""
    return n1 + n2

@app.tool()
def ask_solar(prompt: str) -> str:
    """
    調用 Upstage Solar-Pro-3 模型進行 AI 問答。
    """
    try:
        completion = client.chat.completions.create(
            model="upstage/solar-pro-3:free",
            messages=[
                {"role": "system", "content": "你是一個有幫助的助理，請以繁體中文回答。"},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"連線至 OpenRouter 時發生錯誤: {str(e)}"