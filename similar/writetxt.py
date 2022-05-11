import streamlit as st
import pandas


def main():

    excel_data_df = pandas.read_excel('teste.xlsx')
    json_str = excel_data_df.to_json()
    st.text(json_str)

if __name__ == '__main__':
    main()