import streamlit as st

st.title("Números Complejos")

st.image("https://images.jifo.co/122143261_1648595154570.png")

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
    + **Forma binómica del número complejo:**
    """)
    c1, c2, c3 = st.columns([1,2,1],vertical_alignment="center")
    with c1:
        st.markdown("")
    with c2:
        st.image("https://www.neurochispas.com/wp-content/uploads/2021/01/aplicaciones-de-los-numeros-complejos.png")
    with c3:
        st.markdown("")
    with st.expander("**EJEMPLOS**"):
        c1,c2,c3=st.columns([1,1,1],vertical_alignment="top" )
        with c1:
            st.markdown("**Número complejo**")
            st.markdown("""
            + 7i - 2
            
            + -6
            
            + -8i
            """)
        with c2:
            st.markdown("**Forma estándar**")
            st.markdown("""
            + -2 + 7i

            + -6 + **0**i
            
            + **0** -8i
            """)
        with c3:
            st.markdown("**Descripcion de las partes**")
            st.markdown("""
            + la **parte real** es -2 y la **parte imaginaria** es 7.
            + la **parte real** -6 es y la **parte imaginaria** es 0.
            + la **parte real** 0 es y la **parte imaginaria** es -8.
            """)

st.subheader("Hora de practicar!")
c1, c2, c3 = st.columns([1,1,1],vertical_alignment="center")
with c1:
    st.latex(r"z_1 = 3 + 4i")
    n = st.number_input(" La parte real es:   ", min_value=-1000, max_value=80, value= 5)
    if st.button("Verificar"):
        if n==3:
            st.markdown(f"CORRECTO!")
        else:
            st.markdown(f"No es {n} :c, inténtalo de nuevo.")
with c2:
    st.latex(r"z_2 = -1 - 2i")
    n = st.number_input(" La parte imaginaria es:   ", min_value=-100, max_value=100, value= 5)
    if st.button("Verificar "):
        if n== -2:
            st.markdown(f"CORRECTO!")
        else:
            st.markdown(f"No es {n} :c, inténtalo de nuevo.")
with c3:
    st.latex(r"z_3 = - 8i")
    n = st.number_input(" La parte real es:   ", min_value=-100, max_value=1000, value=5)
    if st.button("Verificar  "):
        if n== 0:
            st.markdown(f"CORRECTO!")
        else:
            st.markdown(f"No es {n} :c, inténtalo de nuevo.")
st.divider()
with st.container(border=True):
    st.subheader(":violet[Conjugado de un complejo]")
    st.markdown("""
    El **conjugado** de un número complejo es el número complejo cuando su **parte imaginaria** cambia de signo.
    """)
    st.latex(r"z = a + bi \ \longrightarrow \ \overline{z} = a - bi")
    with st.expander("**EJEMPLOS**"):
        c1, c2 = st.columns([1,1], vertical_alignment="top")
        with c1: 
            st.latex(r"z = 2 + 9i \ \longrightarrow \ \overline{z} = 2 - 9i")

            st.latex(r"z = 7 \ \longrightarrow \ \overline{z} = 7 ")
        with c2: 
            st.latex(r"z = 5i \ \longrightarrow \ \overline{z} =  - 5i")

            st.latex(r"z = -3 + 4i \ \longrightarrow \ \overline{z} = -3 - 4i")


st.divider()








