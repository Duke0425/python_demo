import win32pipe, win32file
import time
import logging

PIPE_NAME = r'\\.\pipe\scan_result_convert_pipe'
PIPE_BUFFER_SIZE = 65535
PIPE_HEADER_SIZE = 4

class NamedPipe:

    def __init__(self, aPipeName, aPipeBufferSize):
        self.myPipeBufferSize = aPipeBufferSize
        self.myNamedPIPE = win32pipe.CreateNamedPipe(aPipeName,
                                win32pipe.PIPE_ACCESS_DUPLEX,
                                win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_WAIT | win32pipe.PIPE_READMODE_BYTE,
                                win32pipe.PIPE_UNLIMITED_INSTANCES,
                                aPipeBufferSize,
                                aPipeBufferSize, 500, None
                            )
    def ConnectNamedPIPE(self):
        win32pipe.ConnectNamedPipe(self.myNamedPIPE, None)

    def Receive(self, aDataLen = None):
        try:
            data = win32file.ReadFile(self.myNamedPIPE, self.myPipeBufferSize, None)
        except:
            pass
        return data

    def Send(self, aMsg):
        win32file.WriteFile(self.myNamedPIPE, aMsg)

def loop_send_process(aNamePipe):
    aNamePipe.ConnectNamedPIPE()
    for i in range(1, 2):
        header = i.to_bytes(PIPE_HEADER_SIZE, "little", signed=False)
        data = str(i).encode()
        msg = header + data
        c = aNamePipe.Send(msg)
        # time.sleep(2)
    loop_receive_process(aNamePipe)

def loop_receive_process(aNamePipe):
    aNamePipe.ConnectNamedPIPE()
    # try:
    data = aNamePipe.Receive()
    logging.info(f"NamedPipe: receive data {data}")
    # finally:
    #     try:
    #         win32pipe.DisconnectNamedPipe(aNamePipe)
    #     except:
    #         pass
    # loop_send_process(aNamePipe)

def main():
    # init logger
    logging.basicConfig(level=logging.DEBUG, datefmt="%H:%M:%S")
    # create NamedPIPE
    namePipe = NamedPipe(PIPE_NAME, PIPE_BUFFER_SIZE)

    # NamedPIPE receive data function
    # loop_receive_process(namePipe)

    # NamedPIPE send data function
    loop_send_process(namePipe)

if __name__ == '__main__':
    main()