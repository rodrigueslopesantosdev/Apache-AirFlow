"""
Máquinas Windows: é necessário configurar o serviço SSH no Windows.
1- Criar o usuário ec2-user na máquina windows EC2 com a senha padrão Axxiom@2019.
2- Seguir o tutorial https://winscp.net/eng/docs/guide_windows_openssh_server#fn2
3- Não é necessário fazer a geração da chave SSH, pois já existe a chave Axxiom-virginia.pem que é
a chave autorizada para acesso as máquinas EC2 no ambiente AWS da Axxiom.

"""
import time
from SSHClient import SSHClient

hostNameIp = ""
userName = ""
passWord = ""
privateKey = ""

clientSSH = SSHClient(hostNameIp, userName, passWord, privateKey)
response = clientSSH.sshConnection()
print (response)

response = clientSSH.sshCommand("sqoop import --connect jdbc:mysql://192.168.46.134/bases_teste --username pedd580 -password Axxiom@2019 --table cliente_pf_carga  --target-dir s3://zonas/zona_sistemas_fonte/base_teste/estruturado/cliente_pf_carga")
print (response)
tempoEspera=600 #segundos
time.sleep(tempoEspera)
response = clientSSH.closeSSHConnection()
print ("Comando sqoop encerrado com sucesso!")