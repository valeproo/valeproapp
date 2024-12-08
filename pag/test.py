import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.patches as patches
import pandas as pd 

st.title("Test")
with st.container(border=True):
    st.markdown("1. Responde las siguientes preguntas:")

    c1, c2= st.columns([1,1])
    with c1:
        st.latex(r"z_1 = 11 - 5i")
        n1 = st.number_input(" La parte real es:   ",value= 0)  
        ret1 = st.empty()
    with c2:
        st.latex(r"z_2 = -9 - i")
        n2 = st.number_input(" La parte imaginaria es:   ",value= 0)
        ret2 = st.empty()  
with st.container(border=True):  
    st.markdown("2. ¿Cuál es la forma binómica del siguiente número complejo? ")
    t1, t2, t3= st.columns(3, vertical_alignment="center")
    with t1:
        st.latex(r"z = 2e^{i\pi/2}")
    with t2:
        n3= st.number_input("la parte real es:", value=0, key="q")
        n4= st.number_input("la parte imaginaria es:", value=0, key="j")
    with t3:
        ret3=st.empty()
        ret4=st.empty()

with st.container(border=True):  
    st.markdown("3. ¿Qué representa la siguiente gráfica?")
    s1,s2= st.columns([1,1])
    with s1:
        op= ["Real puro", "Imaginario puro", "El complejo -4 + 0i", "Ninguna de las anteriores"]
        n5 = st.radio("selecciona la opcion correcta:", options=op)
        ret5= st.empty()
    with s2:
        x=[0]
        y=[-4]
        fig, ax = plt.subplots()
        ax.quiver(0,0,x[0],y[0], angles="xy", scale_units="xy", scale=1)
        ax.grid()
        ax.set_xlabel("Im(z)")
        ax.set_ylabel("Re(z)")
        ax.axhline(0,c="gray")
        ax.axvline(0,c="gray")
        ax.set_xlim(-5,5)
        ax.set_ylim(-5,5)
        st.pyplot(fig)
with st.container(border=True):
    st.markdown("4. Dado el siguiente número complejo, ¿cuál es su módulo y argumento (en radianes)?")
    c1,c2,c3= st.columns([1,1,1])
    with c1:
        st.latex("z = 3+4i")
    with c2:
        mod=st.number_input("Ingrese la norma/módulo:", value=0)
        arg=st.number_input("Ingrese el argumento (en radianes):")
    with c3:
        r6 = st.empty()
        r7 = st.empty()
with st.container(border=True):
    t1,t2= st.columns([1,1])
    with t1:
        st.markdown("5. Escribe el conjugado del siguiente número complejo")
        st.latex("-6+7i")
    with t2:
        num = st.text_input("(sin espacios)")
        r8= st.empty()
with st.container(border=True):
    q1,q2= st.columns([1,1])
    with q1:
        st.markdown("6. ¿En qué cuadrante se encuentra el siguiente número complejo?")
        st.latex("z = 7-4i")
        r9= st.empty()
    with q2:
        opi= ["I", "II", "III", "IV"]
        n0 = st.radio("Selecciona la opcion correcta:", options=opi)
with st.container(border=True):  
    st.markdown("7. ¿Qué número representa la siguiente gráfica?")
    s1,s2= st.columns([1,1])
    with s1:
        opp= ["-4-6i", "-6-4i", "6-4i", "-4+6i"]
        n9 = st.radio("selecciona la opcion correcta:", options=opp)
        r10= st.empty()
    with s2:
        x=[-4]
        y=[6]
        fig, ax = plt.subplots()
        ax.quiver(0,0,x[0],y[0], angles="xy", scale_units="xy", scale=1)
        ax.grid()
        ax.set_xlabel("Im(z)")
        ax.set_ylabel("Re(z)")
        ax.axhline(0,c="gray")
        ax.axvline(0,c="gray")
        ax.set_xlim(-8,8)
        ax.set_ylim(-8,8)
        st.pyplot(fig)
with st.container(border=True):
    s1,s2=st.columns([1,1])
    with s1:
        st.markdown("8. ¿Cuál es la forma binómica del siguiente número complejo?")
        st.latex(r"z = 2e^{i\frac{\pi}{6}}")
        
    with s2:
        op=st.selectbox("Seleciona la opción correcta:", options=["3+i","1+i","√3+i","√3-i"])
        r11=st.empty()
if st.button("Verificar"):
    ptos = 0
    if n1 == 11:
        ptos += 1
        ret1.success("Es correcto💗")
    else:
        ret1.error("Incorrecto😓")    
    if n2==-1:
        ptos+=1
        ret2.success("Es correcto💗")
    else: 
        ret2.error("Incorrecto😓")
    if n3==0:
        ptos+=1
        ret3.success("Es correcto💗")
    else: 
        ret3.error("Incorrecto😓")
    if n4==2:
        ptos+=1
        ret4.success("Es correcto💗")
    else: 
        ret4.error("Incorrecto😓")
    if n5 == op[1]:
        ptos+=1
        ret5.success("Es correcto💗")
    else:
        ret5.error("Incorrecto😓")
    if mod==5:
        ptos+=1
        r6.success("Es correcto 💗")
    else:
        r6.error("Incorrecto😓")
    if arg==0.93:
        ptos+=1
        r7.success("Es correcto 💗")
    else:
        r7.error("Incorrecto😓")
    if num=="-6-7i":
        ptos+=1
        r8.success("Es correcto 💗")
    else:
        r8.error("Incorrecto😓")
    if n0 == opi[1]:
        ptos+=1
        r9.success("Es correcto 💗")
    else:
        r9.error("Incorrecto😓")
    if n9==opp[3]:
        ptos+=1
        r10.success("Es correcto 💗")
    else:
        r10.error("Incorrecto😓")
    if op=="√3+i":
        ptos+=1
        r11.success("Es correcto 💗")
    else:
        r11.error("Incorrecto😓")
    if ptos<=3:
        st.info(f"Obtuviste {ptos} puntos😓, debes seguir practicando.")
    elif ptos<=5:
        st.info(f"Obtuviste {ptos} puntos💔, lo has hecho bien pero debes seguir practicando.")
    else:
        st.info(f"Obtuviste {ptos} puntos 💗, lo has hecho muy bien, ya eres un pro en complejos ")

