# -*- coding:utf-8 -*-
import MeCab
from gensim.models import word2vec
from glob import glob
import requests
import re
from bs4 import BeautifulSoup

# 歌詞を読み込む
def read_doc(directory):
    text = ""
    for path in directory:
        with open(path,'r',errors='ignore') as f:
            text += f.read()
    return text
# 形態素解析
def split_into_words(doc):
    mecab = MeCab.Tagger("-Ochasen")
    lines = mecab.parse(doc).splitlines()
    words = []
    stop_word = create_stop_word()
    for line in lines:
        chunks = line.split('\t')
        if len(chunks) > 3 and not chunks[2] in stop_word:
            if chunks[3].startswith('動詞'):
                words.append(chunks[2])
            if chunks[3].startswith('名詞') and not chunks[0] in stop_word:
                words.append(chunks[0])
            if chunks[3].startswith('形容詞'):
                words.append(chunks[2])
            if chunks[3].startswith('形容動詞'):
                words.append(chunks[2])    
    return words

def create_stop_word():
    target_url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
    r =requests.get(target_url)
    soup=BeautifulSoup(r.text, "html.parser")
    stop_word=str(soup).split()
    my_stop_word = ["つぶやく","ら","ひる","君","色","かたつむり","彼氏","飲む","ちゃう","する","コンビニ","の","角","無理","予約","ボウリング","立ち読み","ファッション","雑誌","糖","缶","ただ","すぎ","縄","発","偏差","ぃ","せる","頂戴","浮気","くる","びっくり","いじめ","しまう","くん","ふう","ちょうだい","コーヒー"]
    stop_word.extend(my_stop_word)
    return stop_word
if __name__ == "__main__":
    filePathList = glob("kashi/akb48/*")
    kashi = read_doc(filePathList)
    # 英数字の削除
    kashi = re.sub("[a-xA-Z0-9_]","",kashi)
    # 記号の削除
    kashi = re.sub("[!-/:-@[-`{-~]","",kashi)
    sentence = [split_into_words(kashi)]
    model = word2vec.Word2Vec(sentence, size=200, min_count=4, window=5, iter=40)
    love = model.wv.most_similar(positive=[u"恋"], topn=10)
    for i, lv in enumerate(love):
        print(str(i) + "    " + lv[0] + "    " + str(lv[1]))
