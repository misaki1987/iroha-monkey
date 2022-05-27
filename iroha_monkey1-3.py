import random

#文字リストの生成
chara = ["い","ろ","は","に","ほ","へ","と","ち","り","ぬ","る","を",
"わ","か","よ","た","れ","そ","つ","ね","な","ら","む",
"う","ゐ","の","お","く","や","ま","け","ふ","こ","え","て",
"あ","さ","き","ゆ","め","み","し","ゑ","ひ","も","せ","す"]

#正しいいろは歌を作る
iroha = "いろはに"

#カウンターに０をセット
counter = 0

#文章作成関数を定義
def make_iroha() :
    list = []
    for i in range(0,4):
        x = random.choice(chara)
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


