from time import sleep


class Vms:
    def __init__(self):
        self.myvar = 3

    def create(self, name, count):
        print(name)
        for i in range(0, int(count)):
            print(i)
            sleep(1)