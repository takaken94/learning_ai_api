# AI 関連の API（Gemini、OpenAI）の学習・試用

## 概要
生成 AI 関連の API（Gemini、OpenAI）を学習・試用するためのリポジトリです。

## 準備
### 1. API キー
リポジトリのルートディレクトリに .env ファイルを作成し、API キーを設定してください。

**ファイル名: `.env`**
```text
GEMINI_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
```
## 開発環境
本プロジェクトは、 **Dev Container** を使用しています。

### 実行手順
1. **事前準備:** Docker 環境と VS Code (拡張機能: Dev Containers) を用意します。
2. **プロジェクト起動:** 本リポジトリを VS Code で開き、右下のポップアップまたはコマンドパレットから `コンテナで再度開く (Reopen in Container)` を選択します。
3. コンテナ内のターミナルで以下のコマンドを実行します。
```bash
# Gemini のテスト
python gemini_api.py
```

```bash
# OpenAI のテスト
python openai_api.py
```
