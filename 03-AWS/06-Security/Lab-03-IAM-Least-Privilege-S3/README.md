# Lab 03 - AWS IAM: Custom Policy e Princípio do Menor Privilégio para Amazon S3

| Informação | Valor |
| :--- | :--- |
| **Serviço** | AWS IAM (Identity and Access Management) & Amazon S3 |
| **Categoria** | Security, Identity & Compliance |
| **Nível** | Intermediário |
| **Certificações** | AWS Certified Security - Specialty / AWS Certified AI Practitioner / CLF-C02 |
| **Status** | 🟢 Concluído |

---

## Objetivo
Configurar uma IAM Policy customizada no formato JSON e uma IAM Role vinculada a uma instância EC2, aplicando estritamente o princípio do menor privilégio (*Least Privilege*). O objetivo é garantir que a aplicação na EC2 acesse exclusivamente para leitura um único bucket S3, bloqueando qualquer outro acesso à conta.

---

## Cenário
Foi configurado um ambiente onde uma aplicação executada em uma instância EC2 precisa consumir arquivos salvos em um bucket S3 específico. Para atender aos requisitos de segurança, a aplicação não deve utilizar credenciais fixas (*hardcoded*) e deve ter acesso restrito apenas ao bucket designado.

---

## Estrutura Configurada

* **Bucket Alvo:** `lab-sec-exclusivo-andresouza`
* **Nome da Política Customizada:** `Policy-S3-ReadOnly-Lab`
* **Nome da IAM Role:** `Role-EC2-S3-ReadOnly`
* **Entidade de Confiança:** `ec2.amazonaws.com`
* **Ações Permitidas:** `s3:ListBucket` e `s3:GetObject`

---

## Política IAM JSON (`Policy-S3-ReadOnly-Lab`)

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowListBucketOnly",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::lab-sec-exclusivo-andresouza"
        },
        {
            "Sid": "AllowGetObjectOnly",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::lab-sec-exclusivo-andresouza/*"
        }
    ]
}
Evidências do Laboratório
1. Política IAM Customizada
Criação da política JSON no IAM especificando os ARNs exatos do bucket e dos objetos.

2. IAM Role Associada à EC2
Criação e vinculação da IAM Role à instância EC2, garantindo o uso de credenciais temporárias via Instance Metadata Service (IMDS).

3. Teste de Acesso Autorizado
Validação prática via AWS CLI na EC2 confirmando a leitura com sucesso dos arquivos no bucket permitido.

4. Teste de Acesso Negado (Least Privilege)
Tentativa de acesso a outros buckets S3 da conta resultando em Access Denied, comprovando a eficácia do menor privilégio.

Serviços Utilizados
AWS IAM (Policies & Roles)

Amazon EC2

Amazon S3

Boas Práticas Aplicadas
Princípio do Menor Privilégio (Least Privilege): Restrição de escopo a nível de recurso (Resource ARN) e ações específicas (ListBucket / GetObject).

Credenciais Temporárias e Seguras: Uso de IAM Roles para instâncias EC2 através do IMDS, evitando chave de acesso fixa no código.

Validação Ativa de Segurança: Testes práticos de acesso permitido e testes de bloqueio (Access Denied).

Conhecimentos Adquiridos
Construção de políticas IAM refinadas em JSON especificando ARN de recursos.

Associação e substituição de IAM Roles em instâncias EC2 em execução.

Teste e auditoria de políticas de controle de acesso através da AWS CLI.

Próximos Laboratórios
AWS IAM Identity Center (SSO)

Cross-Account Access com IAM Roles

S3 Bucket Policies e Access Points
