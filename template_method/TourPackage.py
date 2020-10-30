from abc import ABC, abstractmethod


class TourPackage(ABC):

    def hire(self):
        self.jabo()
        self.ghurbo()
        self.firbo()

    def jabo(self):
        pass

    def ghurbo(self):
        pass

    def firbo(self):
        pass


class Economy(TourPackage):

    # overriding abstract method
    def jabo(self):
        print("Bus e jabo")


    def ghurbo(self):
        print("Normal hotel")


    def firbo(self):
        print("Bus e firbo")


class Relux(TourPackage):

    # overriding abstract method
    def jabo(self):
        print("Train e jabo")


    def ghurbo(self):
        print("Five star Hotel")


    def firbo(self):
        print("Train e firbo")


class Luxury(TourPackage):

    # overriding abstract method
    def jabo(self):
        print("Air e zabo")


    def ghurbo(self):
        print("7 Star Hotel e thakbo")


    def firbo(self):
        print("Air e firbo")


class Client():
    if __name__ == '__main__':
        pack1 = Luxury()
        #pack1.ghurbo()
        pack1.hire()
