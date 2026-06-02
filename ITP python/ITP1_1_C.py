#長方形の縦と横の長さを受け取って、面積と週の長さを出力する。

a,b=map(int,input().split())
print(a*b,2*(a+b))

#mapでint型を一斉に適応。
#splitで二つの値を別の数として認識させている。
