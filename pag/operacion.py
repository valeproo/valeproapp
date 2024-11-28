import streamlit as st

st.title("Operaciones entre complejos")

st.header("Suma")

st.markdown("""
La suma y diferencia de números complejos se realiza sumando y restando las partes reales y las partes imaginarias entre sí, respectivamente.
""")
st.latex(r"z + w = (a + bi) + (c + di) = (a + c) + (b + d)i")

st.header("Producto")

st.markdown("""
El producto de los números complejos se realiza aplicando la propiedad distributiva del producto respecto de la suma y teniendo en cuenta que:
""")

st.latex(r"i^2 = -1")
st.markdown("""
Entonces, 
""")
st.latex(r"z \cdot w = (a + bi)(c + di) = (ac - bd) + (ad + bc)i")

