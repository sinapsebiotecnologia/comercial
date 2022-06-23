import json
import pandas
import requests as req
import streamlit as st
import streamlit.components.v1 as components

def main():
    components.html("""<html><body><h1>Hello, World</h1><script id="ze-snippet" src="https://static.zdassets.com/ekr/snippet.js?key=c5a26d89-b719-424e-ae03-bd86a1f4feff"> </script></body></html>, width=200, height=200""")

    a = st.checkbox("Comparar", value=False)
    if a:
        #1
        dict = req.get("https://sinapsebiotecnologia.github.io/teste.json")
        dict = dict.json()

        #2
        op = st.radio('Deseja pesquisar por qual tipo?', ("Sinapse","Concorrente"), index=0)

        produto = st.text_input("codigo produto: ")

        #3
        resultado = 'None'
        if lado == "Sinapse":
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
                st.error(f"Correspondente nao encontrado!")
            else:
                st.success(f"O produto {produto}, e similar ao produto {resultado}")

        #5
        # excel_data_df = pandas.read_excel('teste.xlsx')
        # json_str = excel_data_df.to_json()



if __name__ == '__main__':
    main()