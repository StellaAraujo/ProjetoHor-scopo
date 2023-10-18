# Projeto Horoscopo

print('\n\t\t\t -- Horoscopo --')
print('Digite no formato (dd/mm/aa\n')

dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mes do seu nascimento: '))


# Processamento: Cada bloco contém um elif, if e else fazendo a verificação
# do mês e dia, if o dia for maior, um signo, else o signo do mês anterior.

if mes == 1:
    if dia > 19:
        print('Signo: Aquário')
    else:
        print('Signo: Capricórnio')
elif mes == 2:
    if dia > 18:
        print('Signo: Peixes')
    else:
        print('Signo: Aquário')
elif mes == 3:
    if dia > 20:
        print('Signo: Áries')
    else:
        print('Signo: Peixes')
elif mes == 4:
    if dia > 19:
        print('Signo: Touro')
    else:
        print('Signo: Áries')
elif mes == 5:
    if dia > 20:
        print('Signo: Gêmeos')
    else:
        print('Signo: Touro')
elif mes == 6:
    if dia > 22:
        print('Signo: Câncer')
    else:
        print('Signo: Gêmeos')
elif mes == 7:
    if dia > 22:
        print('Signo: Leão')
    else:
        print('Signo: Câncer')
elif mes == 8:
    if dia > 22:
        print('Signo: Virgem')
    else:
        print('Signo: Leão')
elif mes == 9:
    if dia > 22:
        print('Signo: Libra')
    else:
        print('Signo: Virgem')
elif mes == 10:
    if dia > 22:
        print('Signo: Escorpião')
    else:
        print('Signo: Libra')
elif mes == 11:
    if dia > 21:
        print('Signo: Sagitário')
    else:
        print('Signo: Escorpião')
elif mes == 12:
    if dia > 21:
        print('Signo: Capricórnio')
    else:
        print('Signo: Touro')
else:
    print('Mês não identificado')
