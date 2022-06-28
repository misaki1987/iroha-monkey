import random

#文字リストの生成
chara = [
    "い","ろ","は","に","ほ","へ","と","ち","り","ぬ","る","を","わ","か","よ",
    "た","れ","そ","つ","ね","な","ら","む","う","ゐ","の","お","く","や","ま",
    "け","ふ","こ","え","て","あ","さ","き","ゆ","め","み","し","ゑ","ひ","も",
    "せ","す"
]

#カウンターに０をセット
counter = 0

#文章作成関数を定義。今回は初期の文章作成のみに使う。
def make_iroha() :
    list = []
    while len(list) < len(chara):
        x = random.choice(chara)
        list.append(x)
    return list

#フィードバックのしくみを作る
def fitness(chara,list):
    #２つのリストを比較して、一致する数をフィードバックする
    grade = 0
    for i ,j in zip(chara,list):
        if i == j :
            grade = grade + 1
    return grade

#初期の文章を作る
result = make_iroha()
sentence = "".join(result)
counter = counter + 1
print("試行回数"+str(counter)+"回目")
print("今回の結果は、"+"「"+ sentence + "」")
print("monkeys keep trying...")

#いったん初期の文章を最高評価のものとして保存する。
best_hits = result
best_hits_grade = fitness(chara,best_hits)

#正解の文字列ができるまで文章を修正し続ける
while best_hits != chara :
    #best_hitsをコピーする
    next_ans = best_hits[:]
    #修正する位置3カ所を重複ありでランダムに選択
    point = random.randrange(0,len(next_ans))
    point2 = random.randrange(0,len(next_ans))
    point3 = random.randrange(0,len(next_ans))
    #修正する位置をランダムな文字で置き換える
    next_ans[point] = random.choice(chara)
    next_ans[point2] = random.choice(chara)
    next_ans[point3] = random.choice(chara)
    #置き換えた結果を評価する
    next_ans_grade = fitness(chara,next_ans)
    #前のものよりも評価が高ければ最高評価のものとして保存する
    if next_ans_grade > best_hits_grade:
        best_hits = next_ans[:]
        best_hits_grade = next_ans_grade
    counter = counter + 1
    #結果を文章化
    result = "".join(next_ans)
    #結果の出力
    print("試行回数"+str(counter)+"回目")
    print("今回の結果は、"+"「"+ result + "」")
    print("monkeys keep trying...")

#結果の出力
print("!!!!!!!!!!!!!!!")
print("monkeys found it!")
