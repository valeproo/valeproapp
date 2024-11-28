import streamlit as st

st.title("Operaciones entre complejos")

st.header(":violet[Suma]")

st.markdown("""
La suma y diferencia de números complejos se realiza sumando y restando las partes reales y las partes imaginarias entre sí, respectivamente.
""")
st.latex(r"z + w = (a + bi) + (c + di) = (a + c) + (b + d)i")
st.subheader("ejemplos:")
st.markdown("""
1. Realizar las siguientes operaciones con números complejos: 
""")
st.latex(r"(3 + 2i) + (1 - 4i) = (3 + 1) + (2 - 4)i = 4 - 2i")
st.latex(r"(5 + 6i) - (2 + 3i) = (5 - 2) + (6 - 3)i = 3 + 3i")

st.header(":violet[Producto]")

st.markdown("""
El producto de los números complejos se realiza aplicando la propiedad distributiva del producto respecto de la suma y teniendo en cuenta que:
""")

st.latex(r"i^2 = -1")
st.markdown("""
Entonces, 
""")
st.latex(r"z \cdot w = (a + bi)(c + di) = (ac - bd) + (ad + bc)i")
st.subheader("ejemplos:")
st.markdown("""
1. Realizar las siguientes operaciones con números complejos: 
""")
st.latex(r"(2 + 3i)(4 + 5i) = (2 \cdot 4 - 3 \cdot 5) + (2 \cdot 5 + 3 \cdot 4)i = -7 + 22i")
st.latex(r"(-1 + 2i)(3 - i) = (-1 \cdot 3 - 2 \cdot -1) + (-1 \cdot -1 + 2 \cdot 3)i = -1 + 7i")

st.header(":violet[Cociente]")

st.markdown("""
El cociente de números complejos se realiza multiplicando numerador y denominador por el conjugado de este.
""")

st.latex(r"z \div w = \frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}")
st.subheader("ejemplos:")
st.markdown("""
1. Realizar las siguientes operaciones con números complejos: 
""")
st.latex(r"""
\frac{3 + 4i}{1 - 2i} = \frac{(3 + 4i)(1 + 2i)}{(1 - 2i)(1 + 2i)} \\
= \frac{3 + 6i + 4i + 8i^2}{1^2 - (2i)^2} \\
= \frac{3 + 6i + 4i - 8}{1 - (-4)} \\
= \frac{-5 + 10i}{5} \\
= -1 + 2i
""")



