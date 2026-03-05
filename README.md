# mlb-data-pipeline
MLB投球データ取得・Parquet変換・S3アップロード

## フォルダ構成
mlb-data-pipeline/
├─ src/                     # 共通モジュール（ローカル＆Lambda共通）
│   ├─ fetch.py             # データ取得ロジック
│   ├─ transform.py         # データ整形・変換ロジック
│   ├─ storage_local.py     # ローカル保存用（CSVやPickleなど）
│   └─ storage_s3.py        # S3保存用
│
├─ local_runner/            # ローカル開発用ランナー
│   └─ run_local.py         # ローカル実行用スクリプト
│
├─ lambda_app/              # Lambda 用アプリ
│   ├─ lambda_handler.py    # Lambda エントリーポイント
│   ├─ fetch.py             # create_lambda_zip.pyによってsrcフォルダ配下の同名ファイルから複製・更新される
│   ├─ transform.py         # create_lambda_zip.pyによってsrcフォルダ配下の同名ファイルから複製・更新される
│   └─ storage_s3.py        # create_lambda_zip.pyによってsrcフォルダ配下の同名ファイルから複製・更新される
│
├─ scripts/                 # 補助スクリプト
│   └─ create_lambda_zip.py # Lambda 用 ZIP 作成スクリプト
│
├─ venv/
├─ requirements.txt         # 依存パッケージ（pybaseball, boto3 など）
└─ README.md

## Lambdaアップロードまでの流れ
1. src/ 配下のファイルのみを編集する
2. scripts/create_lambda_zip.py を実行する
    1. lambda_app/ 配下の fetch.py, transform.py, storage_s3.py が src/ から自動生成/更新される
    2. lambda_app/ 配下のファイルがまとめてZIP化され、scripts/ 配下に出力される
3. scripts/ 配下に出力されたZIPファイルをLambdaにアップロードする