import win32file
import time
import logging

from server import PIPE_NAME, PIPE_HEADER_SIZE

class NamedPIPESendError(Exception):
    pass


class NamedPIPEReceiveError(Exception):
    pass


class NamedPipeFile:

    def __init__(self, aPipeName):
        self.myFileHandle = win32file.CreateFile(PIPE_NAME,
                                   win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                                   win32file.FILE_SHARE_WRITE, None,
                                   win32file.OPEN_EXISTING, 0, None)

    def Receive(self):
        try:
            data = win32file.ReadFile(self.myFileHandle, PIPE_HEADER_SIZE)
            logging.info(f"NamedPipeFile: receive data {data}")
        except Exception as err:
            raise NamedPIPEReceiveError(f"NamedPipeFile: receive data Error {err} ")
        return data

    def Send(self, aMsg):
        try:
            errCode, nBytesWritten = win32file.WriteFile(self.myFileHandle, aMsg)
        except Exception as e:
            raise NamedPIPESendError(str(e))
        if nBytesWritten != len(aMsg):
            raise NamedPIPESendError("NamedPipeFile: PIPE send data failed, try to send {}, sent {}".format(len(aMsg), nBytesWritten))
        logging.info(f"NamedPipeFile: send data {aMsg}")

def loop_send_process(aNameFileHandler):
    for i in range(1, 2):
        msg = ''.join(['////:', str(i)])
        msg = msg.encode()
        aNameFileHandler.Send(msg)
        time.sleep(2)
    loop_receive_process(aNameFileHandler)

def loop_receive_process(aNameFileHandler):
    try:
        data = aNameFileHandler.Receive()
    finally:
        try:
            win32file.CloseHandle(aNameFileHandler)
        except:
            pass

def main():
    # init logger
    logging.basicConfig(level=logging.DEBUG, datefmt="%H:%M:%S")
    # create FileHandler
    nameFileHandler = NamedPipeFile(PIPE_NAME)

    # FileHandler send data function
    loop_send_process(nameFileHandler)

    # FileHandler receive data function
    # loop_receive_process(nameFileHandler)

if __name__ == '__main__':
    main()