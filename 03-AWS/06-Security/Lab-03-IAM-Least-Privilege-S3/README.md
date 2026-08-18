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

## Estrutura Configurada

* **Bucket Alvo:** `lab-sec-exclusivo-andresouza`
* **Nome da Política Customizada:** `Policy-S3-ReadOnly-Lab`
* **Nome da IAM Role:** `Role-EC2-S3-ReadOnly`
* **Entidade de Confiança:** `ec2.amazonaws.com`
* **Ações Permitidas:** `s3:ListBucket` e `s3:GetObject` (Apenas no bucket e objetos delimitados)

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
