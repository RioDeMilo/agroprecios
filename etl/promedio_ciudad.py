import os
import sys
import etl 
from etl import soap_client
from etl import transformers
from etl import load
import etl_pickle

wsdl = 'https://appweb.dane.gov.co/sipsaWS/SrvSipsaUpraBeanService?WSDL'
service_method = "promediosSipsaCiudad"

fields = [
    "ciudad", "codProducto", "enviado", "fechaCaptura", 
    "fechaCreacion", "precioPromedio", "producto", "regId"
]

transformation = transformers.promedio_ciudad

db_table_name = "precios"
index = False


etl.controller(wsdl, service_method, fields, transformation, db_table_name, index)

#etl.tester(wsdl, service_method, fields, transformation, db_table_name, index)




###  This is the code to create the pickle file
## etl_pickle.controller(wsdl, service_method, fields, transformation, db_table_name, index)


