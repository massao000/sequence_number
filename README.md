![ソースコードサイズ](https://img.shields.io/badge/test-nw-blue)
![pythinのバッチ]
![Windowsのバッチ]
<h1 align = "center">
  <br>
  <a href="https://github.com/ArmynC/ArminC-AutoExec/archive/master.zip"> <img src = "https://arminc.ga/resources/autoexec/arminc_autoexec.png" alt = " ArminC AutoExec "> </a>
</h1>
<h4 align = "center">テスト</h4>

# このプログラムの名前

このプログラムはコマンドが打てなくても連番ファイルの作成が可能


![img](https://user-images.githubusercontent.com/69783019/101378356-57bc4a80-38f6-11eb-9f5a-78a0f26df68d.png)



# demo movie
## 連番ファイル作成 movie

![mv](https://user-images.githubusercontent.com/69783019/101377992-debcf300-38f5-11eb-8b99-b6c899afa05e.gif)

# ～使い方～
 
## テキスト入力に対しての注意点と機能

各項目ごとに入力テキストに空文字入力がされたときは再入力してもらいます。

指定された入力形式でテキスト入力せれなかったら再度入力してもらいます。

絶対パスの c:demo c:<font color="Red">\\</font>demo の始めだけのスラッシュが抜けていても自動でつけてくれます。
 
フォルダ名＆ファイル名がすでにある場合または同じ名前の時、もう一度入力テキストが出ます。
（ \\ / ? * " < > | ）これらの作成できない記号がもし入れば自動で除去されたものがファイル名＆フォルダ名になります。

## 連番ファイルの作成

gifを入れる

メニューから１を入力（半角、全角どちらも可）

### 保存先の選択
 

メニューの１か２の選択

一例としては下のテーブルのように入力すると「c」ドライブに「demo」フォルダが作成され
demoフォルダの中に「test.txt」が生成予定になります。
(ファイル数10は、次の処理でパターンをきめます)

| メニュー | 1：新規フォルダに作成 | 2：既存フォルダに作成 |
|:---:|:---:|:---:|
| 絶対パスの指定 | c:\ | c:\demo |
| フォルダ名 | demo | × |
| ファイル名 | test | test2 |
| 拡張子 | txt | txt |
| ファイル数 | 10 | 10 |


 
### 連番のパターン選択


 
| 1：1xxx.xxx | 2：1_xxx.xxx | 3：xxx1.xxx | 4：xxx1_.xxx |
|:---:|:---:|:---:|:---:|

<br>
 
### ゼロ詰めにしますか？(y/n)
| y(yes) | n(no) |
|:---:|:---:|
| 01xxx.xxx | 1xxx.xxx |
| 01_xxx.xxx | 1_xxx.xxx |
| xxx01.xxx | xxx1.xxx |
| xxx01_.xxx | xxx1_.xxx |

<br>
 
### 作成したフォルダを開きますか？(y/n)

今回だと「c:\demo」のフォルダのエクスプローラーを開こうとしています。
y(yes)の場合エクスプローラーを開きます。
n(no)の場合エクスプローラーを開かずに次の処理に行きます。
 
<br>

### 終了しますか？(y/n)

---
# サブ機能

* フォルダの作成
gifをれる

* フィルの作成
gifをれる

* HTMLのテンプレート作成
gifをれる

* README.mdのテンプレート作成
gifをれる

* プログラムの終了
gifをれる

# 入力が必要な項目

| 連番ファイルの作成 | フォルダの作成 | フィルの作成 | HTMLのテンプレート作成 |READMEのテンプレート作成 |
|:---:|:---:|:---:|:---:|:---:|
| 絶対パスの指定 | 絶対パスの指定 | 絶対パスの指定 | 絶対パスの指定 | 絶対パスの指定 |
| フォルダ名 | フォルダ名 | × | フォルダ名 | フォルダ名 |
| ファイル名 | × | ファイル名 | × | × |
| 拡張子 | × | 拡張子 | × | × |
| ファイル数 | × | × | × | × |
| 連番の数字を指定 | × | × | × | × |
| ゼロ詰めにするか | × | × | × | × |
| 作成フォルダを開くか | 作成フォルダを開くか | 作成フォルダを開くか | 作成フォルダを開くか | 作成フォルダを開くか |
| 終了するか | 終了するか | 終了するか | 終了するか | 終了するか |

<br>

## 

## 使用できる環境

Windows 10




[参考ページ](https://github.com/matiassingers/awesome-readme)

[バッチのつけ方](https://qiita.com/koeri3/items/f85a617dcb6efebb2cab)

[バッチのつけ方](https://kic-yuuki.hatenablog.com/entry/2019/06/29/173256)

[gifに変換](https://rakko.tools/tools/86/)
