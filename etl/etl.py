import soap_client
import transformers
import load
import pickle

# for the transformers I need to create a string 
#to call specific functions depending on the 

def controller(wsdl: str, service_method: str, fields: list, transformation, db_table_name: str,index: bool ,**kwargs):
    print(f">>> Connecting to: {service_method}")
    
    

    # 1. Extract
    
    raw_data = soap_client.extract_soap(wsdl, service_method, **kwargs)
    
    if not raw_data:
        print(">>> No data returned from service.")
        return

    print(f">>> Retrieved {len(raw_data)} records.")

    # 2. Transform
    print(">>> transforming using {} methods")

#    return clean_data

    clean_data = transformation(raw_data,fields)

    db_name = "agro.db"
    # using pandas to upload to the sqlite3 database
    load.update_database(clean_data,db_table_name,index,db_name)

    print(f">>> Done! database uploaded")

def tester(wsdl: str, service_method: str, fields: list, transformation, db_table_name: str,index: bool ,**kwargs):
    
    print(f">>> Connecting to: {service_method}")
    
    

    # 1. Extract
    
    with open('soap_sipsa.pkl', 'rb') as file_handle:
        raw_data = pickle.load(file_handle)
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
   
    if not raw_data:
        print(">>> No data returned from service.")
        return

    print(f">>> Retrieved {len(raw_data)} records.")

    # 2. Transform
    print(">>> transforming using {} methods")

#    return clean_data

    
    clean_data = transformation(raw_data,fields)

    db_name = "test.db"
    # using pandas to upload to the sqlite3 database
    load.update_database(clean_data,db_table_name,index,db_name)

    print(f">>> Done! database uploaded")



