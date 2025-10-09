runs = int(input('Enter runs scored: '))
balls = int(input('Enter balls faced: '))
fours = int(input('Enter 4s hit: '))
sixes = int(input('Enter 6s hit: '))
print(f'''
===== BATTING STATS =====
Runs: {runs}
Balls: {balls}
Strike Rate: {round((runs/balls) * 100, 2)}
4s: {fours} ({fours*4} runs)
6s: {sixes} ({sixes*6} runs)
Boundary %: {round((fours*4 + sixes*6)*100/runs, 2)}
Singles/Doubles: {runs - (fours*4 + sixes*6)}
=========================''')