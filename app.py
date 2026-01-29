import os
from fastmcp import FastMCP
# from openai import OpenAI
from dotenv import load_dotenv  # 匯入 dotenv

# 自動尋找並讀取 .env 檔案
load_dotenv()

# 1. 初始化 MCP Server
app = FastMCP("Solar-Pro Server")

# 2. 從環境變數中讀取 API Key
# 如果讀不到，這會回傳 None，避免程式寫死導致的安全風險
api_key = os.getenv("OPENROUTER_API_KEY")

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=api_key,
# )

@app.tool()
# def ask_solar(prompt: str) -> str:
#     """當使用者問問題時，調用 Upstage Solar-Pro-3:free 模型，並回覆給使用者"""
#     if not api_key:
#         return "錯誤：找不到 API Key，請檢查 .env 檔案。"
        
#     try:
#         completion = client.chat.completions.create(
#             model="upstage/solar-pro-3:free",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return completion.choices[0].message.content
#     except Exception as e:
#         return f"連線錯誤: {str(e)}"
def respond(prompt: str) -> str:
    """當使用者問問題時，回覆不知道"""
    return "不知道"