# 💡 字串演算法必備：邊界條件與效能優化速查筆記

## 1. 256 Valid ASCII Constraints (256 個有效字元限制)
當題目限制字串包含 256 個 ASCII 字元時，代表輸入**不侷限於英文字母或數字**。

### 📌 內含範圍
*   **標準字元 (0-127)**：英文字母、數字、常見標點符號（如 `, . ! # $ % ^ & * ( )`）、空格、換行符號（`\n`）、Tab（`\t`）。
*   **擴充字元 (128-255)**：歐洲變音字母（`é`, `ü`）、數學符號（`±`, `×`）、貨幣符號（`£`, `¥`）。
*   ⚠️ **注意**：中文與 Emoji 不在 256 範圍內（屬於 UTF-8）。

### 🛠️ 程式避坑指南
*   **拒絕減去 `'a'`**：絕對不要用 `s[i] - 'a'` 當作陣列索引（標點符號會減出負數導致程式崩潰）。
*   **C++ 陣列越界防範**：C++ 的 `char` 是有號數（Signed），遇到 128-255 的字元會變成負數。統計時必須轉為 `unsigned char`：
    ```cpp
    int count[256] = {0};
    unsigned char idx = static_cast<unsigned char>(s[i]);
    count[idx]++;
    ```

---

## 2. Python Slicing (切片語法)
語法格式：`s[start:stop:step]` （註：即你提到的 `s[start:first:1]`）

### 📌 參數核心意義
*   **`start`**：開始索引（**包含**）。
*   **`stop`**（或 `first`）：結束索引（⚠️ **不包含**）。
*   **`step`**：步長。若為 `1` 代表連續取值。因為預設即為 `1`，所以 `s[start:stop:1]` 等同於 `s[start:stop]`。

### ⚡ 常用花式切片
*   `s[:5]`：切出前 5 個字元（索引 0 到 4）。
*   `s[3:]`：從索引 3 一路切到字串末尾。
*   `s[::-1]`：**字串反轉**（步長為 -1，倒著走）。

---

## 3. 字串拼接 vs. 列表 追加 (效能大車拼)
這是在 LeetCode 中決定程式會不會 **TLE (超時)** 的關鍵。

### ❌ 寫法一：字串直接加總 (`res = res + s`)
*   **原理**：Python 的字串是不可變的（Immutable）。每次相加，記憶體都要**重新開闢空間並完整複製舊字串**。
*   **時間複雜度**：迴圈跑 N 次總共需要 **O(N²)**。字串越長，速度越慢。

###  寫法二：列表追加後合併 (`res.append(s)`)
*   **原理**：Python 的列表是可變的（Mutable）。`.append()` 是在記憶體原地追加，不需要複製。
*   **時間複雜度**：單次 **O(1)**，迴圈跑 N 次總共只需 **O(N)**。

### 🏆 演算法最佳實踐 (Best Practice)
先用 `list` 高效收集，最後用 `"".join()` 一口氣轉回字串：
```python
res_list = []
for s in strs:
    res_list.append(str(len(s)))
    res_list.append("#")
    res_list.append(s)

# O(N) 高效組裝
final_str = "".join(res_list)
```

## 2. 雙指標命名與核心心法 (Two Pointers)
演算法的最佳解常出現 `i`, `j`，但實務或面試中，使用**具備語意的命名**更能展現工程師的軟體美學。雙指標主要分為兩大派系：

### 派系 A：快慢指標 / 探路指標 (本題核心 💡)
*   **慢指標 (`slow` / `lag`)**：定在原地，通常代表「當前處理區段的起點」。
*   **快指標 (`fast` / `lead`)**：負責往前衝、探路、尋找特定終止條件（如這題要找 `#` 號）。
*   🎯 **解碼 (Decode) 核心心法**：
    > **「用快指標找到關鍵字元，算出長度後，直接用 Slicing 把整段字串吃掉，然後把慢指標瞬移過去。」**

### 派系 B：左右邊界指標 (區間型題目)
*   **左指標 (`left` / `l`)**：區間的左端點。
*   **右指標 (`right` / `r`)**：區間的右端點。
*   **常見場景**：二分搜尋法（Binary Search）、滑動視窗（Sliding Window）、回文字串檢查。

---

## 3. 手工指標 vs 內建 `.find()` 抉擇
在面試中，使用 `s.find()` **絕對不是作弊**，反而能展現 Production-Ready 的實務思維，因為內建函式底層是 C 語言優化，效能更好。

但若想追求「不產生額外子字串」的完美空間複雜度，**純手工雙指標**是極致的寫法。

### 🏆 兩種 Decode 解法對比

#### 作法一：使用內建 `.find()` (簡潔、高效)
```python
def decode(self, s: str) -> List[str]:
    res = []
    slow = 0
    while slow < len(s):
        # 尋找 slow 之後的第一個 '#'
        fast = s.find('#', slow)
        length = int(s[slow:fast])
        
        # 根據長度切片文字，並將 slow 瞬移到下一段起點
        word_start = fast + 1
        word_end = word_start + length
        res.append(s[word_start:word_end])
        slow = word_end
    return res
```

#### 作法二：純手工 `while` 雙指標 (極致空間複雜度，不切片探路)
```python
def decode(self, s: str) -> List[str]:
    res = []
    slow = 0
    while slow < len(s):
        fast = slow
        # 純手工指標往前探路，直到撞到 '#'
        while s[fast] != '#':
            fast += 1
            
        length = int(s[slow:fast])
        word_start = fast + 1
        word_end = word_start + length
        res.append(s[word_start:word_end])
        
        # 慢指標瞬移
        slow = word_end
    return res
```