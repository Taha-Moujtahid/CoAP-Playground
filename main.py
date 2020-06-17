from coapthon.client.helperclient import HelperClient

client = HelperClient(server=('192.168.0.145', 5683)) # WAIT!!! IS THE IP SET CORRECTLY?
for i in range(0,6) :
    response = client.get('/raspberries')
    print("\n")
    pass
client.stop()