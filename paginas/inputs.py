import streamlit as st

st.title("INPUTS")

name = st.text_input("Dime tu nombre <3 : ")
st.markdown(f"Holaa, {name}! ¿Que tal tu dia?")

age = st.number_input("¿Cuantos años tienes?", min_value=0, max_value=80, value=18)
st.markdown(f"WOW! {age}!")
if age>30:
    st.markdown(f"Tas vieje amigue")
else:
    st.markdown(f"Te faltan {30-age} pa los 30 :0")
    
rango = st.slider("yuca:", min_value=0, max_value=80, value=18)

st.markdown(f"{rango}")

i, f= st.slider("eee:", min_value=0, max_value=80, value=(10,30))

st.markdown(f"valor inicial= {i}")
st.markdown(f"valor final= {f}")

x = st.number_input("y = ")
y = st.number_input("x = ")

opc = st.selectbox("¿Que vai a hacer?.", options=["suma", "resta", "multiplicacion"])

if opc== "suma":
    rta= x+y
    st.markdown(f"la solucion es {rta}")
elif opc== "resta":
    rta= x-y
    st.markdown(f"la solucion es {rta}")
else:
    rta= x*y
    st.markdown(f"la solucion es {rta}")
