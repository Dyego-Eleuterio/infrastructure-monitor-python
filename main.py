import paramiko
import getpass 

ip= input("Digite o IP do servidor: ")
usuario = input("Digite o usuário SSH: ")
senha = getpass.getpass("Digite a senha do servidor: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(
        hostname=ip,
        username=usuario,
        password=senha
)

    print("Conexão SSH realizada com sucesso!")
    stdin, stdout, stderr = ssh.exec_command("hostname")
    resultado = stdout.read().decode()
    print(f"Hostname do servidor: {resultado}")

    stdin, stdout, stderr = ssh.exec_command("uptime")
    resultado = stdout.read().decode()
    print(f"Uptime do servidor: {resultado}")

    stdin, stdout, stderr = ssh.exec_command("free -h")
    resultado = stdout.read().decode()
    print(f"Memória RAM: \n{resultado}")

    stdin, stdout, stderr = ssh.exec_command("df -h /")
    resultado = stdout.read().decode()
    print(f"Disco:\n{resultado}")

    stdin, stdout, stderr = ssh.exec_command("nproc")
    resultado = stdout.read().decode()
    print(f"CPUs: {resultado}")
          
except paramiko.AuthenticationException:
    print("Senha incorreta!")

ssh.close()
