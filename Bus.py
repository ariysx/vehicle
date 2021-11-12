from typing import Any

from Vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, model, speed, seat, bus_number, bus_stops):
        # self.var -> model, speed, seat
        # inherit instruction from Vehicle class
        # self.model = model
        # self.speed = speed
        # self.seat = seat
        super().__init__(model, speed, seat)

        # adding more attributes while keeping the Vehicle attributes
        # these attributes exist only in the Bus class
        self.bus_number = bus_number
        self.bus_stops = bus_stops

    # overriding the info function from Vehicle class to print more info
    # super().info
    def info(self):
        # call info method from super() - which is Vehicle class
        super().info()
        # Adding more print steps
        print("Bus Number:", self.bus_number)
        print("Bus Stops:", self.bus_stops)
