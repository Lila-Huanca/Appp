import streamlit as st
import openai

# Configuración de la API de OpenAI
openai.api_key = 's'

# Función para obtener respuestas del chatbot
def obtener_respuesta(pregunta):
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pregunta}]
    )
    return respuesta['choices'][0]['message']['content']

# Función para proporcionar recursos específicos
def proporcionar_recursos(tema):
    recursos = {
        "inglés": [
            "Duolingo: https://www.duolingo.com/",
            "BBC Learning English: https://www.bbc.co.uk/learningenglish",
            "Coursera (Inglés): https://www.coursera.org/browse/language-learning/english"
        ],
        "matemáticas": [
            "Khan Academy: https://www.khanacademy.org/math",
            "Wolfram Alpha: https://www.wolframalpha.com/",
            "Coursera (Matemáticas): https://www.coursera.org/browse/math-and-logic"
        ],
        "programación": [
            "Codecademy: https://www.codecademy.com/",
            "freeCodeCamp: https://www.freecodecamp.org/",
            "Coursera (Programación): https://www.coursera.org/browse/computer-science/mobile-and-web-development"
        ]
    }
    return recursos.get(tema.lower(), ["No tengo recursos específicos para ese tema."])

# Configuración de la interfaz de Streamlit
st.title("Chatbot de Grupo de Estudio")
st.subheader("Pregunta sobre temas de estudio y obtén recursos útiles.")

# Entrada de usuario
pregunta = st.text_input("¿Qué necesitas estudiar?")
if st.button("Enviar"):
    if pregunta:
        if "recursos" in pregunta.lower() or "enlace" in pregunta.lower():
            tema = pregunta.split()[-1]  # Suponemos que el tema es la última palabra
            recursos = proporcionar_recursos(tema)
            st.write("Recursos encontrados:")
            for recurso in recursos:
                st.write(recurso)
        else:
            respuesta = obtener_respuesta(pregunta)
            st.write(respuesta)
    else:
        st.write("Por favor, escribe una pregunta.")

st.write("Ejemplos de preguntas:")
st.write("- ¿Qué necesito estudiar para mejorar mi inglés?")
st.write("- ¿Tienes recursos para aprender matemáticas?")
st.write("- Dame enlaces para aprender programación.")
