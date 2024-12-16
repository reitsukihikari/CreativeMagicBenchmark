'''
一个魔术方案的观众评分
'''

import json
from Util.fA import fA
from Util.getview import get_views
from Util.checkequal import check_equal
import configparser

config = configparser.ConfigParser()
config.read('Config/config.cfg')

api_calls = int(config['DEFAULT']['api_calls'])
view_path = config['DEFAULT']['view_path']

def scoreA_convergence(prompt):
    scores = [fA(prompt) for _ in range(api_calls)]
    score = sum(scores) / len(scores)
    print(f"\t\t\tscoreA:")
    print(f"\t\t\t\tconvergence: {score:.2f}")
    return score

def scoreA_divergence(prompt):
    scores = []
    for _ in range(api_calls):
        views_from_getview = get_views(prompt)["Views"]
        with open(view_path, 'r') as f:
            predefined_views = json.load(f)["Views"]
        difference = [
            v for v in views_from_getview 
            if not any(
                check_equal(
                    v["Name"], v["Description"],
                    predefined["Name"], predefined["Description"]
                ) for predefined in predefined_views
            )
        ]
        total_views = len(views_from_getview)
        scores.append(len(difference) / total_views if total_views > 0 else 0)
    score = sum(scores) / len(scores)
    print(f"\t\t\t\tdivergence: {score:.2f}")
    return score

def scoreA(prompt):
    return scoreA_convergence(prompt) * scoreA_divergence(prompt)

if __name__ == "__main__":
    print(f"{scoreA('Hello, world!'):.2f}")