
class Army:

    def __init__(self, data):
        self.strategic_map = [data[i] for i in range(1, len(data) - 1)]
        self.castle_position = data[len(data) - 1]
