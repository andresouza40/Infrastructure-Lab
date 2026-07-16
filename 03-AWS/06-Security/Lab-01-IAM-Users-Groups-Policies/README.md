# Lab 01 - IAM Users, Grupos e Policies

| Informação | Valor |
|------------|-------|
| Serviço | AWS Identity and Access Management (IAM) |
| Categoria | Security |
| Nível | Fundamental |
| Status | ✅ Concluído |

---

# Objetivo

Implementar uma estrutura básica de gerenciamento de identidades utilizando o AWS IAM, organizando usuários em grupos e atribuindo permissões de acordo com cada função da empresa.

---

# Cenário

Foi criada uma estrutura simulando um ambiente corporativo da empresa **Atlas Network**, onde cada colaborador possui permissões específicas conforme sua responsabilidade.

A administração das permissões foi realizada através de **IAM Groups**, seguindo boas práticas recomendadas pela AWS.

---

# Estrutura criada

## Grupos

- Cloud-Administrators
- Cloud-Engineers
- Service-Desk

---

## Usuários

| Usuário | Grupo |
|----------|--------|
| andresouza.admin | Cloud-Administrators |
| andrewmartins.engineer | Cloud-Engineers |
| marysantos.support | Service-Desk |

---

# Policies aplicadas

| Grupo | Policy |
|--------|--------|
| Cloud-Administrators | AdministratorAccess |
| Cloud-Engineers | PowerUserAccess |
| Service-Desk | ReadOnlyAccess |

---

# Evidências do laboratório

## 1. Usuários IAM

Criação dos usuários que representam cada função dentro da empresa.

![](images/01-iam-users.png)

---

## 2. Grupos IAM

Organização dos usuários em grupos para facilitar o gerenciamento das permissões.

![](images/02-iam-groups.png)

---

## 3. Cloud-Administrators

Grupo responsável pela administração completa do ambiente AWS.

Policy aplicada:

- AdministratorAccess

![](images/03-cloud-administrators-policy.png)

---

## 4. Cloud-Engineers

Grupo destinado aos engenheiros responsáveis pelo gerenciamento dos recursos da infraestrutura.

Policy aplicada:

- PowerUserAccess

![](images/04-cloud-engineers-policy.png)

---

## 5. Service-Desk

Grupo destinado à equipe de suporte, permitindo apenas consultas aos recursos.

Policy aplicada:

- ReadOnlyAccess

![](images/05-service-desk-policy.png)

---

# Serviços utilizados

- AWS IAM
- IAM Users
- IAM Groups
- AWS Managed Policies

---

# Boas práticas aplicadas

- Utilização de grupos para gerenciamento das permissões.
- Usuário administrativo separado da conta Root.
- Conta Root protegida com MFA.
- Alteração obrigatória da senha no primeiro acesso.
- Separação das permissões conforme a função do colaborador.
- Utilização de AWS Managed Policies.
- Aplicação do conceito de menor privilégio.

---

# Conhecimentos adquiridos

- Criação de usuários IAM.
- Criação de grupos.
- Associação de usuários aos grupos.
- Aplicação de Policies.
- Gerenciamento centralizado de permissões.
- Conceito de RBAC (Role-Based Access Control).
- Diferença entre Root User e IAM User.

---

# Próximos laboratórios

- IAM Roles
- Policies customizadas
- IAM Identity Center
- MFA para usuários IAM
- Cross Account Access
