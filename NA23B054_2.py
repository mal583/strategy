def make_bid(self, current_value, previous_winners, previous_second_highest_bids, capital, num_bidders):
    import numpy as np
    if len(self.previous_second_highest_bids) >= 10:
        threshold = np.percentile(self.previous_second_highest_bids, 90)
        margin = 1
        if current_value > threshold + margin:
            bid = int(min(threshold + margin, current_value - 5, capital, 100))
            confidence = min(1, 0.5 + 0.5 * (current_value - threshold) / (100 - threshold))
        else:
            bid = 0
            confidence = 0
    else:
        threshold = 95
        margin = 1
        if current_value > threshold + margin:
            bid = int(min(threshold + margin, capital, 100))
            confidence = min(1, 0.5 + 0.5 * (current_value - threshold) / (100 - threshold))
        else:
            bid = 0
            confidence = 0
    return tuple(bid, confidence)
