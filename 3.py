class Networkconnection:
    def connect(self):
        pass
class LTEConnection(Networkconnection):
    def connect(self):
        return 'LTE'
class WiFiConnection(Networkconnection):
    def connect(self):
        return 'WiFi'
class SatteliteConnection(Networkconnection):
    def sat_connection(self):
        return "sattelite connection"
