''' 
加载数据
'''

import json

def loaddata(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
