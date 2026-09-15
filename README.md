# textkit

Small text and list helpers.

```python
from textkit import chunk, parse_duration, slugify

chunk([1, 2, 3, 4], 2)          # [[1, 2], [3, 4]]
slugify("hello")                # "hello"
parse_duration("1h30m")         # 5400
```
