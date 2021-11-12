from Vehicle import Vehicle


class Train(Vehicle):
    def __init__(self, model, speed, seat, train_number, train_stops, train_platform):
        super().__init__(model, speed, seat)
        self.train_number = train_number
        self.train_stops = train_stops
        self.train_platform = train_platform

    def info(self):
        super().info()
        print("Train Number:", self.train_number)
        print("Train Stops:", self.train_stops)
        print("Train Platform:", self.train_platform)
