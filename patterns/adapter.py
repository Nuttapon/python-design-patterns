class EuropeanSocketInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass


# Adaptee
class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Target interface
class USASocketInterface(EuropeanSocketInterface):
    pass


# The Adapter
class Adapter(Socket, USASocketInterface):
    def voltage(self):
        return Socket.voltage(self)


# Client
class ElectricKettle:
    def __init__(self, power: USASocketInterface):
        self.power = power

    def boil(self):
        voltage = self.power.voltage()
        if voltage > 110:
            print("Kettle on fire!")
        elif voltage == 110:
            print("Coffee time!")
        else:
            print("No power.")


def main():
    # Plug in
    adapter = Adapter()

    # Make coffee
    kettle = ElectricKettle(adapter)
    kettle.boil()

    return 0


if __name__ == "__main__":
    main()
