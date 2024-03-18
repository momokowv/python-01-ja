import os
from collections import defaultdict


def ls_command(directory):
    # ユーザー入力が「sample」の場合、ディレクトリは「sample」になります
    # 無効なディレクトリパスについて考える必要はありません

    # 「pass」を削除して、ここにコードを書いてください
    
    files = os.listdir(str(directory))
    file_dict = defaultdict(list)

    for x in files:
         if os.path.isfile(os.path.join(directory, x)):
             _, ext = os.path.splitext(x)
             file_dict[ext].append(x)

    for ext, file_list in sorted(file_dict.items()):
        print(f"{ext}: {len(file_list)} file{'s' if len(file_list) != 1 else ''}")


if __name__ == "__main__":
    directory_path = input("Enter directory path to organize files: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        ls_command(directory_path)
