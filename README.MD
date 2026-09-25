# Infrastructure Monitor

Projeto prático desenvolvido em Python para monitoramento de máquinas Linux através de conexão SSH.

A proposta é desenvolver, de forma incremental, um pequeno monitor de infraestrutura capaz de coletar informações de servidores e exibir seus dados localmente.

## 🚧 Status

**Em desenvolvimento — versão inicial.**

Atualmente, o projeto realiza uma conexão SSH com uma máquina Linux e trata falhas de autenticação.

## 🛠️ Tecnologias

* Python
* Paramiko
* SSH
* Linux
* Git/GitHub

## 📌 Funcionalidades atuais

* Conexão SSH com servidor Linux
* Autenticação utilizando usuário e senha
* Tratamento de erro para senha incorreta

## 🔜 Próximos passos

* Executar comandos remotamente
* Coletar informações do sistema
* Monitorar CPU, memória e armazenamento
* Verificar disponibilidade da máquina
* Registrar informações do monitoramento
* Evoluir o projeto para uma ferramenta de monitoramento de infraestrutura

## ▶️ Como executar

Instale a dependência:

```bash
python -m pip install paramiko
```

Execute o projeto:

```bash
python main.py
```

Informe os dados de acesso da máquina Linux quando solicitado.

## 🎯 Objetivo

Projeto desenvolvido como prática de Python aplicado a cenários de infraestrutura, automação e administração de sistemas.
