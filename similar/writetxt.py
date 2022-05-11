import streamlit as st
import pandas


def main():
    x = st.file_uploader('arquivo')

    st.text(x)

    # if x != 'None':
    #     excel_data_df = pandas.read_excel(x)
    #     json_str = excel_data_df.to_json()
    #     st.text(json_str)

if __name__ == '__main__':
    main()