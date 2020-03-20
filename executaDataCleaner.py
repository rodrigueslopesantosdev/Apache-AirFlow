#Máquinas Linux: não é necessário configurar o serviço SSH no Linux
"""
Máquinas Windows: é necessário configurar o serviço SSH no Windows.
1- Criar o usuário ec2-user na máquina windows EC2 com a senha padrão Axxiom@2019.
2- Seguir o tutorial https://winscp.net/eng/docs/guide_windows_openssh_server#fn2
3- Não é necessário fazer a geração da chave SSH, pois já existe a chave Axxiom-virginia.pem que é
a chave autorizada para acesso as máquinas EC2 no ambiente AWS da Axxiom.

"""
import time
from SSHClient import SSHClient

hostNameIp = "172.16.50.149"
userName = "ec2-user"
passWord = "Axxiom@2019"
privateKey = "C:\\Tiago\\Chave\\Axxiom-Virginia.pem"

clientSSH = SSHClient(hostNameIp, userName, passWord, privateKey)
response = clientSSH.sshConnection()
print (response)

response = clientSSH.sshCommand("C:\\Instalacao\\DataCleaner\\DataCleaner-console.exe -job C:\\DataCleanerJobs\\Teste_Conversor_Campo_Data.analysis.xml")
print (response)
tempoEspera = 60 #segundos
time.sleep(tempoEspera)

response = clientSSH.closeSSHConnection()
print (response)

