"""
Python中的赋值语句, 应该始终先读右边。 
对象先在右边创建或者获取，然后左边的变量才会绑定到对象上去。
"""
"""
! 可变形参可能导致问题. Bus类接受一个可变形参列表, bus1增加的元素, 结果出现到了bus2中
del 语句只能删除引用,而不是对象, 当对象的引用计数归零后, 将会被垃圾回收.
"""
class Bus:

    def __init__(self, aPassengers = []) -> None:
        self.passenger = aPassengers
    
    def pick(self, aPassenger):
        self.passenger.append(aPassenger)
    
    def drop(self, aPassenger):
        self.passenger.pop(aPassenger)


class OptimizedBus:

    def __init__(self, aPassengers = None) -> None:
        if aPassengers is None:
            self.passenger = []
        else:
            self.passenger = list(aPassengers)


def main():
    busOne = Bus()
    busOne.pick("Duke")
    busTwo = Bus()
    print(busTwo.passenger)

if __name__ == '__main__':
    main()
