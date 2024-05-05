import streamlit as st


image_path = 'images/Frame 33.png'

# Carregando e exibindo a imagem
st.image(image_path)

st.button("Já tenho conta")
st.button("Não tenho conta")

st.markdown('''
<style>
            
    body {
        color: #fff;
        background-color: #FFFFFFFF;
    }
</style>
''', unsafe_allow_html=True)