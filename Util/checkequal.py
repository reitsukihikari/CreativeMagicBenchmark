'''
检查两个文本是否近义
'''

import spacy
import configparser

config = configparser.ConfigParser()
config.read('Config/config.cfg')

name_weight = float(config['DEFAULT']['name_weight'])
description_weight = float(config['DEFAULT']['description_weight'])
synonym_threshold = float(config['DEFAULT']['synonym_threshold'])

nlp = spacy.load('en_core_web_md')

def check_equal(name1, description1, name2, description2, threshold = synonym_threshold):
    name_sim = nlp(name1).similarity(nlp(name2))
    description_sim = nlp(description1).similarity(nlp(description2))
    combined_sim = (name_weight * name_sim) + (description_weight * description_sim)
    return combined_sim >= threshold
