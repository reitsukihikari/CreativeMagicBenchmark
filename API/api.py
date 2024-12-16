from .gpt_api import gpt4omini
## 调用大语言模型
def api(prompt):
    return gpt4omini(prompt)

if __name__ == "__main__":
    print(api("Hello, world!"))