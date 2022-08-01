import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit

def main():
    html_temp = """ <div style ="background-color:blue;padding:13px">
                      <h1 style = "color:white;text-align:center;">Feramentas Comerciais</h1>
                    </dic>
                    
                """


    # Render the h1 block, contained in a frame of size 200x200.
    st.markdown(html_temp, unsafe_allow_html=True)

    # st.markdown("---")

    # começo calc tes
    tes = 'test'
    st.header('Calculadora TES')

    opcoes = ['Selecione a Operação', "Venda Normal", "Amostra", "Doação", "Entrega futura de venda",
              "Entrega futura remessa", "Demonstração", "Saida Troca",
              "Venda por conta e ordem", "Simples remessa","Faturamento entre entidades publicas (entre 2 estados diferentes)"]

    checkbox = st.selectbox('', opcoes)

    operacao = numero_operacao(checkbox)

    if operacao != 0:

        if operacao == 9:
            tes = 521
        elif operacao == 6:
            a = st.checkbox('Produto para Demonstração em evento')
            tes = (955 if a else 956)
        elif operacao == 2:
            tes = 527
        else:
            if operacao != 5:
                ipi = st.checkbox("Produto Com IPI", value=False)
            if operacao == 4:
                tes = op4(ipi)
            elif operacao == 10:
                tes = op10(ipi)
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
                    if cnpj and operacao != 3:
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
            st.success(b)
            if operacao == 10:
                st.warning("**A remessa das mercadorias, deverá conter destaque do ICMS devido, " \
                    "contendo além das informações previstas na legislação.**" \
                    "\n- Destinatário, aquele determinado pelo adquirente (Cliente);" \
                    "\n- Natureza da operação, a expressão \"Remessa por conta e ordem de terceiros\";" \
                    "\n- \"Chave de Acesso da NF-e Referenciada\", a chave de acesso da NF-e relativa ao faturamento (NFE 1);" \
                    "\n- \"Informações Complementares\", a expressão \"NF-e emitida nos termos do artigo 129-A do RICMS/2000-SP\" e " \
                    "\" Ajuste Sinief 13/2013\".")

            # final calc tes
    # st.markdown("---")

# inicio funcoes calc tes

def op10(ipi):
    return (953 if ipi else 954)
def op4(ipi):
    return (505 if ipi else 537)
def op8(ipi):
    return (522 if ipi else 540)
def op5(lado):
    return ( 504 if lado == 'a' else 949 )
def op1(fund,ipi,lado,choice):
    if lado == 'a':
        if fund == 1 and choice == 6:
            return (554 if ipi else 533)
        elif fund == 2:
            return (565 if ipi else 560)
        return (501 if ipi else 535)
    else:
        return (948 if ipi else 947)
def op3(fund,ipi,lado):
    if lado == 'a':
        if fund == 2:
            return 928
        else:
            return (924 if ipi else 925)
    else:
        return (951 if ipi else 950)
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
    return ('a' if sp or contr else 'b')
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
    elif txt == "Faturamento entre entidades publicas (entre 2 estados diferentes)":
        x = 10
    return x

# final funcoes calc tes


if __name__ == '__main__':
    main()