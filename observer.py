class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
        else:
            print 'Failed to add: {}'.format(observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print 'Failed to remove: {}'.format(observer)

    def notify(self):
        for o in self.observers:
            o.notify(self)

class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "DefaultFormatter: '{}' has data = {}".format(self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        print 'Here'
        try:
            self._data = int(new_value)
        except ValueError as e:
            print 'Error: {}'.format(e)
        else:
            self.notify()

class HexFormatter:
    def notify(self, publisher):
        print "HexFormatter: '{}' has now hex data = {}".format(publisher.name, hex(publisher.data))

class BinaryFormatter:
    def notify(self, publisher):
        print "BinaryFormatter: '{}' has now bin data = {}".format(publisher.name, bin(publisher.data))

def main():
    df = DefaultFormatter('test1')
    print df

    print
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print df

    print
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print df

    print
    df.remove(hf)
    df.data = 40
    print df

    print
    df.remove(hf)
    df.add(bf)

    print
    df.data = 15.8
    print df

if __name__ == '__main__':
    main()