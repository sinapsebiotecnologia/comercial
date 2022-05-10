def f():
    #pergunta se é fapesp (1,0)
    fapesp = bool("O cliente é Fapesp? ")
    if fapesp == 0:
        # pergunta se é ffm (1,0)
        ffm = bool("O cliente é Fundação faculdade de medicina? ")

        if ffm==1:
            return 2
        else:
            return 0
    else:
        return 1


def lado_tabela(sp, contr):
    if sp == 1 or contr == 1:
        return 'a'
    return 'b'


def notas():
    return input(
        "<1> - Venda Normal\n" +
        "<2> - Amostra\n" +
        "<3> - Doação\n" +
        "<4> - Entrega futura de venda\n" +
        "<5> - Entrega futura Remessa\n" +
        "<6> - Demonstracao\n" +
        "<7> - Saida Troca\n" +
        "<8> - Venda por conta e ordem\n" +
        "<9> - Simples remessa" +
        "\nDigite o numero equivalente a operacao:\n" \
         )

def decisao(operacao,lado,ipi,fs,origem,demonstracao):
    count = 1
    for opi in (op1,op2,op3,op4,op5,op6,op7,op8,op9):
        if operacao == count:
            return opi(lado,ipi,fs,origem,demonstracao)
        else:
            count += 1

def op1(lado,ipi,fs,origem,demonstracao):

    if lado == 'a':
        if fs == 1 and origem == 6:

            if ipi == 1:
                return 554
            else:
                return 533
        if fs == 2:
            if ipi == 1:
                return 565
            else:
                return 560
        if ipi == 1:
            return 501
        else:
            return 535
    else:
        if ipi == 1:
            return 948
        else:
            return 947

def op2(lado,ipi,fs,origem,demonstracao):
     return 527

def op3(lado,ipi,fs,origem,demonstracao):
    if lado == 'a':
        if fs == 2:
            return 928
        if ipi == 1:
            return 924
        else:
            return 925
    else:
        if ipi == 1:
            return 951
        else:
            return 950

def op4(lado,ipi,fs,origem,demonstracao):
    if ipi == 1:
        return 505
    else:
        return 537

def op5(lado,ipi,fs,origem,demonstracao):
    if lado == 'a':
        return 504
    else:
        return 949

def op6(lado,ipi,fs,origem,demonstracao):

        if demonstracao == 1:
            return 955
        else:
            return 956

def op7(lado,ipi,fs,origem,demonstracao):
    if fs==1 and origem==1:
        return 544

    if ipi == 0:
        if fs == 2 or (fs==1 and origem==6):
            return 550
        return 900

    else:
        if fs == 2:
            555
        else:
            544

def op8(lado,ipi,fs,origem,demonstracao):
    if ipi == 0:
        return 540
    else:
        return 522

def op9(lado,ipi,fs,origem,demonstracao):
    return 521


def bool(text):
    while True:
        var = input(text)
        if var == '1' or var == '0':
            var = int(var)
            break
        else:
            print("Favor responder com 1 ou 0.")
    return var

