import random

#文字リストの生成
chara = ["い","ろ","は","に","ほ","へ","と","ち","り"]

#正しいいろは歌を作る
iroha = "".join(chara)

#カウンターに０をセット
counter = 0

#文章作成関数を定義
def make_iroha() :
    list = []
    while len(list) < len(chara):
        x = random.choice(chara)
        if not x in list:
            list.append(x)
    
    sentence = "".join(list)
    return sentence

#正解の文字列ができるまで文章を生成し続ける
while True:
    result = make_iroha()
    counter = counter + 1
    #結果の出力
    print("試行回数"+str(counter)+"回目")
    print("今回の結果は、"+"「"+ result + "」")
    print("monkeys keep trying...")

    #正解が見つかったら繰り返しから抜ける
    if result == iroha:
        break

#結果の出力
print("!!!!!!!!!!!!!!!")
print("monkeys found it!")


