class User:
    def __init__(self, name = ""):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def _str__(self):
        return"{},{}points, {}tacos left".format(self.name, self.number_of_tacos, self.score)

    def give_taco(self, tacos_given, recipient):
        # adjust my number of tacos
        if self.number_of_tacos < tacos_given:
            tacos_given = self.number_of_tacos
        self.number_of_tacos -= tacos_given

        # adjust recipient's score
        recipient.receive_tacos(tacos_given)

    def recieve_tacos(self, tacos_received):
        self.score = tacos_received