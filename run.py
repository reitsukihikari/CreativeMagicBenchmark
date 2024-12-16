import os
import sys
from Util.loaddata import loaddata
from Util.exportdata import exportdata
from Util.vqa import img2obj, load_model
from Math.score import score
import multiprocessing

def en_spacy_model(model_name='en_core_web_md'):
    try:
        import spacy
        spacy.load(model_name)
    except (ImportError, IOError):
        print(f"Model '{model_name}' not found, downloading...")
        import subprocess
        subprocess.run(['python', '-m', 'spacy', 'download', model_name])
        print(f"Model '{model_name}' downloaded.")

def main():
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    en_spacy_model('en_core_web_md')
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    load_model()
    
    dataset = loaddata('Dataset/magic.json')
    dataset = img2obj(dataset)
    magic_score = {}
    for magic in dataset['Magics']:
        schemes = magic['Schemes']
        total = 0
        print(f"\tmagic: {magic['ID']}")
        for scheme in schemes:
            while True:
                try:
                    print(f"\t\tscheme: {scheme['ID']}")
                    scheme_score = score(scheme)
                    print(f"\t\t\tscore: {scheme_score:.2f}")
                    total += scheme_score
                    break
                except Exception as e:
                    print(f"Evaluating scheme {scheme['ID']} failed: {e}. I think we should just retry...!")
        magic_score[magic['ID']] = round(total / len(schemes), 2)

    print(magic_score)

    exportdata(magic_score, 'Output/magic_score.csv')

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
