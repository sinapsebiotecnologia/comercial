import streamlit as st

def main():
    html_temp = """ <div style ="background-color:blue;padding:13px">
                      <h1 style = "color:white;text-align:center;">Ferramentas Comerciais</h1>
                    </dic>
                """

    st.markdown(html_temp, unsafe_allow_html=True)

    # começo calc tes
    tes = 'test'
    st.header('Calculadora TES')

    opcoes = ['Selecione a Operação', "Venda Normal", "Amostra", "Doação", "Entrega futura de venda",
              "Entrega futura remessa", "Demonstração", "Saida Troca",
              "Venda por conta e ordem", "Simples remessa"]

    checkbox = st.selectbox('', opcoes)

    operacao = numero_operacao(checkbox)

    if operacao != 0:

        if operacao == 9:
            tes = 521
        elif operacao == 6:
            a = st.checkbox('Produto para Demonstração em evento')
            if a:
                tes = 955
            else:
                tes = 956
        elif operacao == 2:
            tes = 527
        else:
            ipi = st.checkbox("Produto Com IPI", value=False)

            if operacao == 4:
                tes = op4(ipi)
            elif operacao == 8:
                tes = op8(ipi)
            else:
                estado = st.checkbox("O cliente é de SP", value=False, )

                cnpj = st.checkbox("O cliente é pessoa juridica", value=False)

                contribuinte = False

                if cnpj:
                    contribuinte = st.checkbox("O cliente é contribuinte", value=False)

                lado = lado_tabela(estado, contribuinte)

                if operacao == 5:
                    tes = op5(lado)
                else:
                    fund = 0
                    choice = 1
                    if cnpj:
                        choice = st.radio('Origem Produto', (1,6), index=0)
                    if estado and cnpj:
                        options = ('Nenhum dos dois', 'Fapesp', 'FFM')
                        radio = st.radio('Cliente é Fapesp ou FFM?', options, index=0)

                        fund = fs(radio)

                    if operacao == 1:
                        tes = op1(fund,ipi,lado,choice)
                    elif operacao == 3:
                        tes = op3(fund,ipi,lado)
                    else:
                        tes = op7(fund,choice,ipi)

        if st.button("Verificar"):
            b = f'TES: {tes}'
            st.info(b)
            # final calc tes


# inicio funcoes calc tes

def op4(ipi):
    if ipi:
        return 505
    else:
        return  537
def op8(ipi):
    if ipi:
        return 522
    else:
        return 540

def op5(lado):
    if lado == 'a':
        return 504
    else:
        return 949

def op1(fund,ipi,lado,choice):
    if lado == 'a':
        if fund == 1 and choice == 6:
            if ipi:
                return 554
            else:
                return 533
        elif fund == 2:
            if ipi:
                return 565
            else:
                return 560
        elif ipi:
            return 501
        else:
            return 535
    else:
        if ipi:
            return 948
        else:
            return 947


def op3(fund,ipi,lado):
    if lado == 'a':
        if fund == 2:
            return 928
        elif ipi:
            return 924
        else:
            return 925
    else:
        if ipi:
            return 951
        else:
            return 950

def op7(fund,choice,ipi):
    if fund == 1 and choice == 1:
        return 544

    if ipi:
        if fund == 2 or (fund == 1 and choice == 6):
            return 550
        return 900

    else:
        if fund == 2:
            return 555
        else:
            return 544

def fs(radio):
    if radio == 'Fapesp':
        return 1
    elif radio == 'FFM':
        return 2
    return 0


def lado_tabela(sp, contr):
    if sp or contr:
        return 'a'
    return 'b'


def numero_operacao(txt):
    if txt == 'Selecione a Operação':
        x = 0
    elif txt == 'Venda Normal':
        x = 1
    elif txt == 'Amostra':
        x = 2
    elif txt == 'Doação':
        x = 3
    elif txt == 'Entrega futura de venda':
        x = 4
    elif txt == 'Entrega futura remessa':
        x = 5
    elif txt == 'Demonstração':
        x = 6
    elif txt == 'Saida Troca':
        x = 7
    elif txt == 'Venda por conta e ordem':
        x = 8
    elif txt == 'Simples remessa':
        x = 9
    return x

    # final funcoes calc tes


if __name__ == '__main__':
    main()