
import paramiko
import time


class SSHClient:

    def __init__(self, hostNameIp, userName, passWord, privateKey):
        self.setHostName(hostNameIp)
        self.setUserName(userName)
        self.setPassWord(passWord)
        self.setPrivateKey(privateKey)
        self.__setClientSSH()

    def __setClientSSH(self):
        self.privateKey = paramiko.RSAKey.from_private_key_file(self.getPrivateKey())
        self.__clientSSH = paramiko.SSHClient()
        self.__clientSSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def getClientSSH(self):
        return self.__clientSSH

    def setHostName(self, hostNameIp):
        self.hostNameIp = hostNameIp

    def getHostName(self):
        return self.hostNameIp

    def setPassWord(self, passWord):
        self.passWord = passWord

    def getPassWord(self):
        return (self.passWord)

    def setUserName(self, userName):
        self.userName = userName

    def getUserName(self):
        return (self.userName)

    def setPrivateKey(self, privateKey):
        self.privateKey = privateKey

    def getPrivateKey(self):
        return (self.privateKey)

    def __setResponse(self, response):
        self.__response = response

    def getResponse(self):
        return self.__response

    def sshConnection(self):
        try:
            client = self.getClientSSH()
            client.connect(hostname=self.getHostName(), username=self.getUserName(), password=self.getPassWord(),
                                     pkey=self.getPrivateKey())
            self.__setResponse("Cliente SSH conectado com sucesso ao hostname")
            return(self.getResponse())
        except Exception as e:
            self.__setResponse(e.__str__())
            print (self.getResponse())

    def sshCommand(self, command):
        try:
            client = self.getClientSSH()
            stdin, stdout, stderr = client.exec_command(command)
            #client.close()
            self.__setResponse(stdout.readlines())
            return (self.getResponse())
        except Exception as e:
            self.__setResponse(e.__str__())
            return (self.getResponse())

    # def sshCommand(self, command):
    #     chan = self.getClientSSH().invoke_shell()
    #     stdin, stdout, stderr = chan.exec_command(input(command))
    #     print(stdout.read())

    def closeSSHConnection(self):
        try:
            client = self.getClientSSH()
            client.close()
            self.__setResponse("Conexao SSH encerrada com sucesso!!")
            return (self.getResponse())
        except Exception as erroMsg:
            self.__setResponse(erroMsg.__str__())
            return (self.getResponse())