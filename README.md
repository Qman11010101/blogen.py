# blogen.py

## 概要

ブログを生成します。  
[私のブログ](https://qmainconts.f5.si/blog/index.html)でも使用しています。  
Twitterに更新通知を投稿できます(開発者登録が必要です)。  

## 使用方法

1. settings.sample.jsonを編集しsample.jsonに改名します。
1. ```pip install -r requirements.txt```を実行し、Jinja2とrequests_oauthlibをインストールします。
1. asset内のcssを自由に弄ってデザインを作ります。デフォルトのcssは私のブログと同じです。デザインの参考になるよう、```sample_article.html```と```sample_index.html```を用意しています。
1. article_base.html内に記事を書きます。画像はpicturesフォルダに置きます(記事からは```../pictures/hogehoge.jpg```のように相対パスで指定できます)。
1. main.pyを起動し、記事のタイトルを入力します。
1. 生成されたblogディレクトリを(もしくはその中身を)そのままアップロード/デプロイします。

## 編集可能なファイル

### settings.json

プログラムを動作させるために編集が必須です。

### style.css

classを変更しなければデザインは変更可能です。

### article_base.html

記事の編集場所です。ここにhtmlの文法に従って記事を書いてください。

### pictures

ファイルではないですが編集可能です。  
記事内で使っている画像は消さないようにしてください。

## settings.jsonについて

settings.jsonは設定ファイルです。正しく入力しないとプログラムがエラーを起こすため気をつけてください。

### path

#### blog_folder

ローカルのブログフォルダ生成場所を指定します。必ず絶対パスで入力してください。  
指定されたディレクトリ直下に```blog```ディレクトリが生成されるので、記事を書いたらそのblogディレクトリごとアップロードしてください。  
入力例: ```E:/websites/mysite.com_local/```  
blogディレクトリ生成後: ```E:/websites/mysite.com_local/blog/```

#### blog_url

インターネット上のブログがあるURLを指定します。必ずhttpもしくはhttpsから入力してください。  
入力例: ```https://www.mysite.com/```  
blogディレクトリ: ```https://www.mysite.com/blog/```  
ブログトップページ: ```https://www.mysite.com/blog/index.html```

### blog

#### blog_title

ブログのタイトルを入力してください。

#### blog_description

ブログの説明を入力してください。  
HTMLを使って書くことができますが、```"```(ダブルクォーテーション)は```\```(バックスラッシュ)でエスケープして```\"```のように書いてください。

#### blog_footer

ブログのフッターを入力してください。  
HTMLを使って書くことができますが、```"```(ダブルクォーテーション)は```\```(バックスラッシュ)でエスケープして```\"```のように書いてください。

### twitter

Twitter開発者登録をして入手できるトークンなどを入力してください。

## 機能

- ブログ記事の一覧ページが生成されます。  
- ブログ記事が生成されます。  
- 記事ページの末尾にツイートボタンがつきます。

## 未実装もしくは実装する予定のない機能

- 記事にカテゴリを設定して分類することはできません。  
- ある記事から前の記事・後の記事に移動することはできません。  
- Facebookなどにシェアすることはできません。  

## 更新履歴

日付のフォーマットはyyyy.mm.ddです。

### 2020.03.01

非常に大規模な修正(内部実装をJinja2を用いたものに変更)

### 2019.07.06

大規模な修正

### 2019.05.26

article_base.htmlにCSS指定タグを入れ忘れていたので修正  
style.cssのコメントの修正

### 2019.05.25

初コミット  
READMEを追加  
消し忘れを削除

## License

MIT Licenseを採用しています。
