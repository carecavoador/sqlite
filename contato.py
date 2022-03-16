class Contato:
    def __init__(self, nome, telefone, cidade):
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
    
    def __repr__(self):
        return f"Contato: {self.nome} | Telefone: {self.telefone} | Cidade: {self.cidade}"

if __name__ == "__main__":
    pessoa = Contato("Everton", "99999-9999", "Blumenau")
    print(pessoa)
