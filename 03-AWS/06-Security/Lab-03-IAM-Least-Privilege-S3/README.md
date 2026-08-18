# Lab 03: IAM Policies Customizadas e Princípio do Menor Privilégio (Least Privilege)

Este projeto demonstra a implementação de políticas de controle de acesso refinadas utilizando o **AWS IAM (Identity and Access Management)**. O objetivo é aplicar o **Princípio do Menor Privilégio (Least Privilege)**, garantindo que uma aplicação ou entidade possua apenas as permissões estritamente necessárias para desempenhar sua função.

---

## 📐 Descrição da Solução

* **IAM Policy Customizada:** Política em formato JSON que concede permissões exclusivas de leitura (`s3:ListBucket` e `s3:GetObject`) em um único bucket S3 específico.
* **IAM Role:** Papel criado para ser assumido por instâncias EC2, eliminando a necessidade de credenciais estáticas (`Access Keys`).
* **Segurança Refinada:** Bloqueio explícito ou implícito para qualquer outro recurso ou serviço fora do escopo definido na política.

---

## 📄 Estrutura da Política JSON

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
            "Resource": "arn:aws:s3:::meu-bucket-lab-exclusivo"
        },
        {
            "Sid": "AllowGetObjectOnly",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::meu-bucket-lab-exclusivo/*"
        }
    ]
}
