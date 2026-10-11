##Aqui será desenvolvido uam assistente de I.A com foco de ajudar em resoluções e códigos da linguagem python

## Importando modulo para interagir com sistema operacional

import os

## importando a biblioteca stremlite para criar a interface web
import  stremlit as st


# importando a classe Groq para se conectar a API Da plataforma gloq e ecessar o LLM
from groq import Groq # usando o código para se conectar a biblioteca Groq , ela acessa o servidor Groq que ai acessa as llms, e no nosso site a I.A será conectada

#Configurando a página do stremlit com titulo, icone e estado incial do side bar
st.set_page_config(
    page_tittle= "Assistente de I.A",
    page_icon = "🤖",
    layout = "wide",
    initial_sidebar_state = "expanded"
)
