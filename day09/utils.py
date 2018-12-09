import re


class Marble():
    def __init__(self, value):
        self.next = self
        self.prev = self
        self.value = value

    def insert_2_after(self, marble):
        insert_after = self.next

        marble.prev = insert_after
        marble.next = insert_after.next

        insert_after.next.prev = marble
        insert_after.next = marble

        return marble

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev

        return self.next

    def generate_circle(self):
        start_value = self.value
        marble = self.next
        yield start_value
        while marble.value != start_value:
            yield marble.value
            marble = marble.next


def load_data():
    with open('input') as f:
        data = f.read()

    n_players, max_marble = map(int, re.search('(\d+) .+ (\d+)', data).groups())
    return n_players, max_marble


def compute_max_score(n_players, max_marble):
    player_scores = [0] * n_players
    current_marble = Marble(0)
    zero_marble = current_marble
    player_id = 0

    for marble_id in range(1, max_marble):
        if marble_id % 23 == 0:
            player_scores[player_id] += marble_id
            for i in range(7):
                current_marble = current_marble.prev
            player_scores[player_id] += current_marble.value
            current_marble = current_marble.delete()
        else:
            current_marble = current_marble.insert_2_after(Marble(marble_id))

        player_id = (player_id + 1) % n_players

    return max(player_scores)
