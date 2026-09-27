# Infrastructure Monitor

Projeto prático desenvolvido em Python para monitoramento de máquinas Linux através de conexão SSH.

A aplicação estabelece uma conexão SSH com um servidor Linux e coleta informações básicas do sistema, exibindo os resultados localmente no terminal.

## Status

Versão inicial concluída.

## Tecnologias

* Python
* Paramiko
* SSH
* Linux
* Git/GitHub

## Funcionalidades

* Conexão SSH com servidor Linux
* Entrada do IP do servidor pelo usuário
* Entrada do usuário SSH pelo usuário
* Solicitação segura da senha sem exibição no terminal
* Tratamento de erro para senha incorreta
* Coleta do hostname do servidor
* Coleta do uptime do servidor
* Coleta de informações de memória RAM
* Coleta de informações de armazenamento em disco
* Identificação da quantidade de CPUs disponíveis

## Como executar

Instale a dependência:

```bash
python -m pip install paramiko
```

Execute o projeto:

```bash
python main.py
```

Informe o IP, usuário SSH e senha do servidor quando solicitado.

## Exemplo de uso

```text
Digite o IP do servidor: 192.168.0.11
Digite o usuário SSH: vboxuser
Digite a senha do servidor:

Conexão SSH realizada com sucesso!
Hostname do servidor: VMLinux
Uptime do servidor: 20:11:39 up 12 min, 2 users, load average: 0.06, 0.37, 0.45
Memória RAM:
...
Disco:
...
CPUs: 2
```

## Objetivo

Projeto desenvolvido como prática de Python aplicado a cenários de infraestrutura, automação e administração de sistemas, utilizando uma máquina Linux em ambiente de laboratório para simular o monitoramento de um servidor remoto.
