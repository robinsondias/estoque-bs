import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO = os.path.join(BASE_DIR, "dados.json")

def salvar_estoque(estoque):
    with open(CAMINHO, "w") as f:
        lista = [p.to_dict() for p in estoque]
        json.dump(lista, f, indent=4)