from coapthon.client.helperclient import HelperClient

def runMethod(method):
    if method  == 'GET' : 
        client.get(path) 
        pass
    elif method == 'POST': 
        client.post(path,payload=input("Payload: "))
        pass
    elif method == 'PUT': 
        client.put(path,payload=input("Payload: "))
        pass
    elif method == 'DELETE': 
        client.delete(path)
        pass
    else : 
        print("INVALID METHOD")

while True:
    method = input("METHOD: ").upper()
    path = input("PATH: ")
    client = HelperClient(server=('127.0.0.1', 5683)) # WAIT!!! IS THE IP SET CORRECTLY?
    runMethod(method)
    client.stop()
    


