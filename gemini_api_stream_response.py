from google import genai
import os
from dotenv import load_dotenv

def main():
    # クライアントの初期化
    load_dotenv()
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    # モデルの指定
    target_model = "models/gemini-2.5-flash"
    # プロンプト
    prompt = "API でデータを処理する仕組みを教えてください。"

    try:
        response = client.models.generate_content_stream(
            model=target_model,
            contents=prompt,
        )
        for chunk in response:
            print(chunk.text, end="", flush=True)
    
    except Exception as e:
        print(f"例外が発生しました: {e}")

if __name__ == "__main__":
    main()