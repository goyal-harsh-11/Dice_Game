import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll(self, round_score=0):
        val = random.randint(1, 6)
        print(f"{self.name} rolled: {val}")
        if val == 1:
            print(f"{self.name}'s turn ended due to rolling a 1.")
            print(f"{self.name}'s score not updated")
            return
        round_score += val
        if round_score+self.score>=100:
            self.score==100
            return
        print(f"{self.name}'s current round score: {round_score}")
        ask = input("Type 'y' to gamble (roll again), 'n' to bank score: ")
        if ask.lower()== 'y':
            self.score += round_score
            print(f"{self.name}'s updated score: {self.score}")
            self.roll(round_score)

if __name__ == "__main__":
    p1 = Player("Player 1")
    p2 = Player("Player 2")
    max_score = 100
    for i in range(2):
        print(f"\nRound {i+1}:")
        if p1.score >= max_score:
            print(f"{p1.name} has reached the maximum score. Game over.")
            break
        if p2.score >= max_score:
            print(f"{p2.name} has reached the maximum score. Game over.")
            break
        p1.roll()
        p1.score = min(p1.score, max_score)
        p2.roll()
        p2.score = min(p2.score, max_score)
    print("\nFinal Scores:")
    print(f"{p1.name}: {p1.score}")
    print(f"{p2.name}: {p2.score}")
    if p1.score == p2.score:
        print("It's a tie! Both players reached the same score.")
    elif p1.score >= max_score:
        print(f"{p1.name} Wins! (Reached maximum score)")
    elif p2.score >= max_score:
        print(f"{p2.name} Wins! (Reached maximum score)")
    elif p1.score > p2.score:
        print(f"{p1.name} Wins!")
    else:
        print(f"{p2.name} Wins!")