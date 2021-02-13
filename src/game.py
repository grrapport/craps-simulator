from game_runner import GameRunner
from bet_types.pass_line import PassLine
import statistics
import multiprocessing


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


def simulate_shooter():
    runner = GameRunner()
    shooter_result = 0
    bets = [PassLine(1, runner.come_out, )]
    while runner.active:
        if runner.come_out and runner.last_roll in [2, 3, 12]:
            bets.append(PassLine(1, runner.come_out, ))
        runner.roll()
        shooter_result += evaluate_bets(bets, runner)
        bets = remove_inactive_bets(bets)
    return shooter_result


def simulate_many_shooters(queue):
    results = []
    for _ in range(1, 5000):
        results.append(simulate_shooter())
    queue.put(results)


def flatten_list_of_lists(broken):
    """
    The queue gets a response from each thread in the form of a list
    This flattens all those lists into one list for analysis
    :param broken: list of lists
    :return: list
    """
    new_list = []
    for li in broken:
        for elem in li:
            new_list.append(elem)
    return new_list


outcomes = []
roll_attempt = simulate_shooter()
q = multiprocessing.Queue()
processes = []
for _ in range(1, 100):
    proc = multiprocessing.Process(target=simulate_many_shooters, args=(q,))
    proc.start()
    processes.append(proc)

for proc in processes:
    result = q.get()
    outcomes.append(result)
for proc in processes:
    proc.join()

outcomes = flatten_list_of_lists(outcomes)
print("Mean outcome is " + str(statistics.mean(outcomes)))
print("Stdev is " + str(statistics.stdev(outcomes)))



