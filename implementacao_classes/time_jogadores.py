class Selecao:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores 
    
    def __str__(self):
        str = f"SELEÇÃO: {self.nome}\n"
        
        for jogador in self.jogadores:
            str += (jogador.nome) + "\n"
        
        return str

class Jogador:
    def __init__(self, posicao, nome, clube):
        self.posicao = posicao
        self.nome = nome
        self.clube = clube
    
    def __str__(self):
        return f"Jogador\nNome: {self.nome}\nPosição: {self.posicao}\nClube: {self.clube}"

j1 = Jogador("Goleiro", "Alisson Becker", "Liverpool FC")
j2 = Jogador("Meio-campo", "Casemiro", "Manchester United FC")
j3 = Jogador("Atacante", "Vinícius Júnior", "Real Madrid CF")

brasil = Selecao("Brasil", [])

brasil.jogadores.append(j1)
brasil.jogadores.append(j2)
brasil.jogadores.append(j3)

print(brasil)
print(j1)



        
        