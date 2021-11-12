class Vehicle:
    def __init__(self, model, speed, seat):
        self.model = model
        self.speed = speed
        self.seat = seat

    def info(self):
        print("Model:", self.model)
        print("Speed:", self.speed)
        print("Seat:", self.seat)
