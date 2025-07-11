# 現場で活用するための生成AIエージェント実践入門 - Chapter 4

このディレクトリは、書籍「現場で活用するための生成AIエージェント実践入門」（講談社サイエンティフィック社）の第4章に関連するソースコードとリソースを含んでいます。

4章記載のコードを実行するためには、以下の手順に従ってください。

## 前提条件

このプロジェクトを実行するには、以下の準備が必要です：

- Python 3.12 以上
- Docker および Docker Compose
- VSCode

また、Python の依存関係は `pyproject.toml` に記載されています。

## VS Code ワークスペースで開く

1. VS Code を開きます。
2. プロジェクトのルートディレクトリ（`genai-agent-advanced-book`）をワークスペースとして開きます。
3. chapter4のワークスペースを選択


## 環境構築

### 1. chapter4のワークスペースを開く
chapter4 ディレクトリに仮想環境を作成します。
VS Code の ターミナルの追加で`chapter4` ワークスペースをを開きます。

### 2. Python 仮想環境の作成と依存関係のインストール

依存関係の解決には[uv]()を利用します。
`uv`のインストールは以下のとおりです。

`pip`を使う場合。
```bash
pip install uv
```

MacまたはLinuxの場合
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

依存関係のインストール
```bash
uv sync
```

インストール後に作成した仮想環境をアクティブにします。

```bash
source .venv/bin/activate
```

### 3. 環境変数のセット
`.env` ファイルを作成し、以下の内容を追加します。

```env
# OpenAI API設定
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE="https://api.openai.com/v1"
OPENAI_MODEL= "gpt-4o-2024-08-06"
```

### 4. 検索インデックスの構築

makeコマンドを使用します。

```bash
#コンテナの起動
make start.engine

#インデックスの構築
make create.index
```

`create.index`実行時にElasticsearchのコンテナでエラーが発生する場合は、`docker-compose.yml`の以下の行をコメントアウトしてください。

```yaml
    volumes:
      - ./.rag_data/es_data:/usr/share/elasticsearch/data
```
