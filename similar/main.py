import json
import pandas
import streamlit as st

def main():

    #1
    dict = json.load(open('teste.json'))

    #2
    op = input("produto ORIGINAL ou SIMILAR?: ")
    produto = input("codigo produto: ")

    #3
    resultado = 'None'
    if op == "ORIGINAL":
        for i in range(len(dict)):
            if dict[i]["ORIGINAL"] == produto:
                resultado = dict[i]["SIMILAR"]
                break
    for i in range(len(dict)):
        if dict[i]["SIMILAR"] == produto:
            resultado = dict[i]["ORIGINAL"]
            break

    #4
    if resultado == 'None':
        print(f"Correspondente nao encontrado! (se achar que isso é um erro, favor verificar arquivo excel)")
    else:
        print(f"O produto {produto}, e similar ao produto {resultado}")

    #5
    excel_data_df = pandas.read_excel('teste.xlsx')
    json_str = excel_data_df.to_json()



if __name__ == '__main__':
    main()