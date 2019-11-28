
import boto3


class SSMService:

    def __init__(self, instanceID, documentName, listComands, regionName):
        self.setRegionName(regionName)
        self.setInstanceID(instanceID)
        self.setDocumentName(documentName)
        self.setListCommands(listComands)
        self.__setSSMClient('ssm', self.getRegionName())
        self.__response = {}

    def setRegionName(self, regionName):
        self.regionName = regionName

    def getRegionName(self):
        return self.regionName

    def __setSSMClient(self, serviceName, regionName):
        self.ssm_client = boto3.client(serviceName, region_name=self.regionName)

    def __getSSMClient(self):
        return self.ssm_client

    def setInstanceID(self, instanceID):
        self.instanceID = instanceID

    def getInstanceID(self):
        return (self.instanceID)

    def setDocumentName(self, documentName):
        self.documentName = documentName

    def getDocumentName(self):
        return (self.documentName)

    def setListCommands(self, listComands):
        self.listComands = listComands

    def getListCommands(self):
        return (self.listComands)

    def __setResponse(self, response):
        self.__response = response

    def getResponse(self):
        return self.__response

    def sendCommandEc2Instance(self):
        ssm_client = self.__getSSMClient()
        listCommands = self.getListCommands()
        response = ssm_client.send_command(
            InstanceIds=self.getInstanceID(),
            DocumentName=self.getDocumentName(),
            Parameters={'commands' : listCommands, 'executionTimeout':['7200']}
        )
        self.__setResponse(response)
        return self.getResponse()

    def getCommandStatusInvocation(self):
        ssm_client = self.__getSSMClient()
        command = self.getResponse()['Command']
        commandID = command['CommandId']
        instanceID = self.getInstanceID()
        pluginName = self.getDocumentName()
        response = ssm_client.get_command_invocation(CommandId=commandID,
                                                     InstanceID=instanceID,
                                                     PluginName=pluginName
                                                     )
        self.__setResponse(response)
        return self.getResponse()