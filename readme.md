# Discord Group Leaver

## インストール方法

### 1. 仮想環境の作成
以下のコマンドを実行して、仮想環境を作成します。

```sh
python -m venv .venv  # 仮想環境の作成
```

### 2. 仮想環境のアクティベート
環境によってアクティベート方法が異なります。

#### Windows (CMD)
```sh
.venv\Scripts\activate
```

#### Windows (PowerShell)
```sh
.venv\Scripts\Activate.ps1
```

#### Mac/Linux
```sh
source .venv/bin/activate
```

### 3. 依存関係のインストール
```sh
pip install discord.py-self
```

### 4. スクリプトの実行
```sh
python main.py
```

## 注意事項
- `discord.py-self` は公式には非推奨となっており、使用にはリスクがあります。  
- Discord の規約に違反する可能性があるため、自己責任で使用してください。

## ライセンス
このプロジェクトのライセンスは [MIT License](LICENSE) です。
