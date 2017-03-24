class Weather:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def spread(self, min_t, max_t):
        return max_t - min_t

    def open_file(self):
        for row in open(self.filename, 'r'):
            self.data.append(row)
        self.data = [datum for datum in self.data if datum != '\n']
        self.data = [datum.replace("\n", "").strip().split(" ") for datum in self.data]
        data = []
        for lst in self.data:
            row = [datum for datum in lst if datum != ""]
            data.append(row)
        self.data = data
        return self.data



