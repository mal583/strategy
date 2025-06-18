def make_bid(self, current_value, previous_winners, previous_second_highest_bids, capital, num_bidders):
    import numpy as np
    if len(self.previous_second_highest_bids) >= 10:
            threshold = np.percentile(self.previous_second_highest_bids, 90)
    else:
            threshold = 80
    margin = 1
    bid = int(min(threshold + margin, current_value, capital, 100))
    return(bid)
