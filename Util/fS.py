'''
出题人收敛性
'''

from API.api import api

def fS(prompt):
    response = api(f"""Estimate if Magics.Schemes.Setter contains Magics.Settings.Location and Magics.Settings.Objects, output float, normalized to 0 to 1. MUST ONLY output float, do not output any other text.""")
    return float(response)

if __name__ == "__main__":
    print(fS("Hello, world!"))