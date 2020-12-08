<h1 align = "center">
  <br>
  <a href="img" ><img src = "https://user-images.githubusercontent.com/69783019/101510502-5bff6b00-39bd-11eb-81a7-171c8dc90503.png" width="500" alt = " ArminC AutoExec "></a>
</h1>
<h4 align = "center">簡単に連番ファイルなどが作れる</h4>
<p align="center">
  <a href="https://img.shields.io/badge/python-3.9.0-blue">
    <img src="https://img.shields.io/badge/python-3.9.0-blue"alt="python">
  </a>
  <a href="https://img.shields.io/badge/-Windows10-blue">
    <img src="https://img.shields.io/badge/-Windows10-blue"alt="os">
  </a>

# スタートメニュー
![img](https://user-images.githubusercontent.com/69783019/101495044-5f89f680-39ab-11eb-9eb5-c4799b37a334.png)


# demo movie

![mv](https://user-images.githubusercontent.com/69783019/101377992-debcf300-38f5-11eb-8b99-b6c899afa05e.gif)

 
# テキスト入力に対しての全体の注意点と機能

* このプログラムはコマンドが打てなくても連番ファイルの作成が可能

* 各項目ごとに入力テキストに空文字入力がされたときは再入力してもらいます。

* 指定された入力形式でテキスト入力せれなかったら再度入力してもらいます。

* 絶対パスの c:demo c:<font color="Red">\\</font>demo の始めだけのスラッシュが抜けていても自動でつけてくれます。
 
* フォルダ名＆ファイル名がすでにある場合または同じ名前の時、もう一度入力テキストが出ます。

* （ \\ / ? * " < > | ）これらの作成できない記号がもし入れば自動で除去されたものがファイル名＆フォルダ名になります。

* osがはいいているCドライブに直接ファイルは作成でません。

# ～使い方～
### 連番ファイルの作成

![me1_a](https://user-images.githubusercontent.com/69783019/101502363-34f06b80-39b4-11eb-9bbf-1d0b183b9ded.gif)

メニューから１を入力

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

![img](https://user-images.githubusercontent.com/69783019/101378356-57bc4a80-38f6-11eb-9f5a-78a0f26df68d.png)

<br>
 
### 連番のパターン選択

1~4の連番のパターンを決めます。
 
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
 
### 作成したフォルダを開きますか？(y/n)

* 今回だと「c:\demo」のフォルダのエクスプローラーを開こうとしています。
* y(yes)の場合エクスプローラーを開きます。
* n(no)の場合エクスプローラーを開かずに次の処理に行きます。

 
<br>

### 終了しますか？(y/n)

---
# サブ機能 GIF

## フォルダの作成
![m2](https://user-images.githubusercontent.com/69783019/101501711-6d437a00-39b3-11eb-9327-bbfc4c1a4765.gif)

## フィルの作成
osがはいいているCドライブに直接ファイルは作成でません。
![me3](https://user-images.githubusercontent.com/69783019/101501722-6fa5d400-39b3-11eb-89cd-48c4ce9d6255.gif)

## HTMLのテンプレート作成
![me4](https://user-images.githubusercontent.com/69783019/101501728-72082e00-39b3-11eb-9f4c-b6c92451b371.gif)

## README.mdのテンプレート作成
![me5](https://user-images.githubusercontent.com/69783019/101501737-73d1f180-39b3-11eb-8411-3fc8ac34c14b.gif)


* プログラムの終了
gifをれる

## 入力が必要な項目

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

## 使用できる環境

Windows 10
