''' 
一个魔术方案的表演者评分
'''

import json
from Util.fP import fP
from Util.gettech import get_techs
from Util.checkequal import check_equal
import configparser

config = configparser.ConfigParser()
config.read('Config/config.cfg')

api_calls = int(config['DEFAULT']['api_calls'])
tech_path = config['DEFAULT']['tech_path']

def scoreP_convergence(prompt):
    scores = [fP(prompt) for _ in range(api_calls)] 
    score = sum(scores) / len(scores)
    print(f"\t\t\tscoreP:")
    print(f"\t\t\t\tconvergence: {score:.2f}")
    return score

def scoreP_divergence(prompt):
    scores = []
    for _ in range(api_calls):
        techs_from_gettech = get_techs(prompt)["Techs"]
        with open(tech_path, 'r') as f:
            predefined_techs = json.load(f)["Techs"]
        difference = [
            t for t in techs_from_gettech 
            if not any(
                check_equal(
                    t["Name"], t["Description"],
                    predefined["Name"], predefined["Description"]
                ) for predefined in predefined_techs
            )
        ]
        total_techs = len(techs_from_gettech)
        scores.append(len(difference) / total_techs if total_techs > 0 else 0)
    score = sum(scores) / len(scores)
    print(f"\t\t\t\tdivergence: {score:.2f}")
    return score

def scoreP(prompt):
    return scoreP_convergence(prompt) * scoreP_divergence(prompt)

if __name__ == "__main__":
    print(scoreP("Hello, world!"))