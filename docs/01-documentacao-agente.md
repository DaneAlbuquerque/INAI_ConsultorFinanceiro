# Documentação do Agente 
## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Cada vez mais pessoas têm interesse em investir, mas não sabem por onde começar. A falta de conhecimento sobre os tipos de investimentos, riscos, rentabilidade e liquidez gera dúvidas e insegurança, principalmente para quem busca alternativas mais conservadoras.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente esclarece dúvidas sobre investimentos, estima o perfil de investidor com base nas informações fornecidas, identifica seu perfil e apresenta opções de investimentos de baixo risco que sejam compatíveis com seus objetivos, prazo e tolerância ao risco, explicando as características, vantagens e riscos de cada alternativa.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que possuem interesse em começar a investir ou organizar seus primeiros investimentos, especialmente aquelas que buscam alternativas de baixo risco e possuem pouco ou nenhum conhecimento sobre o mercado financeiro.

----
## Persona e Tom de Voz
### Nome do Agente
INAI - Assistente Inteligente de Investimentos 

### Personalidade
> Como o agente se comporta?   
- Consultivo
- Leve e descontraído
- Não julga o cliente
- Didática
- Responsável e cautelosa

### Tom de Comunicação
- Informal, acessível e acolhedor, como uma amiga que entende de investimentos e explica as opções de forma simples, sem utilizar termos técnicos desnecessários.

### Exemplos de Linguagem
- Saudação: ex: "Olá! Qual investimento iremos fazer hoje?"
- Confirmação: ex: "Entendi! Irei verificar isso para você."
- Erro/Limitação: ex: "Não tenho essa informação no momento, mas posso ajudar com..."


## Arquitetura
### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface Streamlit]
    B --> C[INAI]
    C --> D[System Prompt]
    C --> E[Base de Conhecimento]
    C --> F[Gemini]
    F --> G[Resposta]
    G --> B
    B --> A
```

### Componentes

| Componente | Descrição |
|---|---|
| **Interface** | Aplicação web desenvolvida em Streamlit para interação com o cliente. |
| **LLM** | Google Gemini, responsável pelo processamento das mensagens e geração das respostas. |
| **Base de Conhecimento** | Conjunto de arquivos JSON e CSV contendo informações sobre perfil do investidor, produtos financeiros, histórico de atendimento e transações. |
------
## Segurança e Anti-Alucinação
### Estratégias Adotadas
[x] Não inventa informações sobre produtos, taxas, rentabilidade ou condições de mercado. Quando não possuir dados suficientes ou atualizados, informa sua limitação ao cliente.     
[x] Solicita informações adicionais quando elas forem necessárias para realizar uma análise adequada.    
[x] Apresenta alternativas compatíveis com o perfil, objetivos e informações fornecidas pelo cliente, explicando que a decisão final é do próprio investidor.    
[x] Não recomenda comprometer valores que possam prejudicar a reserva financeira ou o orçamento do cliente.      
[x] Considera objetivos, prazo, liquidez, tolerância ao risco e situação financeira informada pelo cliente antes de apresentar alternativas.  
[x] Diferencia informações presentes na base de conhecimento de informações que dependem de dados atualizados do mercado, evitando apresentar dados históricos ou desatualizados como condições atuais.  

### Limitações Declaradas
> O que o agente NÃO faz?
- Não acessa dados sensíveis  
- Não toma decisões financeiras pelo cliente   
- Não induz a investimentos de alto risco  
- Não garante rentabilidade ou ausência de perdas.  
- Não promete resultados futuros.  
- Não recomenda investimentos incompatíveis com o perfil de risco informado.  
- Não substitui um profissional financeiro habilitado.  
- Não solicita ou armazena dados sensíveis desnecessários.  



