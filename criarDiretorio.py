

from SSMService import *

listComands = ['cd C:\\', 'mkdir AirFlow_Teste']

ssm_cliente = SSMService (['i-0ee4710fba4dda678'], 'AWS-RunPowerShellScript', listComands, 'us-east-1')

response = ssm_cliente.sendCommandEc2Instance()

print (response)