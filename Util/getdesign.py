''' 
调用 API 获取一个魔术方案的出题人视角的设计思路
'''

from API.api import api
import json

def get_designs(prompt):
    response = api(f"""Reference the following example:
               ```json
               {{
                   "Designs":[
                       {{
                           "Name": "Misdirection",
                           "Description": "Directing audience focus through language, actions, or visuals to conceal key moves on a macro level."
                       }},
                       {{
                           "Name": "Psychological Suggestion",
                           "Description": "Using verbal and nonverbal cues to influence audience thoughts and choices from an overall strategic perspective."
                       }},
                       {{
                           "Name": "Storytelling",
                           "Description": "Structuring the performance with a compelling narrative to maintain engagement and unify the show on a grand scale."
                       }},
                       {{
                           "Name": "Interactive Guidance",
                           "Description": "Steering audience participation as planned, shaping the experience from a high-level viewpoint."
                       }}
                   ]
               }}
               ```
               MUST extract design ideas BUT no more than 3 from the Magic.Schemes.Setter, MUST ONLY output json, MUST ONLY name and description, use "Designs" as the key: {prompt}""")

    response = response.replace("```json", "").replace("```", "")
    # print(response)
    json_start = response.index('{')
    json_str = response[json_start:]
    designs = json.loads(json_str)
    return designs

if __name__ == "__main__":
    print(get_designs("Hello, world!"))