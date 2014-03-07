import sys
from math import sqrt
 
 
class Towers:
    def __init__(self, pegs: int, discs: int):
        self.towers = [[] for _ in range(pegs)]
        self.towers[0].extend(range(discs, 0, -1))
        self.count = 0
 
    def move(self, origin, destination):
        try:
            disc = self.towers[origin].pop()
        except:
            print(self.towers)
            sys.exit()
        if len(self.towers[destination]) > 0 and disc > self.towers[destination][-1]:
            raise ValueError
        else:
            self.towers[destination].append(disc)
            print("Moved disc %d from peg %d to %d" % (disc, origin, destination))
            self.count += 1
            print(self.towers)
 
def move_three_optimally(model: Towers, disc_count, source, dest, temp):
    if disc_count:
        move_three_optimally(model, disc_count-1, source, temp, dest)
        model.move(source, dest)
        move_three_optimally(model, disc_count-1, temp, dest, source)
 
def F(n):
    return (sqrt(1+8*n)-1)//2
 
def move_four_optimally(model: Towers, disc_count, peg1, peg2, peg3, peg4):
    if disc_count > 0:
        move_four_optimally(model, disc_count - F(disc_count), peg1, peg4, peg3, peg2)
        move_three_optimally(model, F(disc_count), peg1, peg2, peg3)
        move_four_optimally(model, disc_count - F(disc_count), peg4, peg2, peg3, peg1)
 
if __name__ == '__main__':
    
    num_discs = 9
    x = Towers(4, num_discs)
    move_four_optimally(x, num_discs, 0, 1, 2, 3)
print(x.count)
