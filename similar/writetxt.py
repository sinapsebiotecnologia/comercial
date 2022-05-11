import streamlit as st


def main():
    x = st.file_uploader('arquivo')

    st.text(x)

    excel_data_df = pandas.read_excel('teste.xlsx')
    json_str = excel_data_df.to_json()

if __name__ == '__main__':
    main()