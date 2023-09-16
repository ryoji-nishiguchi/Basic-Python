text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

word_list = text.split() # カンマで区切った単語リストを作成

word_lengths_str = list(map(str, [len(word.strip(".,")) for word in word_list])) # 各単語の文字数を計算し、mapを使用して文字列のリストに変換
result = ''.join(word_lengths_str) #',[]を削除し、リストを連結
print(result)