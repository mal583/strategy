def make_bid(self, current_value, previous_winners, previous_second_highest_bids,  capital, num_bidders):
    if len(self.previous_second_highest_bids) >= 10:
        threshold = np.percentile(self.previous_second_highest_bids, 90)
    else:
        threshold = 70
    if current_value <= threshold:
        bid = 0
    else:
        bid = int(min(threshold + 1, current_value - 5, capital, 100))
    return bid
