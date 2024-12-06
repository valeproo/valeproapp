import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.patches as patches
import pandas as pd 

st.title("yuca")

x = [1,2,5,6,7]
y = [1,7,8,9,6]

fig, ax = plt.subplots()

ax.plot(x,y)
ax.grid()
ax.set_title("Plano Complejo")
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")

st.pyplot(fig)

st.divider()


x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x,y)
ax.grid()


st.pyplot(fig)

st.divider()

c1, c2= st.columns([1,3], vertical_alignment="center")
with c1:
    xin , xfin = st.slider("Intervalo", min_value=-10, max_value=10, value=(-2,2))

with c2:
    x = np.linspace(xin, xfin, 100)
    y = x**2 - 5
    fig, ax = plt.subplots()

    ax.plot(x,y)
    ax.grid()
    st.pyplot(fig)

st.divider()

puntos = pd.DataFrame({
    "x" : [1,1,-1],
    "y" : [1,-1,0.5],
})
pol = patches.Polygon(puntos, closed=True, fill=True, facecolor= "lightpink", edgecolor= "hotpink")

fig, ax = plt.subplots()
ax.add_patch(pol)

ax.set_xlim(puntos["x"].min()-1, puntos["x"].max()+1)
ax.set_ylim(puntos["y"].min()-1, puntos["y"].max()+1)

st.pyplot(fig)

st.divider()



puntos = pd.DataFrame({
    "x" : [1,1,-1],
    "y" : [1,-1,0.5],
})

puntos = st.data_editor(puntos, hide_index=True, num_rows="dynamic")

pol = patches.Polygon(puntos, closed=True, fill=True, facecolor= "lightpink", edgecolor= "hotpink")

fig, ax = plt.subplots()
ax.add_patch(pol)

ax.set_xlim(puntos["x"].min()-1, puntos["x"].max()+1)
ax.set_ylim(puntos["y"].min()-1, puntos["y"].max()+1)

st.pyplot(fig)