from game_runner import GameRunner
from bet_types.pass_line import PassLine


def evaluate_bets(bet_list, game_run: GameRunner):
    result = 0
    for bet in bet_list:
        if bet.active:
            result += bet.evaluate(
                game_run.last_roll_dice_1,
                game_run.last_roll_dice_2,
                game_run.last_roll
            )
    return result


def remove_inactive_bets(bet_list):
    new_bet_list = []
    for bet in bet_list:
        if bet.active:
            new_bet_list.append(bet)
    return new_bet_list


runner = GameRunner()
bankroll = 0
bets = [PassLine(10, runner.come_out, )]
# Run through one sequence (shooter)
while runner.active:
    runner.roll()
    bankroll += evaluate_bets(bets, runner)
    bets = remove_inactive_bets()
    

print("This shooter netted an outcome of " + str(bankroll))




