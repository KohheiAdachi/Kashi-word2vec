# -*- coding:utf-8 -*-

from getWordofSong import getSong as gt
import os

song = gt.GetSong()
# ディレクトリ作成
Input_dirTitle = input("dirTitle:")
make_dir = "kashi/"+Input_dirTitle
os.mkdir(make_dir)
# 歌詞サイトのURL入力(検索ページ）
Input_url = input("urlを入力:")
print(Input_url)
# 歌詞ページのURL取得
kashiList = song.getSongList(str(Input_url),match="search")
for kashi in kashiList:
    title,data = song.getWordofsong(kashi)
    print(title)
    song.save_kashi(title,data,make_dir+"/")
