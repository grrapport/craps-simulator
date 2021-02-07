from game_runner import GameRunner

runner = GameRunner()
# Run through one sequence (shooter)
while runner.active:
    runner.roll()
    print(str(runner.last_roll))

