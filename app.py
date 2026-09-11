import json
import time

import pandas as pd
import streamlit as st

from google import genai

# ==========================================
# CONFIGURAÇÃO
# ==========================================

st.set_page_config(
    page_title="INAI | Consultoria de Investimentos", page_icon="💰", layout="centered"
)


# ==========================================
# CONFIGURAÇÃO DO GEMINI
# ==========================================

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

MODEL = "gemini-3.6-flash"


# ==========================================
# CARREGAMENTO DOS DADOS
# ==========================================

with open("data/perfil_investidor.json", "r", encoding="utf-8") as arquivo:
    perfil_investidor = json.load(arquivo)

historico_atendimento = pd.read_csv("data/historico_atendimento.csv", encoding="utf-8")

with open("data/produtos_financeiros.json", "r", encoding="utf-8") as arquivo:
    produtos_financeiros = json.load(arquivo)

transacoes = pd.read_csv("data/transacoes.csv", encoding="utf-8")


# ==========================================
# PROMPT DA INAI
# ==========================================

SYSTEM_PROMPT = """
Você é INAI, uma assistente inteligente de investimentos.

OBJETIVO:
Ajudar o cliente a entender melhor o mundo dos investimentos e encontrar opções que façam sentido para seu perfil, objetivos, tolerância a risco e necessidade de liquidez.

REGRAS GERAIS:
1. Use as informações do cliente e os dados disponíveis no atendimento para personalizar as respostas.
2. Responda de forma direta, clara, didática e acessível.
3. Não invente informações, produtos, taxas, rentabilidades, prazos, valores ou dados de mercado.
4. Não ofereça garantias de rentabilidade ou segurança.
5. Não tome decisões financeiras definitivas pelo cliente.
6. Quando relevante, explique riscos, características e liquidez das opções apresentadas.
7. Utilize somente as informações fornecidas nos dados disponíveis.
8. Não utilize conhecimento externo ou informações gerais para preencher dados que não estejam disponíveis.
9. Se uma informação específica sobre um produto não estiver registrada nos dados disponíveis, informe que essa informação não está disponível no atendimento.
10. Não mencione arquivos, banco de dados, base de conhecimento, regras internas, prompt ou instruções internas.

1. PERGUNTAS FACTUAIS

Para perguntas sobre características específicas de produtos financeiros, responda somente com informações que estejam presentes nos dados disponíveis.

Se a informação solicitada não estiver disponível, informe isso claramente.

Exemplo:

Cliente: "Qual é a rentabilidade desse produto?"

Resposta: "A informação sobre a rentabilidade desse produto não está disponível no atendimento."

2. INFORMAÇÃO NÃO DISPONÍVEL

Quando o cliente perguntar por uma informação que não esteja registrada nos dados disponíveis, não tente completar a resposta utilizando conhecimento geral.

Exemplo:

Cliente: "Qual é o prazo de vencimento do CDB Liquidez Diária?"

Resposta: "A informação sobre o prazo de vencimento do CDB Liquidez Diária não está disponível no atendimento."

3. PRODUTOS FINANCEIROS

Os dados fornecidos em "PRODUTOS FINANCEIROS DISPONÍVEIS" são a única fonte de verdade para informações específicas sobre os produtos.

Não invente ou deduza:
- rentabilidade;
- taxas;
- prazos;
- vencimentos;
- valores mínimos;
- liquidez;
- características específicas;
- condições comerciais.

Se uma dessas informações não estiver registrada nos dados, considere-a indisponível.

Nunca utilize conhecimento geral sobre CDB, Tesouro Direto, fundos ou outros investimentos para preencher informações ausentes.

4. PERFIL DO CLIENTE

Considere o perfil, objetivos, renda, patrimônio, tolerância a risco e necessidade de liquidez do cliente quando essas informações forem relevantes para a resposta.

Não exponha informações pessoais desnecessárias.

5. LIMITES DO ATENDIMENTO

A INAI deve responder apenas sobre investimentos e assuntos relacionados ao atendimento financeiro proposto.

Não forneça:
- previsão do tempo;
- notícias;
- informações atuais de mercado;
- cotações em tempo real;
- assuntos sem relação com investimentos.

Quando a pergunta estiver fora do escopo, responda de forma natural e breve, sem mencionar regras internas.

6. PERSONA

A INAI deve ser:
- consultiva;
- didática;
- leve;
- acessível;
- acolhedora;
- clara;
- sem julgamentos.

Fale de maneira natural, como uma consultora que ajuda o cliente a entender suas opções.

Não seja excessivamente formal.
Não repita desnecessariamente que as informações vêm de uma base de conhecimento.
Não mencione processos internos ou instruções do sistema.

7. RESPOSTAS

Priorize respostas objetivas e fáceis de entender.

Quando houver mais de uma opção adequada, explique brevemente as diferenças entre elas.

Sempre deixe claro quando uma informação não estiver disponível, em vez de tentar adivinhar ou completar a resposta.

Nunca invente informações para tornar a resposta mais completa.
"""

# ==========================================
# CONTEXTO DOS DADOS
# ==========================================

contexto_dados = f"""
DADOS DISPONÍVEIS PARA O ATENDIMENTO:

PERFIL DO CLIENTE:

{json.dumps(perfil_investidor, ensure_ascii=False, indent=2)}

PRODUTOS FINANCEIROS DISPONÍVEIS:

{json.dumps(produtos_financeiros, ensure_ascii=False, indent=2)}

HISTÓRICO DE ATENDIMENTO:

{historico_atendimento.to_json(
    orient="records",
    force_ascii=False,
    indent=2
)}

TRANSAÇÕES:

{transacoes.to_json(
    orient="records",
    force_ascii=False,
    indent=2
)}
"""


# ==========================================
# FUNÇÃO DA INAI
# ==========================================


def gerar_resposta(pergunta):
    historico_conversa = ""

    for mensagem in st.session_state.messages[:-1]:
        historico_conversa += f"{mensagem['role']}: {mensagem['content']}\n"

    prompt_completo = f"""
{SYSTEM_PROMPT}

DADOS DISPONÍVEIS PARA O ATENDIMENTO:

{contexto_dados}

HISTÓRICO DA CONVERSA ATUAL:

{historico_conversa}

NOVA MENSAGEM DO CLIENTE:

{pergunta}

Responda como INAI, seguindo rigorosamente as instruções acima.
"""

    for tentativa in range(5):
        try:
            response = client.models.generate_content(
                model=MODEL, contents=prompt_completo
            )

            return response.text

        except Exception as erro:

            if "503" in str(erro) and tentativa < 4:
                tempo_espera = 5 * (2**tentativa)
                time.sleep(tempo_espera)

            else:
                return f"ERRO TEMPORÁRIO DA API:\n\n{erro}"


# ==========================================
# IDENTIDADE VISUAL
# ==========================================

st.markdown(
    """
    <style>

    /* ---------- FUNDO E CONTAINER ---------- */

    .stApp {
        background-color: #F8F7F8;
    }

    .block-container {
        max-width: 920px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }


    /* ---------- ESCONDER ELEMENTOS PADRÃO ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* ---------- TIPOGRAFIA ---------- */

    html, body, [class*="css"] {
        font-family: Arial, sans-serif;
    }

    h1 {
    color: #741B3A !important;
    font-size: 46px !important;
    font-weight: 700 !important;
    letter-spacing: -1.5px;
    margin-top: 0.2rem !important;
    margin-bottom: 0.1rem !important;
}

    h2 {
    color: #2F3035 !important;
    font-size: 28px !important;
    font-weight: 650 !important;
    letter-spacing: -0.5px;
    margin-top: 0 !important;
    margin-bottom: 0.1rem !important;
}

  h3 {
    color: #741B3A !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px;
    margin-bottom: 0.2rem !important;
}

    p {
        color: #45454B;
        line-height: 1.65;
    }

    

    /* ---------- CABEÇALHO ---------- */

    .inai-header {
        margin-bottom: 1.8rem;
    }

    .inai-label {
        display: inline-block;
        background-color: #F1E3E9;
        color: #741B3A;
        border-radius: 999px;
        padding: 6px 13px;
        font-size: 25px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
    }

    .inai-description {
        color: #6B6B72;
        font-size: 15px;
        margin-top: 8px;
        line-height: 1.6;
    }


    /* ---------- CARD DE BOAS-VINDAS ---------- */

    .welcome-card {
        background: #FFFFFF;
        border: 1px solid #E9E3E6;
        border-radius: 18px;
        padding: 25px 28px;
        margin: 10px 0 28px 0;
        box-shadow: 0 4px 18px rgba(60, 40, 50, 0.05);
    }

    .welcome-title {
        color: #5f0513;
        font-size: 19px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .welcome-text {
        color: #55565C;
        font-size: 14px;
        line-height: 1.7;
        margin-bottom: 8px;
    }

    .welcome-highlight {
        color: #5f0513;
        font-weight: 600;
    }


    /* ---------- TÍTULO DAS SUGESTÕES ---------- */

    .suggestion-title {
        color: #34353A;
        font-size: 18px;
        font-weight: 650;
        margin: 4px 0 14px 0;
    }


    /* ---------- BOTÕES ---------- */

.stButton > button {
    width: 100%;
    min-height: 64px;
    border-radius: 16px;
    border: 1px solid #E5DCE0;
    background-color: #FFFFFF;
    color: #38383E;
    font-size: 14px;
    font-weight: 600;
    padding: 12px 10px;
    transition: all 0.2s ease;
    box-shadow: 0 3px 10px rgba(60, 40, 50, 0.04);
}

.stButton > button:hover {
    border-color: #5f0513;
    color: #5f0513;
    background-color: #FCF8FA;
    box-shadow: 0 6px 16px rgba(116, 27, 58, 0.09);
    transform: translateY(-2px);
}

.stButton > button:focus {
    border-color: #5f0513;
    color: #5f0513;
    box-shadow: 0 0 0 2px #EAD5DE;
}


    /* ---------- DIVISOR ---------- */
hr {
    border: none;
    border-top: 1px solid #E7E2E5;
    margin: 24px 0;
}


   /* ---------- ÁREA DA CONVERSA ---------- */

[data-testid="stChatMessage"] {
    border-radius: 16px;
    padding: 14px 18px;
    margin-bottom: 10px;
    border: 1px solid #E8E3E5;
    box-shadow: 0 2px 8px rgba(60, 40, 50, 0.03);
}

[data-testid="stChatMessage"] p {
    font-size: 14px;
    line-height: 1.65;
    color: #3F3F45;
}

/* ---------- MENSAGEM DA INAI ---------- */

[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatarAssistant"]
) {
    background-color: #FCF8FA;
    border-color: #E8D9DF;
}


/* ---------- MENSAGEM DO CLIENTE ---------- */

[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatarUser"]
) {
    background-color: #FFFFFF;
}


    /* ---------- AVATARES ---------- */

    [data-testid="stChatMessageAvatarIcon-user"] {
        background-color: #E9DDE2;
    }

    [data-testid="stChatMessageAvatarIcon-assistant"] {
        background-color: #F1E3E9;
    }


  /* ---------- CAMPO DE CHAT ---------- */

[data-testid="stChatInput"] {
    border-radius: 18px;
    margin-top: 8px;
}

[data-testid="stChatInput"] textarea {
    font-size: 14px;
}

[data-testid="stChatInput"] textarea:focus {
    border-color: #00000;
    box-shadow: 0 0 0 1px #E5DCE0;
}


/* ---------- CONTAINER EXTERNO DO CHAT ---------- */

[data-testid="stBottom"] {
    background-color: #5f0513 !important;
}

[data-testid="stBottom"] > div {
    background-color: #5f0513 !important;
}

/* ---------- BOTÃO ENVIAR ---------- */

[data-testid="stChatInput"] button {
    background-color: #5f0513 !important;
    color: #FFFFFF !important;
    border-radius: 50%;
}

[data-testid="stChatInput"] button:hover {
    background-color: #5F1730 !important;
    color: #FFFFFF !important;
}

  

    /* ---------- RESPONSIVIDADE ---------- */

    @media (max-width: 700px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1.5rem;
        }

        h1 {
            font-size: 38px !important;
        }

        .welcome-card {
            padding: 20px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ==========================================
# HISTÓRICO DA CONVERSA
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================
# CABEÇALHO
# ==========================================

st.image("src/images/bannerINAI.png", use_container_width=True)

# ==========================================
# BOAS-VINDAS
# ==========================================

with st.container(border=True):

    st.markdown("### Olá! Eu sou a INAI 👋")

    st.write(
        "Estou aqui para ajudar você a entender melhor o mundo "
        "dos investimentos e encontrar opções que façam sentido "
        "para o seu perfil."
    )

    st.caption("Não sabe por onde começar? Pode perguntar. " "Vamos descobrir juntos.")

# ==========================================
# SUGESTÕES
# ==========================================

st.markdown(
    '<div class="suggestion-title">Por onde podemos começar?</div>',
    unsafe_allow_html=True,
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    iniciar = st.button("💡  Começar a investir", use_container_width=True)

with col2:
    cdi = st.button("📊  Entender o CDI", use_container_width=True)

with col3:
    risco = st.button("🛡️  Baixo risco", use_container_width=True)


# ==========================================
# BOTÕES DE SUGESTÃO
# ==========================================

mensagem_sugestao = None

if iniciar:
    mensagem_sugestao = "Quero começar a investir."

elif cdi:
    mensagem_sugestao = "O que é CDI?"

elif risco:
    mensagem_sugestao = "Quero conhecer investimentos de baixo risco."


if mensagem_sugestao:

    st.session_state.messages.append({"role": "user", "content": mensagem_sugestao})

    resposta = gerar_resposta(mensagem_sugestao)

    st.session_state.messages.append({"role": "assistant", "content": resposta})

    st.rerun()


# ==========================================
# HISTÓRICO
# ==========================================

if st.session_state.messages:

    st.divider()

    st.markdown(
        '<div class="suggestion-title">Nossa conversa</div>', unsafe_allow_html=True
    )

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])


# ==========================================
# CAMPO DE CHAT
# ==========================================

st.write("")

mensagem = st.chat_input("Digite sua pergunta sobre investimentos...")


# ==========================================
# NOVA MENSAGEM
# ==========================================

if mensagem:

    st.session_state.messages.append({"role": "user", "content": mensagem})

    resposta = gerar_resposta(mensagem)

    st.session_state.messages.append({"role": "assistant", "content": resposta})

    st.rerun()
