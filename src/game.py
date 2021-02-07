from game_runner import GameRunner

runner = GameRunner()
for i in range(0, 100):
    runner.roll()
    print(str(runner.last_roll))

