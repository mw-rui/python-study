### 検索ツール
import sys

# 検索ソース
CSV_PATH = "source.csv"

# CSV読み込み
def read_csv(path):
    try:
        with open(path, "r", encoding="utf_8", newline='') as fr:
            return fr.read().splitlines()

    except:
        print("csvを読み込めません")
        print("ファイルパスを確認してください")
        sys.exit()

# CSV書き出し
def write_csv(path, data):
    try:
        with open(path, "w", newline='', encoding="utf_8") as fw:
            fw.write("\n".join(data))
    except:
        print("csvが書き込めません")
        print("ファイルパスを確認してください")
        sys.exit()
        
### 検索ツール
def search():
    source = read_csv(CSV_PATH)

    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    
    if word in source:
        print(f"{word}が見つかりました")
    else:
        print(f"{word}が見つかりません")
        while (1):
            is_regist = input(f"{word}を登録しますかy/n >>> ")
            if is_regist == "y":
                source.append(word)
                write_csv(CSV_PATH, source)
                print(f"{word}を登録しました")
                break
            elif is_regist == "n":
                break
            else:
                print("y/nを入力してください")

if __name__ == "__main__":
    search()