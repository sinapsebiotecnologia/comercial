import json
import pandas
import requests as req
import streamlit as st

def main():
    if st.checkbox("Comparar"):
        #1
        dict = req.get("https://sinapsebiotecnologia.github.io/teste.json")
        dict = dict.json()

        #2
        op = st.radio('Deseja pesquisar por qual tipo?', ("Sinapse","Concorrente"), index=0)

        produto = st.text_input("codigo produto: ")

        #3
        resultado = 'None'
        if op == "Sinapse":
            for i in range(len(dict)):
                if dict[i]["Sinapse"] == produto:
                    resultado = dict[i]["Concorrente"]
                    break
        for i in range(len(dict)):
            if dict[i]["Concorrente"] == produto:
                resultado = dict[i]["Sinapse"]
                break

        #4
        if st.button("Verificar"):
            if resultado == 'None':
                st.error(f"Correspondente nao encontrado! (se achar que isso é um erro, favor verificar arquivo excel)")
            else:
                st.sucess(f"O produto {produto}, e similar ao produto {resultado}")

        #5
        # excel_data_df = pandas.read_excel('teste.xlsx')
        # json_str = excel_data_df.to_json()



if __name__ == '__main__':
    main()