'''
将json文件中的image字段提取的图片中对象添加到objects字段
'''

from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
import threading

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = None
load_lock = threading.Lock()

def load_model():
    global model
    with load_lock:
        if model is None:
            model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    return model

def vqa(image_path):
    if image_path == "":
        return []
    image = Image.open(image_path)
    text = "What is in the image?"
    encoding = processor(image, text, return_tensors="pt")
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    answer = model.config.id2label[idx]
    # print(answer)
    return answer

def img2obj(dataset):
    load_model()
    for magic in dataset['Magics']:
        objects = vqa(magic['Setting']['Imagepath'])
        magic['Setting']['Objects'] += f", {objects}"
    return dataset