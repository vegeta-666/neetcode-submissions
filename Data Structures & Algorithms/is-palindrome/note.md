# Note

1. chr()
2. ord()
3. 判斷是否為字母或數字
  - 'a'.isalnum())
  - create 一個 set 來判斷
4. 判斷大小寫
  - 'a'.lower()
  - 自己寫 function, 大小寫差 32
  - ord('A') 是 65，ord('a') 是 97。 97 - 65 = 32。
  ```
def my_lower(s: str) -> str:
    result = []
    for char in s:
        # 判斷字元是否在大寫字母 'A' 到 'Z' 的編碼範圍內 (65 ~ 90)
        if 65 <= ord(char) <= 90:
            # 加上 32 轉換為小寫編碼，再用 chr() 轉回字元
            lower_char = chr(ord(char) + 32)
            result.append(lower_char)
        else:
            # 如果不是大寫英文字母（如數字、符號、小寫、中文），保持原樣
            result.append(char)
            
    # 將字元列表合併回字串
    return "".join(result)

# 測試
test_str = "Hello, World! 123 測試"
print(my_lower(test_str))  # 輸出: hello, world! 123 測試

  ```
5. left, right pointer