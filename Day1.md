# Python00 学習ログ

## 学習内容

### print()

画面へ文字を表示する関数。

```python
print("Hello World")
```

### input()

ユーザーから入力を受け取る関数。

```python
name = input("Name: ")
```

### int()

文字列を整数へ変換する。

```python
age = int(input("Age: "))
```

### if文

条件によって処理を分岐する。

```python
if age > 18:
    print("Adult")
```

### while文

条件が真の間繰り返す。

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### 型ヒント

変数や関数の型を明示する。

```python
def add(a: int, b: int) -> int:
    return a + b
```

## 学び

* Pythonはインデントが重要
* snake_caseで命名する
* 関数は1つの責務を持たせる
* 読みやすさを優先する

## 次回レビュー時の確認事項

* 不要な変数がないか
* 命名が適切か
* Pythonらしく書けているか
* flake8を通るか
