import streamlit as st

st.title("TEXTOS")

import streamlit as st

st.title("Valepro")
st.header("Huoli")
st.subheader("BUENAAAS")


st.markdown("""
Viva la ***yuca***, la papa, el queso y los *buñuelos*.

**VIVA LA NAVIDA Y LA PROGRAMACIÓN**

1. Yo
2. Tu

+ yuca
+ papa

:rainbow[VIVA EL PAN]
""")

st.latex("a^2 + b^2 = c^2")

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZmO1Tb0_xNRPGzCmsFixIy6JGVdUOdRNtug&s")

st.video("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D2yfkEAt2ew0&psig=AOvVaw1GnguVUzbm24bHrrnA8Vao&ust=1732738560592000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPjlwuzo-okDFQAAAAAdAAAAABAE")


with st.container(border=True):
    st.subheader("formula de estudiante")
    st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")

c1, c2= st.columns(2, vertical_alignment="center")

with c1:
    st.markdown("jejeje")
    st.title("huoli")

with c2:
    st.markdown("jijiji")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZmO1Tb0_xNRPGzCmsFixIy6JGVdUOdRNtug&s")

st.title("HUOLI")
st.slider("yuca")