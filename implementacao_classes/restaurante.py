from datetime import date

# Neste modelo, o Pedido guarda apenas uma lista de Pratos.
# NÃO existe ItemDoPedido.
# O valor_final já vem calculado e armazenado diretamente.
# CONSEQUÊNCIA:
# Se o preço de um prato mudar depois,
# isso NÃO afeta o pedido, porque o valor final já está fixo.

# O prato possui seu próprio preço.
# Ele é usado apenas como referência no pedido.
# Não existe controle de quantidade por prato no pedido.

class Cliente:
    def __init__(self, nome, data_nasc, cpf):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        


class Pedido:
    def __init__(self, data_pedido, percentual_desconto, valor_final, cliente, pratos):
        self.data_pedido = data_pedido
        self.percentual_desconto = percentual_desconto
        self.valor_final = valor_final
        self.cliente = cliente
        self.pratos = pratos
        
    def __str__(self):
        pratos_str = ", ".join(prato.nome for prato in self.pratos)

        return (
            f"Pedido em {self.data_pedido}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Desconto: {self.percentual_desconto}%\n"
            f"Valor final: R$ {self.valor_final:.2f}\n"
            f"Pratos: {pratos_str}"
        )

        
        
class Prato:
    def __init__(self, nome, ingredientes, modo_preparo, preco):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.preco = preco
        
    def __str__(self):
        lista = ""
        
        for ingrediente in self.ingredientes:
            lista += f" {ingrediente},"
        
        return f"Nome: {self.nome}\nIngredientes: {lista}\nModo de preparo: {self.modo_preparo}\nPreço: {self.preco}"
        

c = Cliente("Laura", date(2009,12,19), "000000")

prato1 = Prato(
    "Sanduiche",
    ["pao", "queijo", "tomate", "alface"],
    "fazer o sanduiche", 10)

prato2 = Prato(
    "Batata frita",
    ["batata", "sal"],
    "fritar a batata e colocar sal", 15
)

p = Pedido(
    date(2026,6,26), 10, 25, c, [prato1, prato2]
)

print(p)
print("Pratos:", prato1, prato2)