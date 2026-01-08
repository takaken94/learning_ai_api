from openai import OpenAI
import os
from dotenv import load_dotenv

def main():
    # API キーの取得
    load_dotenv()  # .env ファイルを読み込む
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY が設定されていません。環境変数か .env ファイルを確認してください。")

    # クライアントの初期化
    client = OpenAI(api_key=api_key)
    # モデルの指定
    target_model = "gpt-5-nano"
    # プロンプト
    prompt = "API でデータを処理する仕組みを200文字で教えてください。"

    try:
        response = client.responses.create(
            model=target_model,
            input=prompt,
        )
        print(f"target_model={target_model}")
        print(f"prompt={prompt}")
        print(f"response.output_text={response.output_text}")
    
    except Exception as e:
        print(f"例外が発生しました: {e}")

if __name__ == "__main__":
    main()