import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.patches as patches
import pandas as pd 
st.title("Plano Complejo")
st.subheader(":violet[Representación gráfica de un complejo]")
c1, c2= st.columns([1,1], vertical_alignment="center")
with c1:
    opc = st.selectbox("Algunos conceptos claves para graficar complejos:", options=["Partes de un complejo", "Imaginario puro", "Real puro"])

    if opc== "Partes de un complejo":
        x = [2]
        y = [4]
        st.markdown("""
        Por ejemplo, para graficar el número 2 + 4i, hay que reconocer:
        + **Parte real:** Re(z)=2

        + **Parte imaginaria:** Im(z)=4
        """)
    elif opc == "Imaginario puro":
        x = [0]
        y = [3]
        st.markdown("""
        Por ejemplo, graficar el número 3i:
        + **Imaginario puro:** si se cumple que Re(z) = 0. Además, son números ubicados sobre el eje Im(z)
        """)

    else:
        x = [-3]
        y = [0]
        st.markdown("""
        Por ejemplo, graficar el número -3.
        + **Real Puro:** si se cumple que Im(z) = 0. Además, son números que ubicados en el eje Re(z).
        """)
with c2:
    fig, ax = plt.subplots()
    ax.quiver(0,0,x[0],y[0], angles="xy", scale_units="xy", scale=1)
    ax.grid()
    ax.set_title("Plano Complejo")
    ax.set_xlabel("Im(z)")
    ax.set_ylabel("Re(z)")
    ax.axhline(0,c="gray")
    ax.axvline(0,c="gray")
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    st.pyplot(fig)



st.divider()
with st.container(border=True):
    st.subheader(":violet[Magnitud o Norma]")
    st.markdown("""
    Sea z = a + bi, la **norma** de z es la distancia desde el origen hasta el punto (a,b). 
    
    Se calcula por:

    """)
    st.latex(r"|z| = \sqrt{a^2 + b^2}")
c1,c2=st.columns([1,1])
with c1:
    st.markdown("**EJEMPLOS**:")

    st.markdown("""
    **1.** Calcular la norma del complejo z = 3 + 4i
    """)


    st.markdown("""
    **2.** Calcular la magnitud del complejo w = -8i
    """)
with c2:
    with st.expander("Ver solución"):
        st.latex(r"""
        |z| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} \\
        = \sqrt{25} = 5
        """)
        st.latex(r"""
        |w| = \sqrt{0^2 + (-8)^2} = \sqrt{0 + 64} \\
        = \sqrt{64} = 8
        """)
st.divider()
with st.container(border=True):
    st.subheader(":violet[Argumento]")
    st.markdown("""
    Se denota por **Arg(x)** y es el angulo formado por el eje real y el complejo z. 
    
    Se calcula por:

    """)
    st.latex(r"\arg(z) = \tan^{-1}\left(\frac{b}{a}\right), \quad a \neq 0")

st.subheader("Casos de los argumentos")
st.markdown("Para calcular el argumento de un número complejo, es necesario conocer los 8 casos y cómo varía la fórmula. A continuación, ingresa un número de la forma a+bi:")
f1,f2= st.columns([1,1],vertical_alignment="top")
with f1:
    x = st.number_input("Ingrese la parte real (a) :", value=0, key= "yuca")
with f2:
    y = st.number_input("Ingrese la parte imaginaria (b):", value=0, key= "yei")

c1, c2 = st.columns([1,1])
with c1:
    fig, ax = plt.subplots()
    ax.quiver(0,0,x,y, angles="xy", scale_units="xy", scale=1)
    ax.grid()
    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(z)")
    ax.axhline(0,c="gray")
    ax.axvline(0,c="gray")
    lim_x = max(abs(x), 1) + 1
    lim_y = max(abs(y), 1) + 1
    ax.set_xlim(-lim_x, lim_x)
    ax.set_ylim(-lim_y, lim_y)
    st.pyplot(fig)

with c2:
    fig, ax = plt.subplots()
    if x ==0 and y>0:
        st.markdown("""
        + **Caso 1:**
        """)
        st.latex(r"\arg(z) = \frac{\pi}{2}, \quad a = 0, b > 0")
    if x == 0 and y<0:
        st.markdown("+ **Caso 2:**")
        st.latex(r"\arg(z) = -\frac{\pi}{2}, \quad a = 0, b < 0")
    if x>0 and y==0:
        st.markdown("+ **Caso 3:**")
        st.latex(r"\arg(z) = 0, \quad a > 0, b = 0")
    if x<0 and y==0:
        st.markdown("+ **Caso 4:**")
        st.latex(r"\arg(z) = \pi, \quad a < 0, b = 0")
    if x>0 and y>0:
        st.markdown("+ **Caso 5: cuadrante I**")
        st.latex(r"\arg(z) = \tan^{-1}\left(\frac{b}{a}\right), \quad a > 0, b > 0")
    if x<0 and y<0:
        st.markdown("+ **Caso 6: cuadrante III**")
        st.latex(r"\arg(z) = -\pi + \tan^{-1}\left(\frac{b}{a}\right), \quad a < 0, b < 0")
    if x>0 and y<0:
        st.markdown("+ **Caso 7: cuadrante IV**")
        st.latex(r"\arg(z) = \tan^{-1}\left(\frac{b}{a}\right), \quad a > 0, b < 0")
    if x<0 and y>0:
        st.markdown("+ **Caso 8: cuadrante II**")
        st.latex(r"\arg(z) = \pi + \tan^{-1}\left(\frac{b}{a}\right), \quad a < 0, b > 0")
st.divider()

with st.container(border=True):
    st.subheader(":violet[Forma Trigonométrica y Polar]")
    c1,c2= st.columns([1,1],vertical_alignment="top")
    with c1:
        st.image("https://img.sangakoo.com/img/img/polar.gif")
    with c2:
        st.markdown("""
        Teniendo en cuenta la  **magnitud** y **argumento** de un número complejo, la **Forma Trigonométrica** se define como: 
        """)
        st.latex(r"a = |z| \cos\alpha, \quad b = |z| \sin\alpha")
        st.latex(r"z = |z| (\cos\alpha + i\sin\alpha)")
        st.markdown("Asimismo, por la contribución de Leonhard Euler y la fórmula de Euler, surge la **Forma Polar** de un número complejo:")    
        st.latex(r"e^{i\alpha} = \cos\alpha + i\sin\alpha")
        st.latex(r"z = |z| e^{i\alpha}")
st.markdown("**EJEMPLOS**")
st.markdown("""
1. Observa 
""")
w1,w2,w3=st.columns([1,1,1])
with w1:
    st.markdown(":violet[**Forma Polar**]")
    st.latex(r"z = 5e^{i\pi/3} \\")    
    st.latex(r"z = 4e^{i\pi/4} \\")
    st.latex(r"z = 2e^{i\pi/2} \\ ")
with w2:
    st.markdown(":violet[**Forma Trigonométrica**]")
    st.latex(r"z = 5 \left( \cos\left(\frac{\pi}{3}\right) + i\sin\left(\frac{\pi}{3}\right) \right) \\")
    st.latex(r"z = 4 \left( \cos\left(\frac{\pi}{4}\right) + i\sin\left(\frac{\pi}{4}\right) \right) \\")
    st.latex(r"z = 2 \left( \cos\left(\frac{\pi}{2}\right) + i\sin\left(\frac{\pi}{2}\right) \right)")
with w3:
    st.markdown(":violet[**Forma Binómica**]")
    a=st.latex(r"z \approx 2.5 + 4.33i\\")
    b=st.latex(r"z \approx 2.83 + 2.83i")
    c=st.latex(r"z = 0 + 2i ")
