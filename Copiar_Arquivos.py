# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:03:48 2019

@author: tiago.santos
"""

import boto3

"""Objeto para conectar ao AWS S3."""
s3_conexao = boto3.resource('s3')

"""Dicionário com os valores Bucket e Key."""
local_origem = {
        'Bucket': 'metadados',
        'Key' : 'Desenho PoC.jpg'        
        }

"""Chamada de função para copiar o arquivo de um bucket para outro."""
s3_conexao.meta.client.copy(local_origem, 'd580-teste', local_origem['Key'])