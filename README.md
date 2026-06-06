# Python00 学習ログ

## 概要

この課題では、Pythonの基本文法を使って、関数・標準出力・標準入力・型変換・条件分岐を学習する。

## 共通ルール

* 各課題は `ex0`, `ex1`, `ex2` のように別フォルダで管理する
* 各ファイルには指定された関数だけを書く
* `if __name__ == "__main__":` は書かない
* 関数を直接呼び出すコードは書かない
* 出力文字列はPDFの指定と完全一致させる
* Pythonではインデントが文法として重要

---

## ex0: ft_hello_garden

### 学んだこと

Pythonでは、画面に文字を表示するために `print()` を使う。

```python
def ft_hello_garden():
    print("Hello, Garden Community!")
```

C言語の `printf()` はPythonの標準関数ではない。

### 注意点

* `printf()` ではなく `print()` を使う
* `print()` はデフォルトで最後に改行する
* 課題では関数だけを書く
* 出力文字列を指定と完全一致させる

---

## ex1: ft_garden_name

### 学んだこと

`input()` を使うと、ユーザーから文字列を受け取ることができる。

```python
garden_name = input("Enter garden name: ")
```

`input()` の戻り値は常に文字列になる。

```python
def ft_garden_name():
    garden_name = input("Enter garden name: ")
    print(f"Garden: {garden_name}")
    print("Status: Growing well!")
```

### 注意点

* `str` という変数名は使わない
* `str` はPythonの組み込み型
* `input()` の表示文字列では、コロンの後のスペースも重要
* Pythonではインデントを揃える
* 固定メッセージは毎回同じ内容を表示する

---

## ex2: ft_plot_area

### 学んだこと

`input()` の戻り値は文字列なので、数値計算をする場合は `int()` で整数に変換する。

```python
length = int(input("Enter length: "))
width = int(input("Enter width: "))
```

長方形の面積は、縦と横を掛け算して求める。

```python
area = length * width
```

```python
def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f"Plot area: {area}")
```

### 注意点

* `input()` は常に文字列を返す
* 数値計算をする前に `int()` で変換する
* `=` の前後はスペース1つにする
* 計算結果は意味のある変数名に入れると読みやすい
* `area` のように目的が分かる変数名を使う

---

## ex3: ft_harvest_total

### 学んだこと

複数の入力値を受け取り、それぞれを整数に変換して合計できる。

```python
day1 = int(input("Day 1 harvest: "))
day2 = int(input("Day 2 harvest: "))
day3 = int(input("Day 3 harvest: "))
```

複数の数値の合計には `+` を使う。

```python
total_harvest = day1 + day2 + day3
```

```python
def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total_harvest = day1 + day2 + day3
    print(f"Total harvest: {total_harvest}")
```

### 注意点

* `input()` に表示するメッセージは文字列なので、クォートで囲む
* `input("Day 1 harvest: ")` のように書く
* `input(Day 1 harvest: )` は文法エラーになる
* Pythonではインデントを揃える
* `+` の前後にはスペースを入れる
* `total_harvest` のように意味が明確な変数名を使う

---

## ex4: ft_plant_age

### 学んだこと

`if` 文を使うと、条件によって処理を分岐できる。

```python
if age > 60:
    print("Plant is ready to harvest!")
else:
    print("Plant needs more time to grow.")
```

`>` は「より大きい」を表す。

```python
def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
```

### 注意点

* `strictly more than 60` は `age > 60` と書く
* `age >= 60` ではない
* `>= 60` にすると、60日ちょうどでも条件を満たしてしまう
* `else` は条件に当てはまらなかった場合の処理を書く
* Pythonでは `if` と `else` の中身をインデントする

---

## ex5: ft_water_reminder

### 学んだこと

`if` 文を使って、入力された日数に応じて出力を変えられる。

```python
if days > 2:
    print("Water the plants!")
else:
    print("Plants are fine")
```

```python
def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
```

### 注意点

* `more than 2 days` は `days > 2` と書く
* `days >= 2` ではない
* 出力文字列は指定と完全一致させる
* `input()` の戻り値は文字列なので、`int()` で変換する
* `day` より `days` の方が複数日を表していて自然

---

## ここまでで学んだPythonの基礎

### print()

画面に文字列を表示する。

```python
print("Hello")
```

### input()

ユーザーから入力を受け取る。

```python
name = input("Name: ")
```

### int()

文字列を整数に変換する。

```python
age = int(input("Age: "))
```

### f-string

変数の値を文字列の中に埋め込む。

```python
print(f"Garden: {garden_name}")
```

### if / else

条件によって処理を分ける。

```python
if age > 60:
    print("Ready")
else:
    print("Not ready")
```

### インデント

Pythonでは `{}` ではなく、インデントでブロックを表す。

```python
if age > 60:
    print("Ready")
```

---

## 現時点で特に注意すること

* C言語の `printf()` ではなくPythonの `print()` を使う
* `input()` の戻り値は文字列
* 数値計算をする前に `int()` で変換する
* Pythonの組み込み名を変数名にしない

  * 例: `str`, `int`, `list`, `dict`
* インデントを必ず揃える
* 演算子の前後にはスペースを入れる
* 課題文の条件を正確に読む

  * `more than` は `>`
  * `at least` なら `>=`
* 出力文字列はスペースや記号も含めて完全一致させる

## ex6: ft_count_harvest_iterative / ft_count_harvest_recursive

### 学んだこと

`while` 文を使うと、条件が成り立っている間、同じ処理を繰り返せる。

```python
day = 1

while day <= days:
    print(f"Day {day}")
    day += 1
```

再帰では、関数が自分自身を呼び出す。

```python
def print_harvest_days(day):
    if day > 1:
        print_harvest_days(day - 1)
    print(f"Day {day}")
```

`print_harvest_days(5)` の場合、先に `print_harvest_days(1)` まで進み、その後戻りながら `Day 1` から `Day 5` まで表示される。

### 実装

#### 反復版

```python
def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    day = 1
    while day <= days:
        print(f"Day {day}")
        day += 1
    print("Harvest time!")
```

#### 再帰版

```python
def print_harvest_days(day):
    if day > 1:
        print_harvest_days(day - 1)
    print(f"Day {day}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    print_harvest_days(days)
    print("Harvest time!")
```

### 注意点

- 再帰呼び出しでは、定義した関数名と同じ名前を呼び出す
- `print_days()` のような未定義の関数を呼ぶと `NameError` になる
- Pythonでは `day++` は使えない
- インクリメントは `day += 1` と書く
- `while day <= days:` のように終了条件を明確に書く
- 再帰には終了条件が必要
- 今回は `if day > 1:` が終了条件になる
- Pythonではインデントをスペース4つで揃える

## ex7: 型ヒントと mypy

### 学んだこと

Pythonでは、関数の引数や戻り値に型ヒントを書ける。

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```

それぞれの意味は以下の通り。

- `seed_type: str` は、`seed_type` が文字列であることを表す
- `quantity: int` は、`quantity` が整数であることを表す
- `unit: str` は、`unit` が文字列であることを表す
- `-> None` は、関数が値を返さないことを表す

### mypy

`mypy` は、Pythonの型ヒントをチェックするための静的型チェックツール。

```bash
mypy ft_seed_inventory.py
```

型に問題がなければ、以下のような結果になる。

```text
Success: no issues found in 1 source file
```

### 注意点

- 型ヒントを書いても、Pythonの実行時に型が強制されるわけではない
- 型チェックには `mypy` を使う
- ex7では型ヒントが必須
- `-> None` の関数では、基本的に値を `return` しない
- `print()` するだけの関数は戻り値が `None`

## ex7: ft_seed_inventory

### 学んだこと

ex7では、型ヒントを必ず使う。

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```

それぞれの意味は以下の通り。

- `seed_type: str` は、種の種類が文字列であることを表す
- `quantity: int` は、数量が整数であることを表す
- `unit: str` は、単位が文字列であることを表す
- `-> None` は、関数が値を返さないことを表す

Pythonでは、複数の条件分岐に `elif` を使う。

```python
if unit == "packets":
    ...
elif unit == "grams":
    ...
elif unit == "area":
    ...
else:
    ...
```

### 実装

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
```

### 注意点

- ex7では型ヒントが必須
- `-> None` は戻り値がないことを表す
- Pythonでは `else if` ではなく `elif` を使う
- `print()` は呼び出すたびに改行される
- 期待出力が1行なら、1回の `print()` で出力する
- `"packets"`, `"grams"`, `"area"` 以外の場合は `Unknown unit type` のみを表示する
- 未知の単位では、種の名前や数量は表示しない
- `seed_type.capitalize()` で先頭文字を大文字にできる
- `mypy ft_seed_inventory.py` で型チェックする
