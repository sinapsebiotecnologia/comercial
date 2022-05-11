import streamlit as st


def main():
    x = st.file_uploader('arquivo')

    st.text(x)

if __name__ == '__main__':
    main()