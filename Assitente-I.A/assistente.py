##Aqui será desenvolvido uam assistente de I.A com foco de ajudar em resoluções e códigos da linguagem python

## Importando modulo para interagir com sistema operacional

import os

## importando a biblioteca stremlite para criar a interface web
import  streamlit as st


# importando a classe Groq para se conectar a API Da plataforma gloq e ecessar o LLM
from groq import Groq # usando o código para se conectar a biblioteca Groq , ela acessa o servidor Groq que ai acessa as llms, e no nosso site a I.A será conectada

#Configurando a página do stremlit com titulo, icone e estado incial do side bar
st.set_page_config(
    page_title= "Assistente de I.A",
    page_icon = "🤖",
    layout = "wide",
    initial_sidebar_state = "expanded"
)


#Criando uma definição de prompt, regras de formato para as respostad da I.A
CUSTOM_PROMPT = """
Você é uma assistente de I.A, Especializado em programação, com foco em Linguagem python, tendo como objetivo ajudar usuários iniciantes a conseguir entender a lógica por trás de cada detalhe de programação
REGRSA DE OPERAÇÕES:
1. **foco em programação**: Responda apneas perguntas focadas e relacionadas a programação especificaente python, conceitos básicos como print, variaveis
    e conceitos maiores como estutura de dados, biblioetcas e frameworks, POO, entre outros, Seu foco será ajudar um iniciante a conseguir entender a lógica dos códigos, não só obter respostas.
2. ** Estrutura de Resposta**: Sempre entregue as respostas destas maneiras:
-  * **Explicação Clara**: Sempre entregue respostas claras e objetivas, com explicação conceitual sobre o tópico perguntado, Seja direto e didático.
   * **Exemplo de código**: Forneça sempre um exemplo de código funcional e comentado, explicando o que cada lnha de código está fazendo, focando no aprendizado do usuário.
   * **Detalhes do código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e funções utilizadas.
   * **Documentação e referência**: Ao final, inclua uma seção chamada " Documentação de referência" com links diretos e relevantes para a docu,mentação oficial do Python, bibliotecas e frameworks mencionados, para que o usuário possa aprofundar seu conhecimento.
3. **Clareza e precisão **: Use uma linguagem clara. Evite jargões desnecessários, Suas respostas devem ser tecnicas e precisa. 
"""
# A I.A terá que responder de acordo com as regras acima, mantendo o foco no aprendizado do usuário.

# Usando o stremlit para fazer a interface visual do site.

with st.sidebar:
    #Definindo o titulo da barra lateral
    st.title("Assistente de I.A")

    #Mostrar um texto explicativo sobre o site
    st.markdown("Um assistente de I.A focado ajudar iniciantes a aprender programação na linguagem python.")


    # Campo para inserir a chave da API Groq, dessa maneira se conectando a api e assim ao llm
    groq_api_key = st.text_input("Insira sua chave da API groq:", type = "password",
                                 help = "Para obter uma chave da API groq acesse: https://groq.com/")
    #Adicionando explicações extras e linhas na barra lateral
    st.markdown("----")
    st.markdown("Desenvolvido para auxiliar você no seu aprendizado em prgramação python -- I.A pode cometer erros, não substitua o estudo e a prática, use como apoio e aprendizado.")

    st.markdown("----")
    st.markdown("**Acesse o meu repositório no GitHub:https://github.com/joaolucas2007/Python-Aprendizado**")

    st.markdown("----")
    st.markdown("Acesse meu linkedin: www.linkedin.com/in/joao-lucas-devsql")

# Aqui acabou o sidebar, agora vamos para parte principal do site
