from datetime import date

class Cliente: 
    def __init__(self, nome, data_nasc, cpf):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        


class Pedido:
    def __init__(self, data_pedido, percentual_desconto, cliente, itens, valor_total):
        self.data_pedido = data_pedido
        self.percentual_desconto = percentual_desconto
        self.cliente = cliente
        self.itens = itens
        self.valor_total = valor_total
        
    def __str__(self):
        itens_str = "\n".join(
        f"- {item.prato.nome} | qtd: {item.quantidade} | R$ {item.valor_prato:.2f}"
        for item in self.itens
        )

        return (
            f"Pedido em {self.data_pedido}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Desconto: {self.percentual_desconto}%\n"
            f"Itens:\n{itens_str}\n"
            f"Valor total: R$ {self.valor_total:.2f}\n"
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
        

class ItemDoPedido:
    def __init__(self, prato, valor_prato, quantidade):
        self.prato = prato
        self.valor_prato = valor_prato
        self.quantidade = quantidade
    
    def __str__(self):
        return f"Prato: {self.prato}\nValor prato:: {self.valor_prato}\nQuantidade: {self.quantidade}"


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
    date(2026,6,26), 10, c,
    [ItemDoPedido(prato1, 20, 2), ItemDoPedido(prato2, 30, 2)],
    50
)

print(p)
print(f"Pratos:\n{prato1}\n{prato2}")