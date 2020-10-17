from Experiments.MathQuiz.DataBank import Questions

rounds = int(input("How many rounds you wish to play (Set to '-1' for unlimited): "))
chance = int(input("How many chances are you gonna be allowed to re-answer a question: "))

game = Questions(rounds, chance)
game.start_quiz()
