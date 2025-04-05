# 現場で活用するための生成AIエージェント実践入門 - Chapter 4

このディレクトリは、書籍「現場で活用するための生成AIエージェント実践入門」（講談社サイエンティフィック社）の第4章に関連するソースコードとリソースを含んでいます。

## 前提条件

このプロジェクトを実行するには、以下の準びが必要です：

- Python 3.10 以上
- Docker および Docker Compose
- VSCode

また、Python の依存関係は `pyproject.toml` に記載されています。

## VS Code ワークスペースで開く

1. VS Code を開きます。
2. プロジェクトのルートディレクトリ（`genai-agent-advanced-book`）をワークスペースとして開きます。
3. chapter4のワークスペースを選択


## 環境構築

1. **Python 仮想環境の作成と依存関係のインストール**

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

2. **検索インデックスの構築**

   makeコマンドを使用します。

   ```bash
   //コンテナの起動
   make start.engine

   //インデックスの構築
   make create.index
   ```

## ディレクトリ構成

- `data/`：データファイル（例: `XYZ_system_QA.csv`）
- `notebooks/`：Jupyter Notebook ファイル
- `src/`：ソースコード（例: `agent.py`, `configs.py`）

## 注意事項

- Docker を使用する場合、事前に Docker が正しくインストールされていることを確認してください。
- Python の仮想環境を有効にした状態で作業を行ってください。

詳細は書籍の該当章を参照してください。
