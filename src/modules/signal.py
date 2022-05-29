class connection:
    connected = True
    def __init__(self, callback: callable):
        self.callback = callback
        pass

    def disconnect(self):
        self.connected = False

class phxSignal:
    connections: list[connection] = []

    def __init__(self):
        pass

    def connect(self, callback: callable):
        conn = connection(callback)
        self.connections.append(conn)
        return conn

    def emit(self):
        for conn in self.connections:
            if conn.connected:
                conn.callback()
            else:
                self.connections.remove(conn)