import streamlit as st
st.title("Plano Complejo")
c1, c2= st.columns(2, vertical_alignment="center")

with c1:
    st.markdown("grafica interactiva del plano complejo")

with c2:
    st.markdown("""
    + **Parte real:** Re(z)

    + **Parte imaginaria:** Im(z)

    + **Imaginario puro:** si se cumple que Re(z) = 0

    + **Real Puro:** si se cumple que Im(z) = 0. Además, son números que van a la derecha o izquierda del eje real.
    """)