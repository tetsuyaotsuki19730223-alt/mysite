# -*- coding: utf-8 -*-

# 仮想環境作成（すでにあれば削除）
if (Test-Path ".venv") {
    Write-Host "既存の仮想環境を削除中..."
    Remove-Item -Recurse -Force .venv
}

# 仮想環境作成
Write-Host "仮想環境を作成中..."
python -m venv .venv

# 仮想環境を有効化
Write-Host "仮想環境を有効化..."
. .\.venv\Scripts\Activate.ps1

# pip を最新に更新
Write-Host "pip を最新化中..."
python -m pip install --upgrade pip

# requirements.txt からインストール
Write-Host "パッケージをインストール中..."
python -m pip install -r requirements.txt

Write-Host "セットアップ完了！"
