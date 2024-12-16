import openai
import json
import os
from openai import OpenAI
  
# 获取当前脚本的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 构建apikey.json的绝对路径
apikey_path = os.path.join(current_dir, "apikey.json")

# 加载API密钥
with open(apikey_path, "r") as f:
    apikey = json.load(f)["gpt4omini_apikey"]

client = OpenAI(api_key=apikey)

## 调用gpt-4o-mini模型
def gpt4omini(prompt):
    """
    调用 gpt-4o-mini 模型生成响应。

    参数：
    - prompt (str): 输入的提示文本。
    - api_key (str): 您的 OpenAI API 密钥。

    返回：
    - response_text (str): 模型生成的响应文本。
    """
    try:
        # 设置 API 密钥

        # 调用 ChatCompletion 接口
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # 根据需要调整
            temperature=0.7  # 控制创造性，范围 0-1
        )

        # 提取响应文本
        response_text = response.choices[0].message.content.strip()
        return response_text

    except openai.OpenAIError as e:
        # 处理 OpenAI API 错误
        print(f"OpenAI API 错误: {e}")
        return None
    except Exception as e:
        # 处理其他可能的错误
        print(f"发生错误: {e}")
        return None

if __name__ == "__main__":

    user_prompt = "请简要介绍一下机器学习的基本概念。"
    response = gpt4omini(user_prompt)

    if response:
        print("模型响应:")
        print(response)
    else:
        print("未能获取模型响应。")