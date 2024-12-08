import streamlit as st
import streamlit as st

st.title("Creadora")
s1,s2=st.columns([1,1])
with s1:
    with st.container(border=True):
        st.subheader(":violet[Sobre mi]")
        st.write("""
        Holi, mi nombre es Vale, soy estudiante de Matemáticas. 
        Siempre me he sentido atraída por el mundo de los números, ya que creo que son la base fundamental de las ciencias y, en general, de la vida.
        """)
    st.image("https://img.freepik.com/premium-vector/cute-cartoon-cat-icon_738849-427.jpg")
with s2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8YwiJ9rlxY6dnlCa8yidBZphbeuQwPdankl-ZCXNpahnC0PYcNB__b2lYXYqEMrVtB0s&usqp=CAU")
    with st.container(border=True):
        st.subheader(":violet[Mis intereses]")
        st.write("""
        Mis intereses abarcan escuchar música, salir con amigos cercanos, ver series o animes, dibujar y, aunque no lo creas, también disfruto mucho aprendiendo y realizando ejercicios de álgebra.
        """)
with st.container(border=True):
    st.subheader(":violet[¿Qué aprendizaje le deja la materia programación I?]")
    st.write("""
    Esta asignatura me ha sorprendido bastante. Incluso, confieso que jamás me imagine disfrutarla tanto. He aprendido aspectos básicos y/o prácticos fundamentales, los cuales considero son una buena base para seguir prácticando y desempeñarme cada vez mejor. Además, a nivel general, habia olvidado que la práctica y la constancia es la base fundamental de todo, lo cual me hizo pasar malos ratos mientras realizaba mis trabajos, sin embargo, el haber corregido mi error a tiempo fue la clave para pensar como hoy lo hago sobre ésta área. 
    """)
