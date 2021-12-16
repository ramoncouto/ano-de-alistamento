from datetime import date
anoAtual = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
genero = str(input('Qual é o seu gênero? [M / F]: ').strip().upper())
idade = (anoAtual - nascimento)
if genero == 'M':
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {anoAtual}.')
    if idade > 18:
        print(f'''Você já deveria ter se alistado há {idade - 18} anos
Seu alistamento foi em {anoAtual - (idade - 18)}''')
    elif idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')
    else:
        print(f'''Ainda faltam {18 - idade} anos para o alistamento.
    Seu alistamento será em {anoAtual + (18 - idade)}''')
else:
    print('Você não precisa se alistar.')
