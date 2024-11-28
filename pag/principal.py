import streamlit as st

st.title("Números Complejos")


with st.container(border=True):
    st.subheader(":violet[Definición]")
    st.markdown("""
    Se entiende por números complejos a la combinación de números reales e imaginarios. La **parte real** puede ser expresada por un número entero o sus decimales, mientras que la **parte imaginaria** es aquella cuyo cuadrado es negativo. 
    """)
    st.latex(r"\mathbb{C} = \{ a + bi \mid a, b \in \mathbb{R}, \ i^2 = -1 \}")
    st.markdown("""
    Entonces,
    """)
    
    st.latex(r"z \in \mathbb{C}, \ z = a + bi") 
    st.markdown("""
    Lo anterior es la ***forma binómica del número complejo.***
    """)






