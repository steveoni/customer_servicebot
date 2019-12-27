from fastai.text import load_learner
from pathlib import Path

def make_model():

    path = Path("models")
    
    model = load_learner(path)

    return model


if __name__=="__main__":
    leaner = make_model()

    print(leaner.predict("ok")[0])

