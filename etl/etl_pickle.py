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

    #  Transform
    #exporting to pickle file
    print(">>> transforming using {} methods")
    with open('soap_sipsa.pkl', 'wb') as file_handle:
        pickle.dump(raw_data,file_handle)
    return

#    return clean_data

#    clean_data = transformation(raw_data,fields)


    # using pandas to upload to the sqlite3 database
#    load.update_database(clean_data,db_table_name,index)

    print(f">>> Done! database uploaded as a raw pickle file, no transformations")



