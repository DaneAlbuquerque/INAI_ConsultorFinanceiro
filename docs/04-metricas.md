# Avaliação e Métricas

## Como Avaliar seu Agente
A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

-------
## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|----------|--------|--------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto | 
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

-------
### Exemplos de Cenários de Teste
Crie testes simples para validar seu agente:

#### Teste 1: Consulta de gastos
**Pergunta:** "Quanto gastei com alimentação?"  
**Resposta esperada:**   
**Resultado:** [] Correto [ ] Incorreto  

#### Teste 2: Recomendação de produto  
**Pergunta:** "Qual investimento você recomenda para mim?"  
**Resposta esperada:**  
**Resultado:** [] Correto [ ] Incorreto  
  
#### Teste 3: Pergunta fora do escopo  
**Pergunta:** "Qual a previsão do tempo?"  
**Resposta esperada:**   
**Resultado:** [] Correto [ ] Incorreto  

#### Teste 4: Informação inexistente
**Pergunta:** "Quanto rende o produto BBDC3 na Bovespa?"  
**Resposta esperada:**  
**Resultado:** [] Correto [ ] Incorreto  

-------
### Resultados
Após os testes, registre suas conclusões:

**O que funcionou bem:***  
- xxx  

**O que pode melhorar:**  
- xxx  

-------
## Métricas Avançadas (Opcional)
Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.
