
senha = str(input())
out = 0
if len(senha) == 0:
    print(6)
elif len(senha) == 1:
    print(5)
elif len(senha) == 2:
    print(4)
elif len(senha) == 3:
    print(3)
elif len(senha) > 3:
    faltam = 4
    novasenha = senha
    if any(chr.isdigit() for chr in senha):
        novasenha = ''.join([i for i in novasenha if not i.isdigit()])
        faltam = faltam - 1
    if any(chr.isupper() for chr in senha):
        novasenha = ''.join([i for i in novasenha if not i.isupper()])
        faltam = faltam - 1
    if any(chr.islower() for chr in senha):
        novasenha = ''.join([i for i in novasenha if not i.islower()])
        faltam = faltam - 1
    if len(novasenha) > 0:
        faltam = faltam - 1
    if faltam + len(senha) >= 6:
        print(faltam)
    elif len(senha) == 4:
        print(2)
    else:
        print(1)

    