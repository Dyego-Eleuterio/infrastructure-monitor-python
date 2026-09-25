import paramiko

ip= "192.168.0.11"
usuario = "vboxuser"
senha = input("Digite a senha do servidor: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(
        hostname=ip,
        username=usuario,
        password=senha
)

    print("Conexão SSH realizada com sucesso!")

except paramiko.AuthenticationException:
    print("Senha incorreta!")

ssh.close()
