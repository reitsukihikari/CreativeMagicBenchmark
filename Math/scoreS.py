''' 
一个魔术方案的出题人评分
'''

import json
from Util.fS import fS
from Util.getdesign import get_designs
from Util.checkequal import check_equal
import configparser

config = configparser.ConfigParser()
config.read('Config/config.cfg')

api_calls = int(config['DEFAULT']['api_calls'])
design_path = config['DEFAULT']['design_path']
def scoreS_convergence(prompt):
    scores = [fS(prompt) for _ in range(api_calls)]
    score = sum(scores) / len(scores)
    print(f"\t\t\tscoreS:")
    print(f"\t\t\t\tconvergence: {score:.2f}")
    return score

def scoreS_divergence(prompt):
    scores = []
    for _ in range(api_calls):
        designs_from_getdesign = get_designs(prompt)["Designs"]
        with open(design_path, 'r') as f:
            predefined_designs = json.load(f)["Designs"]
        difference = [
            d for d in designs_from_getdesign 
            if not any(
                check_equal(
                    d["Name"], d["Description"],
                    predefined["Name"], predefined["Description"]
                ) for predefined in predefined_designs
            )
        ]
        total_designs = len(designs_from_getdesign)
        scores.append(len(difference) / total_designs if total_designs > 0 else 0)
    score = sum(scores) / len(scores)
    print(f"\t\t\t\tdivergence: {score:.2f}")
    return score

def scoreS(prompt):
    return scoreS_convergence(prompt) * scoreS_divergence(prompt)

if __name__ == "__main__":
    print(scoreS("Hello, world!"))