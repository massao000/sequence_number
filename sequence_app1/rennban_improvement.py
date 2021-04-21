# ファイルを連番で作成
# https://www.javadrive.jp/python/file/index9.html
# https://techacademy.jp/magazine/18986
# https://qiita.com/Oz-Spade/items/7fa479fae7a0ea6fcddf
# https://deep-blog.jp/engineer/12248/
# https://www.sejuku.net/blog/67787


import os
import time
from itertools import count
import subprocess


#####  #####
class CreateDirFileMove:
    def __init__(self):
        self.filepas = filepas

    def directory_move(self):
        os.chdir(self.filepas) # ディレクトリの移動

class CreateDirFile:
    def __init__(self):
        self.filename = filename       
    
    def create_file(self):
        os.mkdir(self.filename) # フォルダの作成

##### 連番作成 #####
class CreateSerialNumber(CreateDirFileMove,CreateDirFile):
    def __init__(self, name, numbers, extension, selection_zero):
        CreateDirFileMove.__init__(self)
        CreateDirFile.__init__(self)
        
        self.name = name
        self.numbers = numbers
        self.extension = extension
        self.selection_zero = selection_zero
        self.count = 1

    def sequence(self):
        super().directory_move()
        super().create_file()
        if self.selection_zero == 1:
            for i in range(self.numbers):
                f = open(f"{self.filepas}\{self.filename}\{self.count}{self.name}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 2:
            for i in range(self.numbers):
                f = open(f"{self.filepas}\{self.filename}\{self.count}_{self.name}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 3:
            for i in range(self.numbers):
                f = open(f"{self.filepas}\{self.filename}\{self.name}{self.count}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 4:
            for i in range(self.numbers):
                f = open(f"{self.filepas}\{self.filename}\{self.name}_{self.count}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1

    def zero_padding(self):
        super().directory_move()
        super().create_file()
        if self.selection_zero == 1:
            for i in range(self.numbers):
                f = open(f"{self.filepas}\{self.filename}\{'{0:02d}'.format(self.count)}{self.name}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 2:
            for i in range(self.numbers):
                f = open(f"{self.filepas}\{self.filename}\{'{0:02d}'.format(self.count)}_{self.name}.{self.extension}","w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 3:
            for i in range(self.numbers):
                f = open(f"{self.filepas}\{self.filename}\{self.name}{'{0:02d}'.format(self.count)}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 4:
            for i in range(self.numbers):
                f = open(f"{self.filepas}\{self.filename}\{self.name}_{'{0:02d}'.format(self.count)}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1



class CreateSerialNumberExistingFile(CreateDirFileMove):
    def __init__(self, name, numbers, extension, selection_zero):
        CreateDirFileMove.__init__(self)
        self.name = name
        self.numbers = numbers
        self.extension = extension
        self.selection_zero = selection_zero
        self.count = 1

    def padding_2(self):
        super().directory_move()
        if self.selection_zero == 1:
            for i in range(self.numbers):
                f = open(f"{self.count}{self.name}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 2:
            for i in range(self.numbers):
                f = open(f"{self.count}_{self.name}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 3:
            for i in range(self.numbers):
                f = open(f"{self.name}{self.count}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 4:
            for i in range(self.numbers):
                f = open(f"{self.name}_{self.count}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1

    def zero_padding_2(self):
        super().directory_move()
        if self.selection_zero == 1:
            for i in range(self.numbers):
                f = open(f"{'{0:02d}'.format(self.count)}{self.name}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 2:
            for i in range(self.numbers):
                f = open(f"{'{0:02d}'.format(self.count)}_{self.name}.{self.extension}","w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 3:
            for i in range(self.numbers):
                f = open(f"{self.name}{'{0:02d}'.format(self.count)}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1
        elif self.selection_zero == 4:
            for i in range(self.numbers):
                f = open(f"{self.name}_{'{0:02d}'.format(self.count)}.{self.extension}", "w", encoding='UTF-8')
                f.close()
                self.count += 1


class ContentsHtml(CreateDirFile,CreateDirFileMove):
    def __init__(self, name):
        CreateDirFileMove.__init__(self)
        CreateDirFile.__init__(self)
        self.name = name

    def html(self):
        super().directory_move()
        super().create_file()
        for i in program_list:
            os.mkdir(f'{self.filepas}\{self.filename}\{i}')
        f = open(f"{self.filepas}\{self.filename}\{program_list[0]}\\script.js","w", encoding='UTF-8')
        f.close()
        f = open(f"{self.filepas}\{self.filename}\{program_list[2]}\style.css","w", encoding='UTF-8')
        f.write('')
        f.close()
        f = open(f"{self.filepas}\{self.filename}\その他styleURL.txt","w", encoding='UTF-8')
        f.write('getbootstrap\nhttps://getbootstrap.com/docs/3.4/\n\nsanitize.css\nhttps://csstools.github.io/sanitize.css/')
        f.close()
        f = open(f"{self.filepas}\{self.filename}\{self.name}.html","w", encoding='UTF-8')
        f.write('<!DOCTYPE html>\n<html lang="js">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n\n    <!-- Latest compiled and minified CSS -->\n    <link rel="stylesheet"\n    href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"\n    integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu"\n    crossorigin="anonymous">\n\n    <!-- Optional theme -->\n    <link rel="stylesheet"\n    href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap-theme.min.css"\n    integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ"\n    crossorigin="anonymous">\n\n    <link rel="stylesheet" href="css\style.css">\n    <title>Document</title>\n</head>\n<body>\n\n    <script src="JavaScript\script.js"></script>\n</body>\n</html>\n') # 作られたファイルに文字が入れられる
        f.close()

class Markdown(CreateDirFile,CreateDirFileMove):
    def __init__(self):
        CreateDirFileMove.__init__(self)
        CreateDirFile.__init__(self)

    def mark(self):
        super().directory_move()
        super().create_file()
        f = open(f"{self.filepas}\{self.filename}\\basics.md","w", encoding='UTF-8')
        f.write('# 見出し1\n## 見出し2\n### 見出し3\n#### 見出し4\n##### 見出し5\n\n**太字**\n\n*斜字*\n\n~~削除します~~\n\n***\n線を引く\n\n---\n\n---\n___\n***\n\n* 箇条書き1\n* 箇条書き2\n  * 箇条書き3\n  * 箇条書き4\n    * 箇条書き5\n    * 箇条書き6\n* 箇条書き7\n    * 箇条書き8\n\n1. 数字付き1\n1. 数字付き2\n1. 数字付き3\n\n> 引用\n>> 二重引用\n>\n> 二重引用あとは一つ行空けた方が良いみたい\n>\n\n### テーブル \n| A列 | B列 | C列 |D列|E列|\n|-----|:---:|-----|--:|---|\n| あ  | い  | う  |え |お |\n| か  | き  | く  |け |こ |\n| さ  | し  | す  |せ |そ |\n\nソースコードも書ける。実行はできない。\n\n【Python】\n```python\n# コメント\nimport numpy\nimport pandas\n\nprint("Hello World")\n```\n【C言語】\n```c\n// コメント\n#include<stdio.h>\n\nint main(){\n    printf("Hello World")\n}\n```\n\n【C++】\n```c++\n// コメント\n#include <iostream>\nusing namespace std;\n\nint main(void){\n    cout << "Hello World" << endl\n}\n```\nCとC++は同じ色付けだね。（そりゃそーか）\n\n---\n\n改行するときはスペース2つ入れる↓\n\n【拡張機能：HTMLやPDFに変換】\nhttp://www.atmarkit.co.jp/ait/articles/1804/27/news034.html\n\n[リンク⇒拡張機能：HTMLやPDFに変換](http://www.atmarkit.co.jp/ait/articles/1804/27/news034.html)\n***\nほとんど同じことが書いてありますが参考程度においておきます\n\n* [マークダウン基礎1](https://qiita.com/Minalinsky_1911/items/b684cfabe0f2fde0c67b)\n\n* [マークダウン基礎2](https://qiita.com/kamorits/items/6f342da395ad57468ae3)\n\n[いろんなマークダウン](https://github.com/matiassingers/awesome-readme)\n\n****\n画像の表示や動画の表示\n\n* [画像の表示](https://qiita.com/ROY_M/items/2c4feb5de05535441bc8)\n\n* [gif変換サイト](https://rakko.tools/tools/86/)\n\n* [動画の表示参考ページ:1](https://qiita.com/i-to-to-to-mi/items/e73eb0a5899f111d0e64)\n\n* [動画の表示参考ページ:2](https://qiita.com/kosuke0820/items/ebeb0c59b603c7224eac)\n\n* [動画の表示参考ページ:3](https://qiita.com/yamataku29/items/fb14fb99f5024e01b4b8)\n\n[バッチのつけ方](https://qiita.com/koeri3/items/f85a617dcb6efebb2cab)\n\n[バッチのつけ方](https://kic-yuuki.hatenablog.com/entry/2019/06/29/173256)\n')
        f.close()
        f = open(f"{self.filepas}\{self.filename}\\template.md","w", encoding='UTF-8')
        f.write('最初にアイキャッチ画像などを表示\n\n# リポジトリ名\nこのソフトはどんなもので、何ができるのかを書く\n合わせて、簡単なデモ（使用例）などスクリーンショットやGIFアニメで表示\n\n## Dependency\n使用言語とバージョン、必要なライブラリとそのバージョンを書く\nPythonならrequirements.txtを用意するのも良い\n\n## Setup\nセットアップ方法を書く。用意するハードウェアとソフトウェアをセットアップするためのコマンドを記載する\n\n## Usage\n使い方。なるべく具体的に書く。サンプルも書く\n\n## License\nThis software is released under the MIT License, see LICENSE.\n\n## Authors\n作者を明示する。特に、他者が作成したコードを利用する場合は、そのコードのライセンスに従った上で、リポジトリのそれぞれのコードのオリジナルの作者が誰か分かるように明示する（私はそれが良いと思い自主的にしています）。\n\n## References\n参考にした情報源（サイト・論文）などの情報、リンク\n')
        f.close()
        f = open(f"{self.filepas}\{self.filename}\\参考url.txt","w", encoding='UTF-8')
        f.write('マークダウン基礎\nhttps://qiita.com/Minalinsky_1911/items/b684cfabe0f2fde0c67b\n\n様々なマークダウンのまとめたgithub URL\nhttps://github.com/matiassingers/awesome-readme\n\nフォントカラー\nhttps://qiita.com/twipg/items/d8043cd4681a2780c160')
        f.close()


class FileOne(CreateDirFileMove):
    def __init__(self, name, extension):
        CreateDirFileMove.__init__(self)
        
        self.name = name
        self.extension = extension

    def file_ze(self):
        # super().directory_move()
        f = open(f"{self.filepas}\\{self.name}.{self.extension}", "w", encoding='UTF-8')
        f.close()


class OpenFolderXXX(CreateDirFileMove):
    def __init__(self):
        CreateDirFileMove.__init__(self)

    def open_folder_txt(self):
        # super().directory_move()
        explorer_list = []
        for i in self.filepas:
            explorer_list.append(i)
            # x = '\\'
        # if explorer_list[-1] != x:
        #     explorer_list.append(x)
            self.filepas = "".join(explorer_list)
        # Arrange(sts).loading()
        subprocess.run(f'explorer {self.filepas}')


class OpenFolder(CreateDirFile,CreateDirFileMove):
    def __init__(self):
        CreateDirFileMove.__init__(self)
        CreateDirFile.__init__(self)

    def open_folder(self):
        # super().directory_move()
        # super().create_file()
        explorer_list = []
        for i in self.filepas:
            explorer_list.append(i)
            x = '\\'
        if explorer_list[-1] != x:
            explorer_list.append(x)
            self.filepas = "".join(explorer_list)
        # Arrange(sts).loading()
        subprocess.run(f'explorer {self.filepas}{self.filename}')


##### 表示文字にアニメーションをつける #####
class Arrange:
    def __init__(self, selectors):
        self.selectors = selectors
        self.times = 1
        self.interval = 0.023 #0.09 
        self.keisen = '───────────────────────┤メニューの選択│' # 罫線
        self.keisen2 = '──────────────────────────────────────' # 罫線
    # 配列にしないとできないアニメーション
    def display(self):
        print(self.keisen)
        for i, list_string in enumerate(self.selectors):
            one_character = []
            stairs = []
            for moji in list_string:
                one_character += moji
                comma_character = ",".join(one_character)
                l = comma_character.replace(",", '')
                stairs.append(l)
            for v in range(self.times):
                for st in stairs:
                    print(f"{st}", end="")
                    time.sleep(self.interval)
                    print("\r", end="")
                print()
        print(self.keisen2)

    def loading(self): # 使うかわからない
        for n in range(5):
            for i in self.selectors:
                print('\r %c ' %i, end='')
                time.sleep(self.interval)
                print('\r', end="")

    def end_loading():
        # print(f"実行されました")
        for i in range(5, -1, -1):
            print('\rプログラム終了まで > %d' %i, end='')
            time.sleep(0.85)
        print()

        
##### y\n判断 #####
class YesOrNo(CreateSerialNumber):
    def __init__(self, message):
        self.message = message

    def selection(self):
        while True:
            # sequence_file = CreateSerialNumber(filepas, filename, name, numbers, extension, selection_zero)
            x = input(self.message)
            if x == "y":
                # xn.zero_padding()
                # break
                return x
            elif x == "n":
                # xn.sequence()
                # break
                return x
            else:
                print("半角 英数で入力") # (y/n)
                continue


##### 入力文字の判断 #####
class InputJudgement:
    def __init__(self, judgment):
        self.judgment = judgment

    # 数字か判断
    def setting_number(self):
        while True:
            x = input(self.judgment)
            if x.isdecimal():
                x = int(x)
                return x
            else:
                print('─────────────────────────────────────')
                print("数字を入力してください")
                continue

    # 入力した拡張子がextension_listに含まれるか
    def extension_check(self):
        while True:
            extension_list = []
            extension_list += input(self.judgment)
            extension = ','.join(extension_list).replace(',', '')
            if extension in extension_lists:
                return extension
            else:
                print("プログラムにない拡張子または正しくない拡張子です") # false
                continue
            
    
    # 絶対パスがあるか判断
    def check_pass(self):
        while True:
            file = input(self.judgment)
            if file == '':
                continue
            file_adding = self.check_backslash(file)
            if os.path.exists(file_adding):
                print('get pass ') # 消してもいい
                return file_adding
            else:
                print('no get pass (絶対パスが正しくありません)') # 消してもいい
                continue

    # c:の後に\があるか判断　なければつける
    def check_backslash(self, aaa):
        judg = self.judgment
        c_koron = []
        for i in aaa:
            c_koron.append(i)
        nanba = len(c_koron)
        x = '\\'
        y = ':'
        if nanba == 2:
            c_koron.append(x)
            aaa = "".join(c_koron)
        elif  nanba > 3 and c_koron[2] != x:
            c_koron.insert(2, x)
            aaa = "".join(c_koron)
        return aaa

    # フォルダがすでに存在するか
    def check_folder(self, filep):
        self.filep = filep
        while True:    
            folder = input(self.judgment)
            if folder == '':
                print("空白です")
                continue
            folder_change = self.check_special(folder)
            # pas = os.path.exists(folder)
            if os.path.exists(f'{self.filep}\\{folder_change}'):
                print('exist folder (常に存在するフォルダ)') # 消してもいい
                continue
            # elif folder == '':
            #     print('no file name (何も入力がされていない)')
            #     continue
            else:
                print('creatable folder (作成可能)') # 消してもいい
                return folder_change

    # フォルダの中に同じファイルがあるかチェック
    def check_folder_ex(self, absolute, file_name):
        self.absolute = absolute
        self.file_name = file_name
        while True:
            file_name = input(self.file_name)
            if file_name == '':
                print("空白です")
                continue
            file_name_change = self.check_special(file_name)
            extension_list = []
            extension_list += input(self.judgment)
            extension = ','.join(extension_list).replace(',', '')
            if extension in extension_lists:
                if os.path.isfile(f'{self.absolute}\\{file_name_change}.{extension}'):
                    print('exist folder (常に存在するファイル名です)') # 消してもいい
                    # name = input(name)
                    continue
                else:
                    print('creatable folder (作成可能)') # 消してもいい
                    return file_name_change, extension
            else:
                print("プログラムにない拡張子または正しくない拡張子です") # false
                continue


    # ファイルに特殊文字が入っているか
    def check_special(self, special):
        not_filename = ['\\', '/', '?', '*', '"', '<', '>', '|']
        name_list = []
        for i in special:
            name_list.append(i)
            if i in not_filename:
                name_list.pop()
            change = ''.join(name_list)
        return change

    def no_name(self):
        # self.nana = nana
        while True:
            x = input(self.judgment)
            if x == '':
                print("空白です")
                continue
            else:
                return x
    


# ファイル作成いるかもしれない(no number ファイルの作成)
systems_list = ["1：連番ファイル作成", "2：フォルダの作成", "3：ファイルの作成", "4：HTMLテンプレート作成", "5：Markdownテンプレートの作成", "6：プログラム終了"]
select_number = ['1：1xxx.xxx', '2：1_xxx.xxx', '3：xxx1.xxx', '4：xxx_1.xxx']
menu_name = ["絶対パス：", "フォルダ名：", "ファイル名：", "作成ファイルの数：", "拡張子：", "連番タイプの選択："]
extension_lists = ['txt', 'sjis', 'dir', 'ico', 'coffee', 'pct', 'dic', 'asx', 'tif', 'abp', 'as', 'cgm', 'pmp', 'tgz', 'sh', 'xpm', 'dib', 'ani', 'wmv', 'uu', 'ts', 'aif', 'fpx', 'rm', 'rpm', 'Z', 'sys', 'mat', 'htm', 'cab', 'h', 'xsl', 'bat', 'pcd', 'ml', 'pas', 'cobol', 'cpp', 'mht', 'pdf', 'erl', 'dvr', 'lhs', 'pro', 'rle', 'wvx', 'mng', 'asp', 'db', 'mid', 'dcr', 'ai', 'php', 'c', 'vrml', 'sql', 'xml', 'ini', 'ras', 'swi', 'lisp', 'pm', 'm', 'url', 'd', 'forth', 'pict', 'ra', 'zip', 'bin', 'asm', 'art', 'clj', 'inf', 'html', 'jpe', 'dwt', 'rv', 'wma', 'chm', 'py', 'jsx', 'tmp', 'log', 'jpg', 'mov', 'pic', 'exe', 'ppd', 'snd', 'eps', 'cdr', 'tcl', 'tga', 'xquery', 'mac', 'rtf', 'asc', 'reg', 'scala', 'wrl', 'ps', 'obj', 'qt', 'mpg', 'mpeg', 'vbs', 'aifc', 'css', 'maki', 'cnf', 'man', 'conf', 'wpg', 'rmm', 'jfif', 'bmp', 'gif', 'asf', 'ttf', 'mag', 'q0', 'swf', 'dxr', 'jxw', 'com', 'nsk', 'jpeg', 'ocx', 'hx', 'lsl', 'sj1', 'j6i', 'rs', 'pcx', 'pnm', 'doc', 'aiff', 'js', 'xbm', 'sit', 'cf', 'cgi', 'pl', 'au', 'cam', 'dll', 'vdo', 'class', 'png', 'fon', 'dart', 'xht', 'dpx', 'smi', 'a', 'bak', 'cs', 'ram', 'cmp', 'avi', 'scr', 'so', 'wmf', 'tar', 'smil', 'cur', 'old', 'org', 'ttc', 'midi', 'mp3', 'hlp', 'shtml', 'wax', 'csv', 'tiff', 'pps', 'xhtml', 'wri', 'jar', 'go', 'v', 'scm', 'xls', 'groovy', 'hs', 'wav', 'lua', 'rb', 'java', 'lzh', 'r', 'ppt', 'gz', 'dat', 'mp4', 'json', 'md']
program_list = ['JavaScript', 'img', 'css']
select_list = ['1：新規フォルダに作成', '2：既存フォルダに作成'] # 仮でつけている
sts = ["｜", "／", "ー", "＼", "｜", "／", "ー", "＼"]
# not_filename = ['\\', '/', '?', '*', '"', '<', '>', '|']
# input_bunn = ["使いたいものの数字を入力："]

# filepasとfilenameを変数と宣言しているからクラスのCreateDirFileMove　CreateDirFileが動いている

while True:
    # number = int(input("使いたいものの数字を入力："))
    Arrange(systems_list).display() # 数字か判断
    # arrange.display()

    # decide_number = ("使いたいものの数字を入力：")
    number = InputJudgement("使いたいものの数字を入力：").setting_number()
    # number = number.setting_number()
    file_option = 0

    if number == 1:
        print(systems_list[0][2:])
        
        Arrange(select_list).display() # file_option_check名前変更
        # file_option_check.display()
        
        file_option = InputJudgement("使いたいものの数字を入力：").setting_number()
        # file_option = file_option.setting_number()
            
        if file_option == 1: # エクスプローラー開く
            print(select_list[0][2:]) # 新規
                        # 絶対パス
            filepas = InputJudgement(menu_name[0]).check_pass() # からもじっだた時の処理を書く
            # filepas = InputJudgement(filepas).check_backslash()
            # filepas = filepas.check_pass() # 絶対パスがあるか

            filename = InputJudgement(menu_name[1]).check_folder(filepas) # フォルダ名
            name = InputJudgement(menu_name[2]).no_name() # ファイル名

                # 拡張子チェック
            extension = InputJudgement(menu_name[4]).extension_check()
            # extension = extension.extension_check()

                # 作成ファイルの数
            numbers = InputJudgement(menu_name[3]).setting_number()
            # numbers = numbers.setting_number()

            Arrange(select_number).display() # 連番タイプの表示
            # arrange.display() # 選択数字の表示

                # selection_zero = (menu_name[5]) 
            selection_zero = InputJudgement(menu_name[5]).setting_number() # 連番タイプの選択
            # selection_zero = selection_zero.setting_number() # 数字か判断

            zero_number = ("ゼロ詰めにしますか？(y/n)：")

            yes_or_no = YesOrNo(zero_number).selection()
            # yes_or_no = yes_or_no.selection()

            if yes_or_no == "y":
                CreateSerialNumber(name, numbers, extension, selection_zero).zero_padding()       
            elif yes_or_no == "n":
                CreateSerialNumber(name, numbers, extension, selection_zero).sequence()
            # break

        elif file_option == 2: # エクスプローラー開けない
            print(select_list[1][2:]) # 既存

            # 絶対パス
            filepas = InputJudgement(f'作成先の{menu_name[0]}').check_pass()
            # 絶対パスに C:demoのように C: の後に\\がなかったらつける
            # filepas = InputJudgement(filepas).check_backslash()

            # ファイル名がかぶらないように同じ名前、拡張子が同じだったらもう一度入力してもらう
            # name = (menu_name[2]) # ファイル名

            # InputJudgement(name).check_file(filepas)
                # 拡張子チェック
            extension_and_name = InputJudgement(menu_name[4]).check_folder_ex(filepas, menu_name[2])
            # extension = extension.extension_check()
            # InputJudgement(extension).extension_check()

                # 作成ファイルの数
            numbers = InputJudgement(menu_name[3]).setting_number()
            # numbers = numbers.setting_number()

            Arrange(select_number).display() # 連番タイプの表示
            # arrange.display() # 選択数字の表示
                # selection_zero = (menu_name[5])

            selection_zero = InputJudgement(menu_name[5]).setting_number() # 連番タイプの選択
            # selection_zero = selection_zero.setting_number() # 数字か判断


            zero_number = ("ゼロ詰めにしますか？(y/n)：")

            yes_or_no = YesOrNo(zero_number).selection()
            # yes_or_no = yes_or_no.selection()

            if yes_or_no == "y":
                CreateSerialNumberExistingFile(extension_and_name[0], numbers, extension_and_name[1], selection_zero).zero_padding_2()       
            elif yes_or_no == "n":
                CreateSerialNumberExistingFile(extension_and_name[0], numbers, extension_and_name[1], selection_zero).padding_2()
                # Arrange.end_loading()
            # break
        else:
            print(f"{file_option}は存在しないナンバー")
        # break
        # continue
    elif number == 2: # エクスプローラー開く
        print(systems_list[1][2:])
                # 絶対パス
        filepas = InputJudgement(menu_name[0]).check_pass()
        # filepas = InputJudgement(filepas).check_backslash()
        # filepas = filepas.check_pass()

        filename = InputJudgement(menu_name[1]).check_folder(filepas) # フォルダ名
        CreateDirFileMove().directory_move()
        CreateDirFile().create_file()
        #Arrange.end_loading()
        # break
    elif number == 3: # エクスプローラー開く
        print(systems_list[2][2:])
        filepas = InputJudgement(menu_name[0]).check_pass()
        # filepas = InputJudgement(filepas).check_backslash()
        # name = InputJudgement(menu_name[2]).check_file(filepas) # ファイル名
        # extension = InputJudgement(menu_name[4]).extension_check()
        extension_and_name = InputJudgement(menu_name[4]).check_folder_ex(filepas, menu_name[2])


        # extension = extension.extension_check()
        FileOne(extension_and_name[0], extension_and_name[1]).file_ze()


    elif number == 4: # エクスプローラー開く
        # テンプレートのバリエーションを作ってもいいかもしれない
        print(systems_list[3][2:])
        # 絶対パス
        filepas = InputJudgement(menu_name[0]).check_pass()
        # filepas = InputJudgement(filepas).check_backslash()
        # filepas = filepas.check_pass()
        
        filename = InputJudgement(menu_name[1]).check_folder(filepas) # フォルダ名

        name = ("index")
        ContentsHtml(name).html()
        # aa.html()

        # Arrange.end_loading()
        # ContentsHtmlを消して
        # CreateSerialNumberの変数を適当に決めて処理を一つにしてもいいかもしれない
        # break
    elif number == 5: # エクスプローラー開く
        print(systems_list[4][2:])
        # 絶対パス
        filepas = InputJudgement(menu_name[0]).check_pass()
        # filepas = InputJudgement(filepas).check_backslash()
        # filepas = filepas.check_pass()
        
        filename = InputJudgement(menu_name[1]).check_folder(filepas) # フォルダ名

        # name = ("index")
        Markdown().mark()
        # continue
        # Arrange.end_loading()
        # break
    elif number == 6:
        print(systems_list[5][2:])
        Arrange.end_loading()
        break
    else:
        print(f"{number}は存在しないナンバー")
        print(f"メニューを再表示します")
        time.sleep(0.5)
        continue

    explorer = ("作成したフォルダを開きますか？(y/n)：")
    yes_or_no = YesOrNo(explorer).selection()

    if number == 3 or file_option == 2:
        if yes_or_no == "y":
            #Arrange(sts).loading()
            OpenFolderXXX().open_folder_txt()
        elif yes_or_no == "n":
            pass
    else:
        if yes_or_no == "y":
            #Arrange(sts).loading()
            OpenFolder().open_folder()
        elif yes_or_no == "n":
            pass

    end_message = ("終了しますか？(y/n)：")
    yes_or_no = YesOrNo(end_message).selection()
    if yes_or_no == "y":
        Arrange.end_loading()
        break
    elif yes_or_no == "n":
        continue

