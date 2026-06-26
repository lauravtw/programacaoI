class Temperamento:
    def __init__(self, id, nome, elemento, focoProfissional, pontos_fortes, desafios, personalidades, areas):
        self.id = id
        self.nome = nome
        self.elemento = elemento
        self.focoProfissional = focoProfissional
        self.pontos_fortes = pontos_fortes
        self.desafios = desafios
        self.personalidades = personalidades
        self.areas = areas
        
    def __str__(self):
        texto = f"Temperamento: {self.nome}\n"
        texto += f"ID: {self.id}\n"
        texto += f"Elemento: {self.elemento}\n"
        texto += f"Foco profissional: {self.focoProfissional}\n"

        texto += "\nPontos fortes:\n"
        for ponto in self.pontos_fortes:
            texto += str(ponto) + "\n"

        texto += "\nDesafios:\n"
        for desafio in self.desafios:
            texto += str(desafio) + "\n"

        texto += "\nPersonalidades:\n"
        for personalidade in self.personalidades:
            texto += str(personalidade) + "\n"

        texto += "\nÁreas ideais:\n"
        for area in self.areas:
            texto += str(area) + "\n"

        return texto
        
class PontoForte:
    def __init__(self,descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

        
class Desafio:
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __str__(self):
        return self.descricao
    
class Personalidade:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome
        
class AreaIdeal:
    def __init__(self, nome, profissoes):
        self.nome = nome
        self.profissoes = profissoes 
        
    def __str__(self):
        texto = self.nome + ": "

        for profissao in self.profissoes:
            texto += str(profissao) + ", "

        return texto[:-2]  # remove a última vírgula e espaço

class Profissao:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome
    

        
sanguineo = Temperamento(
    1,
    "Sanguíneo",
    "Ar",
    "Pessoas e Dinamismo",
    [
        PontoForte("Extrovertido"),
        PontoForte("Comunicativo"),
        PontoForte("Espontâneo"),
        PontoForte("Otimista"),
        PontoForte("Entusiasta")
    ],
    [
        Desafio("Impulsivo"),
        Desafio("Indisciplinado"),
        Desafio("Superficial"),
        Desafio("Falta de foco")
    ],
    [
        Personalidade("Bill Clinton"),
        Personalidade("Will Smith"),
        Personalidade("Anna (Frozen)"),
        Personalidade("Joey (Friends)")
    ],
    [
        AreaIdeal(
            "Comunicação, Vendas, Eventos e Entretenimento",
            [
                Profissao("Jornalista"),
                Profissao("Vendedor"),
                Profissao("Relações Públicas"),
                Profissao("Ator"),
                Profissao("Professor"),
                Profissao("Corretor")
            ]
        )
    ]
)

colerico = Temperamento(
    2,
    "Colérico",
    "Fogo",
    "Resultados e Desafios",
    [
        PontoForte("Determinado"),
        PontoForte("Focado"),
        PontoForte("Líder nato"),
        PontoForte("Prático"),
        PontoForte("Corajoso")
    ],
    [
        Desafio("Impaciente"),
        Desafio("Autoritário"),
        Desafio("Intolerante"),
        Desafio("Orgulhoso")
    ],
    [
        Personalidade("Napoleão Bonaparte"),
        Personalidade("Steve Jobs"),
        Personalidade("Gordon Ramsay")
    ],
    [
        AreaIdeal(
            "Gestão, Liderança, Empreendedorismo e Direito",
            [
                Profissao("Diretor/CEO"),
                Profissao("Empreendedor"),
                Profissao("Advogado"),
                Profissao("Engenheiro"),
                Profissao("Gestor de Projetos")
            ]
        )
    ]
)

melancolico = Temperamento(
    3,
    "Melancólico",
    "Terra",
    "Processos e Detalhes",
    [
        PontoForte("Analítico"),
        PontoForte("Organizado"),
        PontoForte("Detalhista"),
        PontoForte("Profundo")
    ],
    [
        Desafio("Pessimista"),
        Desafio("Perfeccionista"),
        Desafio("Muito crítico"),
        Desafio("Reservado")
    ],
    [
        Personalidade("Albert Einstein"),
        Personalidade("Sherlock Holmes"),
        Personalidade("Bruce Wayne")
    ],
    [
        AreaIdeal(
            "Ciência, Finanças, Tecnologia, Artes e Planejamento",
            [
                Profissao("Programador"),
                Profissao("Contador"),
                Profissao("Arquiteto"),
                Profissao("Analista de Dados"),
                Profissao("Escritor"),
                Profissao("Cientista")
            ]
        )
    ]
)

fleumatico = Temperamento(
    4,
    "Fleumático",
    "Água",
    "Estabilidade e Mediação",
    [
        PontoForte("Calmo"),
        PontoForte("Paciente"),
        PontoForte("Diplomata"),
        PontoForte("Confiável"),
        PontoForte("Equilibrado")
    ],
    [
        Desafio("Procrastinador"),
        Desafio("Indeciso"),
        Desafio("Evita conflitos"),
        Desafio("Passivo")
    ],
    [
        Personalidade("Mahatma Gandhi"),
        Personalidade("Samwise Gamgee"),
        Personalidade("Hagrid")
    ],
    [
        AreaIdeal(
            "Educação, RH, Suporte, Saúde e Administração Pública",
            [
                Profissao("Analista de RH"),
                Profissao("Diplomata"),
                Profissao("Assistente Social"),
                Profissao("Enfermeiro"),
                Profissao("Bibliotecário")
            ]
        )
    ]
)

print(sanguineo)
print(colerico)
print(melancolico)
print(fleumatico)
        
        
        
