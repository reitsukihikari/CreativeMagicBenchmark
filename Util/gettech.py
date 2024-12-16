''' 
调用 API 获取一个魔术方案的表演者视角的手法
'''

from API.api import api
import json

def get_techs(prompt):
    response = api(f"""Reference the following example:
               ```json
               {{
                   "Techs":[
                       {{
                           "Name": "Palming",
                           "Description": "Concealing or switching objects unnoticed through refined hand techniques."
                       }},
                       {{
                           "Name": "Manual Control",
                           "Description": "Employing skilled, rapid hand maneuvers to render object movements untraceable."
                       }},
                       {{
                           "Name": "Props Usage",
                           "Description": "Designing and using specialized props to enhance effects at a detailed scale."
                       }},
                       {{
                           "Name": "Visual Illusions",
                           "Description": "Utilizing light, mirrors, or similar methods to create deceptive appearances."
                       }},
                   ]
               }}
               ```
               MUST extract techniques BUT no more than 3 from the Magic.Schemes.Performer, MUST ONLY output json, MUST ONLY name and description, use "Techs" as the key: {prompt}""")

    response = response.replace("```json", "").replace("```", "")
    # print(response)
    json_start = response.index('{')
    json_str = response[json_start:]
    techs = json.loads(json_str)
    return techs

if __name__ == "__main__":
    print(get_techs("Hello, world!"))