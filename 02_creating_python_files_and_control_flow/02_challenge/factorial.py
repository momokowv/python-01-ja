def compute_factorial():
    # ここにコードを書いてください
    # number変数を編集し、ユーザー入力として正の整数を受け取ります。整数に変換することを忘れないでください
    number = int(input("Please input number:"))
    if (number < 0):
        number = number * (-1)

    # result変数を編集し、最終的な計算結果を保存します
    result = 1
    while (number >= 1):
        result = result * number
        number = number - 1
    print(result)

    return result


compute_factorial()
