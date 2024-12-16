''' 
调用 API 获取一个魔术方案的观众视角看到的效果
'''

from API.api import api
import json

def get_views(prompt):
    response = api(f"""Reference the following example:
               ```json
               {{
                   "Views":[
                       {{
                           "Name": "Smooth and Natural Movements",
                           "Description": "The performer's hands and gestures appear completely natural, never hinting at hidden maneuvers."
                       }},
                       {{
                           "Name": "Captivating Narrative",
                           "Description": "The show unfolds like a mesmerizing story, making each effect feel like a natural part of the performance."
                       }},
                       {{
                           "Name": "Inviting Participation",
                           "Description": "Audience members who are chosen to assist feel genuinely involved, never suspecting any hidden tactics."
                       }},
                       {{
                           "Name": "Astonishing Visual Effects",
                           "Description": "Objects seem to appear from nowhere, vanish into thin air, or transform instantly—no logical explanation is apparent."
                       }},
                   ]
               }}
               ```
               MUST extract visual effects BUT no more than 3 from the Magic.Schemes.Audience, MUST ONLY output json, MUST ONLY name and description, use "Views" as the key: {prompt}""")

    response = response.replace("```json", "").replace("```", "")
    # print(response)
    json_start = response.index('{')
    json_str = response[json_start:]
    views = json.loads(json_str)
    return views

if __name__ == "__main__":
    print(get_views("Hello, world!"))