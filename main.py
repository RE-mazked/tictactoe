import random

class Game():
    
    def __init__(self):
        self.state_pos = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.tourn = 'X'
        self.fin = False
        print("Welcome to TIC TAC TOE game.")
    
    def state(self):
        for i in self.state_pos:
            for x in i:
                print(x, end='')
            print()
        state = self.check()
        if state[0]:
            self.movement()
            state = self.check()
            if state[0]:
                self.randMachine()
            self.state()
        else:
            self.fin = True
        if self.fin:
            print(f'{state[1]} Win!')
            self.stop()

    def movement(self):
        movement = input("->")
        movement = movement.split()
        if self.state_pos[int(movement[0])][int(movement[1])] == 0:
            self.state_pos[int(movement[0])][int(movement[1])] = self.tourn
        else:
            print("Please select a empty position")
            self.movement()

    def check(self):
        x = 0
        y = 0
        for z in range(3):
            if self.state_pos[z][0] == self.state_pos[z][1] and self.state_pos[z][0] == self.state_pos[z][2] and self.state_pos[z][0] != 0:
                return False, self.state_pos[z][0]
            elif self.state_pos[0][z] == self.state_pos[1][z] and self.state_pos[0][z] == self.state_pos[2][z] and self.state_pos[0][z] != 0:
                return False, self.state_pos[0][z]
        if self.state_pos[0][0] == self.state_pos[1][1] and self.state_pos[0][0] == self.state_pos[2][2] and self.state_pos[0][0] != 0:
            return False, self.state_pos[0][0]
        elif self.state_pos[0][2] == self.state_pos[1][1] and self.state_pos[0][2] == self.state_pos[2][0] and self.state_pos[1][1] != 0:
            return False, self.state_pos[0][2]
        return True, None
    
    def randMachine(self):
        i = 0
        while True:
            posX = random.randint(0, 2)
            posY = random.randint(0, 2)
            if self.state_pos[posX][posY] == 0:
                self.state_pos[posX][posY] = 'O'
                break
            if i == 10:
                print("Tablas")
                break

    def start(self):
        self.state()

    def stop(self):
        exit()
        
if __name__ == '__main__':
    game = Game()
    game.start()