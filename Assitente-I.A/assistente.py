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
st.title("Assistente de I.A - Aprendizado em python")

#Adicionando um texto auxiliar
st.caption("Digite sua pergunta ou dúvida para a I.A")


#Iniciando o histórico de perguntas e respostas
if "messages" not in st.session_state:
    st.session_state.messages = []

#Mostrando o histórico de perguntas e respostas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    # Assim criamos um histórico de perguntas e respostas

#Criando uma variavel cliente
client = None #None significa vazio, não tem cliente ainda conectado

#Criando um if para garantir que a chave da API foi inserida corretamente

if groq_api_key:
    try:
        #Criando o cliente groq com a chave da API fornecida
        client = Groq(api_key = groq_api_key)

    except Exception as e:
        #Exibindo erro caso não tenha chave da API ou seja a chave seja invalida
        st.sidebar.error(f"erro ao inicializar o cliente Groq: {e}")
        st.stop() # para a exeução do código

# Caso não tenha chave, mas já existam mensagens, mostrar aviso
elif st.session_state.messages:
    st.waring("Por favor, insira sua chave da API Groq para continuar a conversa.")


    # Caixa de texto do chat na página principal (fora de condicionais restritivas)
if prompt := st.chat_input("Qual sua dúvida sobre python"):

    # Se não houver cliente válido, mostrar aviso
    if not client:
        st.warning("Por favor, insira sua chave da API Groq para continuar")
        st.stop()

    # Armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Preparando a mensagem para enviar a API
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}] 
    for msg in st.session_state.messages:
        messages_for_api.append(msg)

    # Criando a resposta do assistente no chat
    with st.chat_message("assistant"):
        with st.spinner("Analisando sua pergunta.."):
            try:
                # Chama a API da Groq para gerar resposta
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model="openai/gpt-oss-120b",
                    temperature=0.7,
                    max_tokens=2048,
                )

                # Extrai a resposta gerada pela I.A
                dsa_ai_resposta = chat_completion.choices[0].message.content

                # Mostrando a resposta na tela
                st.markdown(dsa_ai_resposta)

                # Armazena a resposta do assistente no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content": dsa_ai_resposta})

            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com API da Groq: {e}")

st.markdown("""
            <div style="position: fixed; bottom: 0; width: 100%; text-align: center; background-color: #f1f1f1; padding: 10px;">
                <p style="margin: 0;">Desenvolvido por João Lucas - 2024</p>
            </div>
            """, unsafe_allow_html=True
    ) 