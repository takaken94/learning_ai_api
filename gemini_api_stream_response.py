from google import genai
import os
from dotenv import load_dotenv

def main():
    # API キーの取得
    load_dotenv()  # .env ファイルを読み込む
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY が設定されていません。環境変数か .env ファイルを確認してください。") 

    # クライアントの初期化
    client = genai.Client(api_key=api_key)
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