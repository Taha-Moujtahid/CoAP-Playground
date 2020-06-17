from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

class MonitorResource(Resource):
    def __init__(self, name="BasicResource", coap_server=None):
        super(MonitorResource, self).__init__(name, coap_server)
        self.iterator = 0

    def render_GET(self, request):
        print(request)
        self.iterator += 1
        self.payload = "Aufruf nr: "+ str(self.iterator) 
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_POST(self, request):
        res = MonitorResource()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('basic/', MonitorResource())

def main():
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print ("Server Shutdown")
        server.close()
        print ("Exiting...")

if __name__ == '__main__':
    main()