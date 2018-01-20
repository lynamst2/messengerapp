import socketserver


class MessageHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            self.data = self.rfile.readline().strip()
            print(self.data)

            if self.data == b'kill':
                break


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MessageHandler) as server:
        server.serve_forever()
