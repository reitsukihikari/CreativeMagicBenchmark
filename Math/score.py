'''
一个魔术方案的综合得分
'''

from Math.scoreS import scoreS
from Math.scoreA import scoreA
from Math.scoreP import scoreP
import configparser

config = configparser.ConfigParser()
config.read('Config/config.cfg')

alpha = float(config['DEFAULT']['alpha'])
beta = float(config['DEFAULT']['beta'])
gamma = float(config['DEFAULT']['gamma'])   

def score(text):
    return alpha * scoreS(text) + beta * scoreA(text) + gamma * scoreP(text)

if __name__ == "__main__":
    print(score("Hello, world!"))