from datetime import datetime
import os
import json
import sys
import shutil
from distutils.dir_util import copy_tree

from jinja2 import Environment, FileSystemLoader
from requests_oauthlib import OAuth1Session

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # カレントディレクトリを指定
current_dir = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader=FileSystemLoader("./", encoding="utf-8"))
top_template = env.get_template("assets/top_template.html")
article_template = env.get_template("assets/article_template.html")

# with open("config.toml", mode="r", encoding="utf-8_sig") as cftf:
#     config = toml.load(cftf)

with open("settings.json", encoding="utf-8_sig") as s:
    config = json.load(s)

blog_folder = config["path"]["blog_folder"]
blog_url = config["path"]["blog_url"]
blog_title = config["blog"]["blog_title"]
blog_description = config["blog"]["blog_description"]
blog_footer = config["blog"]["blog_footer"]

ckey = config["twitter"]["consumer_key"]
csec = config["twitter"]["consumer_secret"]
atkn = config["twitter"]["access_token"]
asec = config["twitter"]["access_secret"]

os.chdir(blog_folder)
os.makedirs("articles/", exist_ok=True)
os.makedirs("pictures/", exist_ok=True)
os.chdir(current_dir)  # 戻ってくる

print("記事のタイトルを入力してください")
article_title = input(">> ")
current_time = datetime.now().strftime("%Y%m%d%H%M%S")
article_id = str(current_time)
day_str = str(datetime.now().strftime("%Y-%m-%d"))

if os.path.isfile("articles.json"):
    with open("articles.json", encoding="utf-8_sig") as atl:
        article_list = json.load(atl)
else:
    article_list = []

ariticle_object = {
    "id": article_id,
    "date": day_str,
    "title": article_title
}

article_list.append(ariticle_object)

article_list.reverse()

# トップページのレンダリング
render_top = {
    "title": blog_title,
    "blogDesc": blog_description,
    "footerText": blog_footer,
    "articleList": article_list
}

index_path = f"{blog_folder}index.html"

with open(index_path, mode="w", encoding="utf-8_sig") as f:
    f.write(top_template.render(render_top))

article_list.reverse()

with open("articles.json", mode="w", encoding="utf-8_sig") as atl:
    json.dump(article_list, atl, indent=4, ensure_ascii=False)

# 記事のレンダリング
with open("assets/article_base.html", mode="r", encoding="utf-8_sig") as b:
    article_text = b.read()

render_article = {
    "articleTitle": article_title,
    "title": blog_title,
    "blogDesc": blog_description,
    "articleText": article_text,
    "footerText": blog_footer,
}

file_path = f"{blog_folder}articles/{article_id}.html"

with open(file_path, mode="w", encoding="utf-8")as f:
    f.write(article_template.render(render_article))

copy_tree("pictures", f"{blog_folder}pictures")
shutil.copy("assets/style.css", f"{blog_folder}style.css")

input("ファイルの準備ができました。サーバーへのアップロードが完了したら、キーを押して続行してください。Twitterに更新通知が投稿されます")

# Twitterに更新通知をツイートする
endpoint = "https://api.twitter.com/1.1/statuses/update.json"
tweet = "ブログを更新しました: " + article_title + \
    f" {blog_url}articles/" + article_id + ".html"
params = {"status": tweet}
twAuth = OAuth1Session(ckey, csec, atkn, asec)
postReq = twAuth.post(endpoint, params=params)
if postReq.status_code != 200:  # ここも自動化できたらうれしい
    print("HTTP Status Code:" + str(postReq.status_code))
    print("エラーが発生した可能性があります。")
    print("articleフォルダ内の最新記事とindex.htmlにある最新記事へのリンクを削除し、再試行してください。")
    print("もしくは、更新通知のみを手動で行ってください。")
    input("Enterを押すとプログラムが終了します。")
else:
    input("更新通知が正常に投稿されました。Enterキーを押して終了します")
