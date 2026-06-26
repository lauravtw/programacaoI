class Veiculo:
    def __init__(self, placa, ano):
        self.placa = placa
        self.ano = ano
    
    def __str__(self):
        return f"Placa: {self.placa}\nAno: {self.ano}"
        
class Moto(Veiculo):
    def __init__(self, placa, ano):
        super().__init__(placa, ano)

    def __str__(self):
        return super().__str__()

class Caminhao(Veiculo):
    def __init__(self, placa, ano, peso_em_kg):
        super().__init__(placa, ano)
        self.peso_em_kg = peso_em_kg
        
    def __str__(self):
        return f"{super().__str__()}\nPeso em kg: {self.peso_em_kg} "
        

m = Moto("ABC-1234", 2022)
print(m)

c = Caminhao("XYZ-9876", 2020, 12000)
print(c)