def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    temp=int(input("Please input temperature:"))
    unit=input("Please input unit:")
    unit_f="f"
    unit_c="c"
    if(unit==unit_f):
        unit="c"
        temp= (temp-32)*5/9
        temp=int(temp)
        print(str(temp) + unit)
    elif (unit==unit_c):
        unit="f"
        temp= temp*9/5+32
        temp=int(temp)
        print(str(temp) + unit)
    else:
        print("Error - Please input f or c for unit.")


    return temp


convert()
