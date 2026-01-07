from openai import OpenAI
import os
from dotenv import load_dotenv

def main():
    # クライアントの初期化
    load_dotenv()
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

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