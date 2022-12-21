# Link: https://colab.research.google.com/drive/18A_dnXcu31vXkXAZ6d_FadQnzmtlI_2P?usp=sharing

from google.colab import drive
drive.mount('/content/gdrive')

import random
import sys
sys.path.insert(1, '/content/gdrive/MyDrive/Colab Notebooks/FactoryMethod3.2')


class Public:
    def exibeInfos():
        with open("/content/gdrive/MyDrive/Colab Notebooks/FactoryMethod3.2/publico.txt", "r") as arquivo:
            text = arquivo.read()
        print(text)

class Confidential:
    def exibeInfos():
        with open("/content/gdrive/MyDrive/Colab Notebooks/FactoryMethod3.2/confidencial.txt", "r") as arquivo:
            text = arquivo.read()
        print(text)

        
def Factory(senha):
    types = {
        "public": Public,
        "confidential": Confidential
    }
    return types[senha]


def defineSeguranca(senha):
    if senha == "designpatterns":
        return 'confidential'
    else: 
        return 'public'

    
if __name__ == "__main__":
    senha = "designpatterns"
    Factory(defineSeguranca(senha)).exibeInfos()
