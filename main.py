import streamlit as st

p = st.Page("pag/principal.py", title="Introducción: números complejos", icon=":material/favorite:")
n = st.Page("pag/plano.py", title="Plano complejo", icon=":material/favorite:")
o = st.Page("pag/operacion.py", title="Operaciones", icon=":material/favorite:")
e = st.Page("pag/ejemplo.py", title="Ejemplos", icon=":material/favorite:")
t = st.Page("pag/test.py", title="Test", icon=":material/favorite:")
t2 = st.Page("pag/test2.py", title="Test 2", icon=":material/favorite:")
q = st.Page("pag/presentacion.py", title="¿Quién soy?", icon=":material/favorite:")
pg = st.navigation({"Teoria":[p, n, o], "Test": [t], "Creadora": [q]})

pg.run()

