'''
将数据导出为 csv 文件
'''

import os

def exportdata(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write("ID,Score\n")  # 添加表头
        for id, score in data.items():
            f.write(f"{id},{score}\n")
