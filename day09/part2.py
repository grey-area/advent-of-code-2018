import utils

n_players, max_marble = utils.load_data()

print(utils.compute_max_score(n_players, 100*max_marble))
