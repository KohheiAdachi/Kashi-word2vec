import unittest
from getSong import GetSong

# song = GetSong()
#
# kashiList = song.getSongList("https://www.uta-net.com/artist/12550/")
#
# for kashi in kashiList:
#     print(kashi)

class TestGetSong(unittest.TestCase):

    def test_getsong(self):

        song = GetSong()
        kashiList = song.getSongList("https://www.uta-net.com/artist/12550/")

        # for kashi in kashiList:
        #     # print(kashi)

    def test_getsong_search(self):

        song = GetSong()
        kashiList = song.getSongList("https://www.uta-net.com/search/?Keyword=%E4%B9%83%E6%9C%A8%E5%9D%82&x=52&y=17&Aselect=1&Bselect=3",match="search")
        # for kashi in kashiList:
        #     # print(kashi)

    def test_getkashi(self):
        song = GetSong()
        kashiList = song.getSongList("https://www.uta-net.com/search/?Keyword=%E4%B9%83%E6%9C%A8%E5%9D%82&x=52&y=17&Aselect=1&Bselect=3",match="search")
        for kashiurl in kashiList:
            title,data = song.getWordofsong(kashiurl)

    def test_getkashi_search(self):
        song = GetSong()
        kashiList = song.getSongList("https://www.uta-net.com/artist/12550/")
        for kashiurl in kashiList:
            title,data = song.getWordofsong(kashiurl)

if __name__ == "__main__":
    unittest.main()
