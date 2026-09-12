# 🚀 Python OA 關鍵資料結構與語法筆記

## 🧱 堆疊與佇列 (Stack & Queue)
```python
from collections import deque

# 初始化
q = deque()          # 空佇列/堆疊
q = deque(nums)      # 帶入現有 list (OA 推薦！效能好)

# Stack (FILO 先進後出)
q.append(x)          # 推入頂端
q.pop()              # 彈出頂端

# Queue (FIFO 先進先出)
q.append(x)          # 從尾端加入
q.popleft()          # 從前端取出 (O(1) 關鍵！勿用 list.pop(0))
```

## 🎛️ 條件分支 (Case When)
### Python 3.10+ (Match-Case)
```python
match x:
    case 1:
    case 2 | 3:      # OR 條件
    case 4 if expr:  # Guard 條件
    case _:          # Default (Else)
```


## 🎯 經典題型避坑 (以 Valid Parentheses 為例)
```python
# 1. 字典配對防呆 (右括號 -> 左括號)
mapping = {"}": "{", "]": "[", ")": "("}

# 2. 防空邊界
if not stack:        # 必先檢查，防止 pop 空結構噴 Error

# 3. 結尾檢查
return len(stack) == 0  # 確保完全配對清空
```
