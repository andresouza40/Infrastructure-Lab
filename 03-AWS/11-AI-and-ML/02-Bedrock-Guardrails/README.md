Implementação de Filtros de Segurança com Amazon Bedrock Guardrails

## 📌 Visão Geral
Neste laboratório, implementamos uma camada de **IA Responsável e Segurança (Responsible AI)** utilizando o **Amazon Bedrock Guardrails**. O objetivo foi estabelecer filtros rígidos de conteúdo, bloqueio de termos confidenciais e proteção contra vazamento de dados pessoais (PII - Personally Identifiable Information).

---

## 🛠️ Configurações Aplicadas

1. **Informações Básicas:**
   - **Nome:** `guardrail-seguranca-lab`
   - **Descrição:** Guardrail para bloqueio de palavras confidenciais e PII.
   - **Mensagem Personalizada de Bloqueio:** *"Conteúdo bloqueado pelas políticas de segurança do sistema."*

2. **Filtros de Conteúdo (Content Filters):**
   - Configurados em nível **High** para categorias nocivas: *Hate*, *Insults*, *Sexual*, e *Violence*.

3. **Filtros de Palavras e Termos (Word Filters):**
   - Habilitado filtro de profanidades (*Profanity filter*).
   - Adicionadas palavras bloqueadas customizadas: `senha` e `confidencial` (Ação: Block para entrada e saída).

4. **Filtros de Informações Sensíveis (Sensitive Information Filters / PII):**
   - Configurado bloqueio automático para o tipo de PII: **EMAIL** (Ação: Block para entrada e saída).

---

## 🔬 Testes e Validação

Durante os testes no painel do Bedrock:
- Submissões contendo os termos `senha` ou endereços de e-mail foram interceptadas com sucesso antes de serem processadas pelo modelo de fundação.
- O sistema retornou a mensagem customizada de bloqueio definida na política de segurança.

---

## 📷 Evidência
![Bedrock Guardrail Blocked](img/guardrail-blocked.png)
