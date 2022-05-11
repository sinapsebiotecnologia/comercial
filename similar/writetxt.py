import streamlit as st


def main():
    x = st.file_uploader('arquivo', type=txt)

    st.text(x)

if __name__ == '__main__':
    main()