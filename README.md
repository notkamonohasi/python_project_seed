Pythonの環境を整備する話
=====

モチベーション
-----
- サーバーのPythonのバージョン低すぎ
    - ライブラリが対応していないなどの問題が発生
    - アノテーションが弱すぎるので最低でも`3.9`ないとダメ
    - バージョンを上げるには**管理者権限**が必要。サーバが壊れる可能性（パスワード聞きに行くの面倒）
- ライブラリの依存関係を解消するのだるい
    - `numpy`と`pandas`のバージョンは事故る可能性高い
    - 自分で良いバージョンの組合せを探すのだるい
    - インストール時にも管理者権限必要になったりしてだるい
- 人から貰ったコード動かない問題
    - 人から貰ったコードは120%動きません
    - お互いの手間を省くために**仮想環境**で作りましょう
    - ~~`requirements.txt`くらい残せ~~

解決方法
-----
- `pyenv`と`poetry`を使います
- `pyenv`
    - Pythonのバージョンを自由に変えられるすごいやつ
- `poetry`
    - Pythonのライブラリを管理してくれるすごいやつ

方法
-----
linux以外は知りません。macはこれで良い可能性が高いが、windowsは絶対これでは動きません
1. `pip3 install poetry`
    - `poetry`をインストール
    - ここで管理者権限が必要になるかも
2.  [このサイト](https://zenn.dev/hr0t15/articles/8ae3564bde2cce)に従って`pyenv`をダウンロード
    - 手抜きですみません。。。
    - `~/.bashrc`はターミナル起動時に実行されるやつで、ここに色々書き込んだりする
3. `pyenv install 3.X.Y`
    - 欲しいPythonのバージョンをインストール
4. `pyenv gloabal 3.X.Y`
    - 環境全体のPythonのバージョンが`3.X.Y`になる
5. `cd {workspaceFolder}`
    - 作業ディレクトリに移動
6. `poetry init`
    - `pyproject.toml`が作られる
    - 色々聞かれるが、Pythonのバージョンを`^3.X`に変え、他はdefaultで良い
7. ``poetry env use `which python3` ``
    - `poetry`がこのPythonに従う
    - nadalで試した時は不要だったが、よく分からない
8. `poetry shell`
    - 仮想環境に入れる
    - コマンドラインの左に`${workspaceFolder}-py3.X`とでればok
    - 2回目以降は`poetry shell`だけでok

結果
----- 
```shell-session
(python-project-seed-py3.11) k_tokunaga@nadal:~/master/python_project_seed$ python3 --version
Python 3.11.1
```
- nadalのPythonのバージョンを上げられた

その他
-----
- ディレクトリ構成は[これ](https://github.com/notkamonohasi/python_project_seed)を参考に