class Produto:
    def __init__(self, nome, quantidade, validade, categoria):
        self.nome = nome
        self.quantidade = quantidade
        self.validade = validade
        self.categoria = categoria

    def to_dict(self):
        return {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "validade": self.validade,
            "categoria": self.categoria
        }

    @staticmethod
    def from_dict(dados):
        return Produto(
            dados["nome"],
            dados["quantidade"],
            dados["validade"],
            dados["categoria"]
        )