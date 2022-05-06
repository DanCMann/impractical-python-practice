class Game():
    def __init__(self):
        self.running = True

    def game_loop(self):
        pass

    def run(self):
        while self.running:
            self.game_loop()

    def end_game(self):
        self.running = False
        print("Ending game")