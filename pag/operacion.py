import streamlit as st

st.title("Operaciones entre complejos")
st.header("Forma binómica")
with st.container(border=True):
    st.subheader(":violet[Suma]")

    st.markdown("""
    La suma y diferencia de números complejos se realiza sumando y restando las partes reales y las partes imaginarias entre sí, respectivamente.
    """)
    st.latex(r"z + w = (a + bi) + (c + di) = (a + c) + (b + d)i")
c1,c2=st.columns([1,1])
with c1:
    st.markdown("**EJEMPLOS:**")
    st.markdown("""
        1. Realizar las siguientes operaciones con números complejos: 
        """)
    st.latex(r"a. (3 + 2i) + (1 - 4i)")
    st.latex(r"b. (5 + 6i) - (2 + 3i)")
with c2:
    with st.expander("Ver solución"):
        st.latex(r"""
        a. (3 + 2i) + (1 - 4i) \\
        = (3 + 1) + (2 - 4)i \\
        = 4 - 2i
        """)
        st.latex(r"""
        b. (5 + 6i) - (2 + 3i) \\
        = (5 - 2) + (6 - 3)i \\
        = 3 + 3i
        """)
st.divider()
with st.container(border=True):
    st.subheader(":violet[Producto]")

    st.markdown("""
    El producto de los números complejos se realiza aplicando la propiedad distributiva del producto respecto de la suma y teniendo en cuenta que:
    """)

    st.latex(r"i^2 = -1")
    st.markdown("""
    Entonces, 
    """)
    st.latex(r"z \cdot w = (a + bi)(c + di) = (ac - bd) + (ad + bc)i")

c1,c2=st.columns([1,1])
with c1:
    st.markdown("**EJEMPLOS**")
    st.markdown("""
    1. Realizar las siguientes operaciones con números complejos: 
    """)
    st.latex(r"(2 + 3i)(4 + 5i)")
    st.latex(r"(-1 + 2i)(3 - i)")  
with c2:
    with st.expander("Ver solución"):
        st.latex(r"(2 + 3i)(4 + 5i)\\ = (2 \cdot 4 - 3 \cdot 5) + (2 \cdot 5 + 3 \cdot 4)i \\ = -7 + 22i")
        st.latex(r"(-1 + 2i)(3 - i)\\ = (-1 \cdot 3 - 2 \cdot -1) + (-1 \cdot -1 + 2 \cdot 3)i\\ = -1 + 7i ")
st.divider()
with st.container(border=True):
    st.subheader(":violet[Cociente]")

    st.markdown("""
    El cociente de números complejos se realiza multiplicando numerador y denominador por el conjugado de este.
    """)

    st.latex(r"z \div w = \frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}")
c1,c2=st.columns([1,1])
with c1:
    st.markdown("**EJEMPLOS**")
    st.markdown("""
    1. Realizar las siguientes operaciones con números complejos: 
    """)
    st.latex(r"""
        \frac{3 + 4i}{1 - 2i}
        """)
with c2:
    with st.expander("Ver solución"):
        st.latex(r"""
        \frac{3 + 4i}{1 - 2i} = \frac{(3 + 4i)(1 + 2i)}{(1 - 2i)(1 + 2i)} \\
        = \frac{3 + 6i + 4i + 8i^2}{1^2 - (2i)^2} \\
        = \frac{3 + 6i + 4i - 8}{1 - (-4)} \\
        = \frac{-5 + 10i}{5} \\
        = -1 + 2i
        """)
st.divider()
st.subheader("¡Ahora inténtalo tú!")
c1, c2 = st.columns([1,1],vertical_alignment="center")
with c1:
    st.latex(r"\frac{(3 + 4i)}{(-2 + 5i)}")
    n = st.text_input("La solucion es (sin espacios):", key="sol1")
    if st.button(" Verificar"):
        if n=="14/39-23/29i" or n=="14/39-23i/29" or n== "-23/29i+14/39" or n== "-23i/29+14/39":
            st.markdown(f"LO HAS HECHO MUY BIEN!")
        else:
            st.markdown(f"No es {n} :c, inténtalo de nuevo.")
with c2:
    st.latex(r"(6 - 3i) + (-1 - 2i)")
    n = st.text_input(" La respuesta es (sin espacios):   ")
    if st.button("Verificar "):
        if n== "5-5i" or n== "-5i+5":
            st.markdown(f"MUY BIEN!")
        else:
            st.markdown(f"No es {n} :c, inténtalo de nuevo.")
c1, c2 = st.columns([1,1],vertical_alignment="center")
with c1:
    st.latex(r"(3 + 4i)(-2 + 5i)")
    n = st.text_input(" La solucion es (sin espacios) :   ")
    if st.button("  Verificar"):
        if n=="-26+7i" or n=="7i-26":
            st.markdown(f"ESO ES CORRECTO!")
        else:
            st.markdown(f"No es {n} :c, inténtalo de nuevo.")
with c2:
    st.latex(r"(0 + 7i)(-8 + 0i)")
    n = st.text_input(" La solucion es (sin espacios):   ")
    if st.button("Verificar     "):
        if n== "-56i":
            st.markdown(f"MUY BIEN!")
        else:
            st.markdown(f"No es {n} :c, inténtalo de nuevo.")
st.divider()
st.header("Forma Polar")
with st.container(border=True):
    st.subheader(":violet[Producto]")
    st.markdown("""
    La multiplicación de dos números complejos es otro número complejo tal que:
    + Su módulo es el producto de los módulos.
    + Su argumento es la suma de los argumentos.
    """)
    st.latex(r"z_1 = |z_1| e^{i\alpha_1}, \quad z_2 = |z_2| e^{i\alpha_2}")
    st.latex(r"z_1 \cdot z_2 = |z_1| |z_2| e^{i(\alpha_1 + \alpha_2)}")
c1,c2= st.columns([1,1])
with c1:
    st.markdown("**EJEMPLO**")
    st.markdown("1. Hallar el producto entre los siguientes complejos en forma polar:")
    st.latex(r"""
    z_1 = 2e^{i\pi/4}, \quad z_2 = 3e^{i\pi/6}, \quad
    """)
with c2:
    with st.expander("Ver solución"):
        st.latex(r"""
        |z_1|e^{i\theta_1} \cdot |z_2|e^{i\theta_2} \rightarrow (|z_1| \cdot |z_2|) e^{i(\theta_1 + \theta_2)} \\
        = (2 \cdot 3) e^{i\left(\frac{\pi}{4} + \frac{\pi}{6}\right)} \\
        = 6e^{i\frac{5\pi}{12}}.
        """)
st.divider()
with st.container(border=True):
    st.subheader(":violet[Cociente]")
    st.markdown("""
    La división de dos números complejos es otro número complejo tal que:
    + Su módulo es el cociente de los módulos.

    + Su argumento es la diferencia de los argumentos.
    """)
    st.latex(r"""
\frac{z_1}{z_2} = \frac{|z_1|}{|z_2|} e^{i(\theta_1 - \theta_2)}
""")
c1,c2=st.columns([1,1])
with c1:
    st.markdown("**EJEMPLO**")
    st.markdown("1. Realiza el cociente entre los siguientes complejos en forma polar:")
    st.latex(r"""
    z_1 = 4e^{i\pi/3}, \quad z_2 = 2e^{i\pi/6}
    """)
with c2:
    with st.expander("Ver solución"):
        st.latex(r"""
        \frac{z_1}{z_2} = \frac{|z_1|}{|z_2|} e^{i(\theta_1 - \theta_2)}
        """)
        st.latex(r"""
        \frac{|z_1|}{|z_2|} = \frac{4}{2} = 2, \quad 
        \theta_1 - \theta_2 = \frac{\pi}{3} - \frac{\pi}{6} = \frac{\pi}{6}
        """)
        st.latex(r"""
        \frac{z_1}{z_2} = 2e^{i\pi/6}
        """)