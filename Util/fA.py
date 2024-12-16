'''
观众收敛性
'''

from API.api import api

def fA(prompt):
    response = api(f"""Estimate if Magics.Schemes.Audience has the audience's perspective of ornamental value, output float, normalized to 0 to 1. MUST ONLY output float, do not output any other text.""")
    return float(response)

if __name__ == "__main__":
    print(fA("Hello, world!"))