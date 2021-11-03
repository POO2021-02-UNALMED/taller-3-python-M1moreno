from televisores.tv import TV

class Control:

    def __init__(self):
        self._tv = None

    def setTv (self, tv):
        self._tv = tv

    def getTv (self):
        self.enlazar(self._tv)
        return self._tv

    def enlazar (self, tv):
        self.setTv(tv)
        self._tv.setControl(self)

    def turnOn (self):
        self._tv.turnOn()

    def turnOff (self):
        self._tv.turnOff()
        
    def canalUp (self):
        self._tv.canalUp()

    def canalDown (self):
        self._tv.canalDown()

    def volumenUp (self):
        self._tv.volumenUp()

    def volumenDown (self):
        self._tv.volumenDown()

    def setCanal (self, numero):
        self._tv.setCanal(numero)
