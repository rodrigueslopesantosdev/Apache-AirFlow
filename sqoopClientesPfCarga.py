from SSMService import *

listComands = ['sqoop import --connect jdbc:mysql://192.168.46.134/bases_teste --username pedd580 -password Axxiom@2019 --table cliente_pf_carga  --target-dir s3://zonas/zona_sistemas_fonte/base_teste/estruturado/cliente_pf_carga']

ssm_cliente = SSMService (['i-02ebb5de49b6298fe'], 'AWS-RunShellScript', listComands, 'us-east-1')

response = ssm_cliente.sendCommandEc2Instance()

print (response)