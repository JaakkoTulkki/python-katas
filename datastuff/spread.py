class Weather:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def spread(self, min_t, max_t):
        min_t = "".join([m for m in min_t if m.isnumeric()])
        max_t = "".join([m for m in max_t if m.isnumeric()])
        return int(max_t) - int(min_t)

    def open_file(self):
        for row in open(self.filename, 'r'):
            self.data.append(row)
        self.data = [datum for datum in self.data if datum != '\n']
        self.data = [datum.replace("\n", "").strip().split(" ") for datum in self.data]
        self.data = [[d for d in datum if d != ""]for datum in self.data]

        return self.data

    def get_smallest_spread(self):
        smallest_spread = -1
        smallest = []

        for datum in self.data[1:-1]:
            min_t = datum[2]
            max_t = datum[1]
            spread = self.spread(min_t, max_t)
            if spread > smallest_spread:
                smallest = datum

        return (smallest, 1)

    def run(self):
        self.open_file()
        smallest_spread, spread = self.get_smallest_spread()

        print("On day {day} the spread was {spread}".format(**{'day': smallest_spread[1], 'spread': spread}))



if __name__ == "__main__":
    w = Weather('weather.dat')
    w.run()
