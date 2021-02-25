import random  # 生成隨機數


def major():
    print("Keep it logically awesome.")

    f = open("quotes.txt")  # 讀檔案
    quotes = f.readlines()
    f.close()

    last = len(quotes-1)  # 自動更新最後一列資料的index，這樣可以在文件中新增/刪除行數
    ran = random.randint(0, last)
    print(quotes[ran])


if __name__ == "__main__":
    major()
