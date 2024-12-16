'''
表演者收敛性
'''

from API.api import api

def fP(prompt):
    response = api(f"""Estimate if Magics.Schemes.Performer is proper for the performer's perspective of the performance difficulty, output float, normalized to 0 to 1. MUST ONLY output float, do not output any other text.""")
    return float(response)

if __name__ == "__main__":
    print(fP("Hello, world!"))