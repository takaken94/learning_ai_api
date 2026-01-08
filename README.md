# AI 関連の API（Gemini、OpenAI）の学習・試用

## 概要
Python 等で、生成 AI 関連の API（Gemini、OpenAI）の学習・試用するためのリポジトリです。

## 準備

### 1. ライブラリのインストール
以下のコマンドを実行して、必要なライブラリを一括インストールしてください。

```bash
pip install -r requirements.txt
```

### 2. API キー
リポジトリのルートディレクトリに .env ファイルを作成し、API キーを設定してください。

**ファイル名: `.env`**
```text
GEMINI_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
```

## 実行方法
```bash
# Gemini のテスト
python gemini_api.py

# OpenAI のテスト
python openai_api.py
```
