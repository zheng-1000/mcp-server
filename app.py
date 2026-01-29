import os
from fastmcp import FastMCP
from openai import OpenAI
from dotenv import load_dotenv

# 1. 載入 .env 檔案（在雲端部署時，記得在平台的 Environment Variables 設定 API Key）
load_dotenv()

# 2. 初始化 MCP Server
app = FastMCP("Solar-Pro AI Server")

# 3. 從環境變數獲取 OpenRouter 金鑰
api_key = os.getenv("OPENROUTER_API_KEY")

# 4. 初始化 OpenAI 客戶端 (使用 httpx 避開 proxy 報錯)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

@app.tool()
def ask_solar_ai(prompt: str) -> str:
    """
    呼叫強大的 AI 模型來回答使用者的問題。
    適合處理邏輯分析、翻譯、寫作或一般諮詢。
    """
    if not api_key:
        return "錯誤：雲端環境中未設定 OPENROUTER_API_KEY 變數。"

    try:
        completion = client.chat.completions.create(
            model="upstage/solar-pro-3:free",
            messages=[
                {"role": "system", "content": "你是一個專業的助理，請使用繁體中文回答。"},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"AI 服務暫時無法連線：{str(e)}"
