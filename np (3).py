from janome.tokenizer import Tokenizer
import re
import random
 
templatesP = [
    "それってさぁ！{}ってコト！？楽しそう！",
    "うんうん！楽しそうだね！"
    "ふふふ！{}だね！",
    "{}？それって美味しいの！？",
    "{}って最高じゃん！",
    "わ！ふふふ！（楽しそうにこっちを見ている）",
    "そうなんだ！ぼくは最近買ったんだ！なんとかバニア！これあげる！",
]

templatesN = [
    "それってさぁ！{}ってコト！？",
    "ワッ！ワッ！ワッ！ヤダァ",
    "なんとかなれー！",
    "それはとっても…悲しいね",
    "{}！？視界がモノクロになる～",
    "こんなんさァッッ絶対アレじゃん！{}じゃん！ちゃりめら食べて元気だそ！",
    "やぁぁ！はぁぁ！（元気出せ！的な意味）",
    "いやぁ！いやぁ！いやぁぁ！",
    "{}！？それって危ない奴？",
    "はぁ？",
    "そうなんだ…元気出して！これあげる！なんとかバニア！最近買ったんだ！",
    "よろこびがないぃ…"
]



#形態素解析の実行
keyword = input("キーワードを入力してください: ")
token = Tokenizer().tokenize(keyword)
 
#単語の取り出し
words = []
for line in token:
    tkn = re.split('\t|,', str(line))
    # 名詞、形容詞、動詞で判定
    if tkn[1] in ['名詞','形容詞','動詞'] :
        words.append(tkn[0])  
 
#日本語評価極性辞書（名詞編）の読み込み
with open("pn.csv.m3.120408 (1).trim",encoding='utf-8') as f:
    lines = f.readlines()    
    dic = { x.split('\t')[0]:x.split('\t')[1] for x in lines }
 
cnt = 0
judge = 0
judge1 = 0
judge2 = 0
#単語のネガポジ判定
for word in words:
    judge1 = dic.get(word,'-')
    if judge1 == ("n") or judge1 == ("p"):
       judge = judge1
    print(f'{word} : {judge1}')

    #日本語評価極性辞書（用語編）の読み込み
with open("yougo (3).trim",encoding='utf-8') as f:
    lines = f.readlines()    
    dic2 = { x.split(':')[0]:x.split(':')[1] for x in lines } 

#単語のネガポジ判定
for word in words:
    judge2 = dic2.get(word,'-')
    if judge2 == ("n") or judge2 == ("p"):
       judge = judge2
    print(f'{word} : {judge2}')


def generate_textP(word):
    template = random.choice(templatesP)  # ランダムなテンプレート選択
    generated_text = template.format(word, "追加のキーワード")  # テンプレートにキーワードを埋め込む
    return generated_text

def generate_textN(word):
    template = random.choice(templatesN)  # ランダムなテンプレート選択
    generated_text = template.format(word, "追加のキーワード")  # テンプレートにキーワードを埋め込む
    return generated_text


if judge1 == ("p"):
   generated_text = generate_textP(word)
   print(generated_text)
   cnt=1

if judge1 == ("n"):
   generated_text = generate_textN(word)
   print(generated_text) 
   cnt=1

if judge2 == ("p"):
   generated_text = generate_textP(word)
   print(generated_text)
   cnt=1

if judge2 == ("n"):
   generated_text = generate_textN(word)
   print(generated_text) 
   cnt=1

if judge1 == ("-") and judge == (0) or judge1 == ("e") and judge == (0):
   generated_text = generate_textP(word)
   print(generated_text)
   cnt=1

if judge1 == (0) and judge == (0) and judge2 == (0):
   generated_text = generate_textP(keyword)
   print(generated_text)
   cnt=1

if cnt == 0:
   generated_text = generate_textP(word)
   print(generated_text)
