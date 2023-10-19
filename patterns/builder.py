class Director:
    def __init__(self, builder):
        self.builder = builder

    def getCar(self):
        car = Car()

        # First goes the body
        body = self.builder.getBody()
        car.setBody(body)

        # Then engine
        engine = self.builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        wheels = [self.builder.getWheel() for _ in range(4)]
        car.attachWheels(wheels)

        return car


# The whole product
class Car:
    def __init__(self):
        self.__wheels = []
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheels(self, wheels):
        self.__wheels.extend(wheels)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d'" % self.__wheels[0].size)


class Builder:
    def getWheel(self):
        pass

    def getEngine(self):
        pass

    def getBody(self):
        pass


class JeepBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body


# Car parts
class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


def main():
    jeepBuilder = JeepBuilder()  # initializing the class

    director = Director(jeepBuilder)

    # Build Jeep
    print("Jeep")
    jeep = director.getCar()
    jeep.specification()
    print("")


if __name__ == "__main__":
    main()
