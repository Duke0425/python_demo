from datetime import datetime
from uuid import uuid4

class TimeFormatID:

    staticFormatter = "%Y%m%d%H%M"
    staticBodyLen = 2
    staicTailStr = ""

    def __init__(self):
        self.myTimeIDHead = datetime.now().strftime(self.staticFormatter)
        self.myTimeIDBody = uuid4().hex[:self.staticBodyLen]

    def __str__(self):
        return ''.join([self.myTimeIDHead, self.myTimeIDBody, self.staicTailStr])


if __name__ == "__main__":
    c= TimeFormatID("LC")
    pass