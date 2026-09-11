# INAI - Consultoria de Investimentos Inteligente 🤖💰

Agente de inteligência artificial desenvolvido como projeto final do **Bootcamp Bradesco 2026**, com o objetivo de auxiliar pessoas que desejam começar a investir, oferecendo informações e orientações sobre investimentos de baixo risco de forma simples, acessível e personalizada.

---

## 📌 Sobre o projeto

Muitas pessoas têm interesse em começar a investir, mas encontram dificuldades para entender conceitos financeiros, comparar alternativas e identificar investimentos compatíveis com seu perfil.

A **INAI - Consultoria de Investimentos Inteligente** foi desenvolvida para atuar como uma assistente virtual especializada em finanças pessoais e investimentos.

A agente utiliza informações estruturadas sobre o cliente e sobre os produtos financeiros disponíveis para contextualizar as respostas e conduzir o atendimento de maneira consultiva.

O projeto também foi desenvolvido com foco em **controle de informações e prevenção de alucinações**, evitando que a IA invente características, taxas, rentabilidades ou condições de produtos que não estejam disponíveis em sua base de conhecimento.

---

## 🎯 Objetivo

Criar um agente de inteligência artificial capaz de:

- Esclarecer dúvidas sobre investimentos;
- Auxiliar iniciantes no processo de conhecimento sobre investimentos;
- Identificar informações relacionadas ao perfil do investidor;
- Considerar objetivos financeiros, prazo, liquidez e tolerância ao risco;
- Apresentar alternativas de investimentos de baixo risco compatíveis com o contexto informado;
- Utilizar uma base de conhecimento estruturada para fundamentar suas respostas;
- Recusar solicitações fora do seu escopo de atuação;
- Informar quando determinada informação não está disponível, sem inventar dados.

---

## 👤 Público-alvo

A INAI é direcionada principalmente para pessoas que:

- Desejam começar a investir;
- Possuem pouco ou nenhum conhecimento sobre investimentos;
- Buscam alternativas de menor risco;
- Têm dúvidas sobre produtos financeiros;
- Desejam compreender melhor a relação entre perfil, objetivos e investimentos.

---

## 🧠 Como a INAI funciona

O atendimento é realizado por meio de uma interface desenvolvida em **Streamlit**.

A mensagem do cliente é processada pela aplicação juntamente com:

- regras e comportamento definidos no System Prompt;
- informações disponíveis na base de conhecimento;
- contexto da conversa atual.

Esse conjunto de informações é enviado ao modelo **Google Gemini**, que interpreta o contexto e gera a resposta da INAI.

### Fluxo simplificado

```text
Cliente
   ↓
Interface Streamlit
   ↓
INAI
   ↓
System Prompt + Base de Conhecimento + Contexto
   ↓
Google Gemini
   ↓
Resposta da INAI
   ↓
Cliente
```

---

## 🏗️ Arquitetura

A arquitetura detalhada do agente está documentada em:

📄 [Documentação do Agente](docs/01-documentacao-agente.md)

Nela estão descritos:

- Caso de uso;
- Persona e tom de voz;
- Arquitetura;
- Componentes;
- Estratégias de segurança;
- Estratégias de prevenção de alucinações;
- Limitações do agente.

---

## 📚 Base de conhecimento

A INAI utiliza arquivos estruturados para fornecer contexto ao atendimento.

### Estrutura

```text
data/
├── perfil_investidor.json
├── produtos_financeiros.json
├── historico_atendimento.csv
└── transacoes.csv
```

### `perfil_investidor.json`

Contém informações relacionadas ao perfil e aos objetivos financeiros do cliente.

### `produtos_financeiros.json`

Contém informações sobre os produtos financeiros disponíveis para consulta, como categoria, risco, rentabilidade, aporte mínimo e indicação.

### `historico_atendimento.csv`

Armazena informações utilizadas para contextualizar atendimentos anteriores.

### `transacoes.csv`

Contém dados fictícios de transações financeiras utilizados para análises dentro do projeto.

> Os dados utilizados no projeto são fictícios e destinados exclusivamente à demonstração e aos testes da aplicação.

---

## 🤖 Persona da INAI

A INAI foi projetada para manter uma comunicação:

- **Consultiva**
- **Leve**
- **Descontraída**
- **Didática**
- **Acessível**
- **Não julgadora**
- **Responsável e cautelosa**

A proposta é explicar conceitos financeiros de maneira simples, evitando excesso de termos técnicos e mantendo uma comunicação próxima e acolhedora.

---

## 🛡️ Segurança e prevenção de alucinações

Um dos principais objetivos do projeto é evitar que o agente apresente informações financeiras não disponíveis em seu contexto.

Para isso, foram definidas regras para que a INAI:

- Não invente taxas ou rentabilidades;
- Não invente características de produtos financeiros;
- Informe quando uma informação não estiver disponível;
- Solicite informações adicionais quando forem necessárias;
- Considere o contexto financeiro fornecido pelo cliente;
- Não forneça senhas, credenciais ou informações sensíveis;
- Não apresente informações externas ou em tempo real como se fossem dados disponíveis;
- Não recomende investimentos incompatíveis com o perfil informado;
- Não garanta rentabilidade ou resultados futuros.

A documentação completa dessas estratégias está disponível em:

📄 [Segurança e Anti-Alucinação](docs/01-documentacao-agente.md)

---

## 🧪 Testes e avaliação

O projeto possui uma documentação específica para acompanhamento dos testes realizados durante o desenvolvimento.

Os testes foram utilizados para avaliar aspectos como:

- Consulta ao perfil;
- Análise de gastos;
- Consulta e comparação de investimentos;
- Continuidade do atendimento;
- Respeito ao escopo;
- Segurança;
- Uso adequado da base de conhecimento;
- Naturalidade das respostas.

Os testes também foram realizados em diferentes rodadas de refinamento do prompt, permitindo comparar o comportamento da INAI antes e depois das alterações.

📄 [Avaliação e Métricas](docs/04-metricas.md)

### Observação sobre a API

Durante o desenvolvimento foram identificadas ocorrências de indisponibilidade temporária (`503 UNAVAILABLE`) na API do modelo.

Essas ocorrências foram tratadas separadamente das falhas funcionais da aplicação, uma vez que estão relacionadas à disponibilidade do serviço externo.

A etapa de testes dependente da API permanece em andamento.

---

## 📊 Métricas de qualidade

A avaliação da INAI considera principalmente:

| Métrica           | Objetivo                                                                      |
| ----------------- | ----------------------------------------------------------------------------- |
| **Assertividade** | Verificar se o agente responde corretamente ao que foi solicitado.            |
| **Segurança**     | Verificar se o agente respeita seus limites e evita inventar informações.     |
| **Coerência**     | Verificar se as respostas são compatíveis com o contexto e perfil do cliente. |
| **Relevância**    | Verificar se a resposta atende diretamente à necessidade apresentada.         |

Os resultados e observações detalhadas estão disponíveis na documentação de métricas.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Streamlit**
- **Google Gemini**
- **Pandas**
- **JSON**
- **CSV**
- **Google Gen AI SDK**

---

## 📁 Estrutura do projeto

```text
INAI_ConsultorFinanceiro/
│
├── data/
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   ├── historico_atendimento.csv
│   └── transacoes.csv
│
├── docs/
│   ├── 01-documentacao-agente.md
│   └── 04-metricas.md
│
├── app.py
│
└── README.md
```

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/DaneAlbuquerque/INAI_ConsultorFinanceiro.git
```

### 2. Acesse a pasta do projeto

```bash
cd INAI_ConsultorFinanceiro
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da API

A aplicação utiliza uma chave de API para acessar o modelo Gemini.

Configure a variável:

```text
GEMINI_API_KEY
```

A chave deve ser armazenada de forma segura e **não deve ser adicionada diretamente ao código ou ao repositório**.

### 5. Execute a aplicação

```bash
python -m streamlit run app.py
```

Após a inicialização, o Streamlit disponibilizará a aplicação localmente.

---

## ⚠️ Limitações atuais

A INAI possui algumas limitações importantes:

- Não possui acesso a informações de mercado em tempo real;
- Não consulta cotações externas;
- Não substitui um profissional financeiro habilitado;
- Não garante resultados ou rentabilidade futura;
- Atua dentro do escopo definido para finanças pessoais e investimentos;
- Depende da disponibilidade do serviço de inteligência artificial utilizado;
- A etapa de testes da integração com o modelo ainda está em andamento.

---

## 📖 Documentação

| Documento                                                | Conteúdo                                                    |
| -------------------------------------------------------- | ----------------------------------------------------------- |
| [Documentação do Agente](docs/01-documentacao-agente.md) | Caso de uso, persona, arquitetura, componentes e segurança. |
| [Avaliação e Métricas](docs/04-metricas.md)              | Testes realizados, resultados, métricas e refinamentos.     |

---

## 🎓 Contexto acadêmico

Este projeto foi desenvolvido como **projeto final do Bootcamp Bradesco 2026**, com o objetivo de aplicar conceitos relacionados ao desenvolvimento de agentes de inteligência artificial, engenharia de prompts, processamento de contexto, utilização de dados estruturados e construção de uma interface de interação.

O projeto também foi utilizado como oportunidade para explorar, na prática, aspectos de:

- Desenvolvimento de aplicações com IA;
- Engenharia de prompts;
- Tratamento de contexto;
- Estruturação de bases de conhecimento;
- Testes de comportamento de agentes;
- Segurança e prevenção de alucinações;
- Documentação técnica.

---

## 👩‍💻 Autora

**Dayane Albuquerque Passos**

Projeto desenvolvido para fins educacionais e de portfólio.

---

## Projeto Funcionando

[🎥 Vídeo](https://drive.google.com/file/d/1WsBwOE0HAfJJennZ84ULpLbr6j_7d3c-/view?usp=sharing)

---

⭐ Obrigada por visitar o projeto!
