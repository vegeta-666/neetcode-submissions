# 💡 Python Class & MinStack 複習筆記

## 1. Python `__init__` 的核心作用
* **它是什麼**：類別的**初始化方法**（建構子）。當你建立物件實例（如 `minStack = MinStack()`）時，Python 會**自動呼叫**它。
* **主要任務**：
  1. 接收外部傳入的參數。
  2. **建立並綁定屬性**：在內部使用 `self.變數名稱 = ...`，概念就像是「新創造一個該物件專屬的變數」，讓物件內的所有方法都能共用它。

---

## 2. LeetCode 155. Min Stack 關鍵設計

### 為什麼 `__init__` 要初始化「兩個」List？
```python
def __init__(self):
    self.stack = []      # 主 Stack：放所有資料
    self.min_stack = []  # 輔助 Stack：同步記錄「目前為止的歷史最小值」
```

### 🧠 常犯盲點：為什麼 `min_stack` 不能直接用一個 `int` 紀錄？
* **答案：因為 `int` 沒有「歷史記憶」！**
* **災難情境**：如果依序 `push(5)` ➔ `push(3)`，此時最小值 `int` 是 `3`。但當我們執行 `pop()` 拿掉 `3` 之後，最小值應該要變回 `5`。
* **List 的優勢（時光機效應）**：如果用輔助 Stack，拿掉 `3` 的同時，`min_stack` 也跟著 `pop()`，頂端就會自然浮現出之前的最小值 `5`。這樣就能在 **\(O(1)\) 常數時間**內取得最小值，不用重新用迴圈尋找。

---

## 3. 防禦性程式設計（Defensive Programming）

### 為什麼在 `top()` 或 `pop()` 要先判斷 `if self.stack:`？
```python
def top(self) -> int:
    if self.stack:
        return self.stack[-1]
```
* **防止程式崩潰**：在 Python 中，`[-1]` 代表抓取 List 的最後一個元素。
* **避免錯誤**：如果 Stack 是空的（`[]`），強行呼叫 `self.stack[-1]` 會引發 `IndexError: list index out of range`。加上 `if self.stack:` 檢查能確保只有在「袋子裡有東西」時才操作，避免程式當機。
