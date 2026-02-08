# setup_django.ps1
# Windows 用：cookiecutter-django 一発セットアップ

# ==== 設定 ====
$project_dir = "C:\mysite\accounts"
$project_name = "my_awesome_project"
$cookiecutter_url = "https://github.com/pydanny/cookiecutter-django"

# ==== 古いプロジェクトを削除（存在する場合） ====
if (Test-Path "$project_dir\$project_name") {
    Write-Host "古いプロジェクトを削除中..."
    Remove-Item -Recurse -Force "$project_dir\$project_name"
}

# ==== プロジェクト生成（hook スキップ） ====
Write-Host "cookiecutter-django を生成中..."
cd $project_dir
cookiecutter $cookiecutter_url --no-input

# ==== 生成されたディレクトリに移動 ====
cd "$project_dir\$project_name"

# ==== 仮想環境作成 ====
Write-Host "仮想環境を作成中..."
python -m venv .venv

# ==== 仮想環境アクティブ化 ====
Write-Host "仮想環境をアクティブ化..."
.venv\Scripts\Activate.ps1

# ==== pip を最新版にアップデート ====
Write-Host "pip をアップデート中..."
python -m pip install --upgrade pip

# ==== 必要なパッケージをインストール ====
Write-Host "必要なパッケージをインストール中..."
pip install django
pip install django-environ
pip install psycopg2-binary

# ==== cookiecutter-django 推奨パッケージもインストール ====
if (Test-Path "requirements\base.txt") {
    pip install -r requirements/base.txt
}

# ==== 開発サーバ起動 ====
Write-Host "開発サーバを起動..."
python manage.py runserver
