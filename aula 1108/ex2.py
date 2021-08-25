filmes = {"Motoqueiro fantasma": {"2008": "Nicolas Cage"}, "Homem-aranha": {"2002": "Tobey Maguire"}, "Homem de ferro": {"2008": "Robert Downey Jr"}, "Venom": {"2018": "Tom Hardy"}, "Motoqueiro fantasma espirito de vingança": {"2011": "Nicolas Cage"}}
print(filmes)

# for chave, valor in filmes.items():
#     print('\n Filme: ', chave)
#     print('\n Ano: ', valor.keys())
#     print('\n Ator: ', valor.values())

# for chave, valor in filmes.items():
#     print('\n Filme: ', chave)
#     print('\n Ano: ', list(valor.keys()))
#     print('\n Ator: ', list(valor.values()))


for chave, valor in filmes.items():
    print('\n Filme: ', chave)
    print('\n Ano: ', *(list(valor.keys())), sep='')
    print('\n Ator: ', *(list(valor.values())), sep='')