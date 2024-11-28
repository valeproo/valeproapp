import streamlit as st

textos= st.Page("paginas/textos.py", title="TEXTOS", icon=":material/apps:")

inputs = st.Page("paginas/inputs.py", title="INPUTS")

example = st.Page("paginas/ejemplos.py", title="EJEMPLOS")

pg = st.navigation({"ELEMENTS":[textos, inputs], "EXAMPLE": [example]})

pg.run()

