import json
import socketserver
import sys
import threading
import traceback
import expressions

Error = "error"
Status = "status"
workType = "workType"
EvaluateExpression = "EvaluateExpression"
Echo = "Echo"

HOST, PORT = "0.0.0.0", 9150


class IpcTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    @staticmethod
    def start_server():
        server = ThreadedTCPServer((HOST, PORT), IpcTCPRequestHandler)
        try:
            # activate the server
            server.serve_forever()
        except KeyboardInterrupt:
            sys.exit(0)

    def handle(self):
        response = {}
        # self.request is the TCP socket connected to the client
        socket = self.request
        # printing thread-ID
        cur_thread = threading.current_thread()
        print("Current Thread Name: ", cur_thread.name)
        try:
            while True:
                try:
                    data = socket.recv(4096*4096).decode('utf-8')
                    if data == '':
                        print("client socket connection closed")
                        break
                except BlockingIOError as e:
                    print("Socket BlockingIO Error ", e.__str__())
                    response[Status] = False
                    response[Error] = "Socket BlockingIO Error " + e.__str__()
                    break
                except BrokenPipeError as e:
                    print("Broken Pipe Error ", e.__str__())
                    response[Status] = False
                    response[Error] = "Broken Pipe Error " + e.__str__()
                    break
                except ConnectionResetError as e:
                    print("Socket Connection Reset Error ", e.__str__())
                    response[Status] = False
                    response[Error] = "Socket Connection Reset Error " + e.__str__()
                    break
                except ConnectionAbortedError as e:
                    print("Socket Connection Aborted ", e.__str__())
                    response[Status] = False
                    response[Error] = "Socket Connection Aborted " + e.__str__()
                    break
                try:
                    print("Data Received: ", data)
                    work_packet = json.loads(data)
                except Exception as e:
                    print("failed to convert below received data into json packet ", e.__str__())
                    print("received data: ", data)
                    continue

                processed_data = None
                if workType in work_packet and work_packet[workType] == EvaluateExpression:
                    processed_data = expressions.functions.evaluate(work_packet)

                elif workType in work_packet and work_packet[workType] == Echo:
                    processed_data = work_packet

                print(">>>>>>>> processed_data: ", processed_data)
                # sending back the processed data
                socket.sendall(bytes(str(processed_data), encoding="utf-8"))

            # exiting the server
            socket.close()
            return response
        except Exception as e:
            print(e.__str__())
            traceback.print_exc()
            print("Try reconnecting to the server")


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    IpcTCPRequestHandler.start_server()

#     # instantiate the server, and bind to localhost on port 9150
#     server = ThreadedTCPServer((HOST, PORT), IpcTCPRequestHandler)
#     # this will keep running until Ctrl-C
#     try:
#         # activate the server
#         server.serve_forever()
#     except KeyboardInterrupt:
#         sys.exit(0)




