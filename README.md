**Problem Statement -** Let’s Bid  

**Overview:**
In this competition, each participant will program a trading bot that competes against other bots in a multi-round bidding game. The objective is to develop the most effective bidding strategy to maximize profit over several rounds.


**Gameplay:**
In each round, every player is given a value x_i (All x_i's are independent of each other i.e. they need not be the same for all players). 
Each x_i is drawn from a distribution (specified in the next part). 
Every player will submit a bid. Bids can be fractional as well, but must lie in the range [0, 100].
The player with the highest bid wins the item for that round. If multiple players are tied for the highest bid, all of them win the item. 
Every player receives a payoff (explained in the section below) 
Players start off with a fixed amount of capital, which gets updated according to their payoffs i.e. new capital = old capital + payoff. 
At the start of each round, players will be provided with the following information:
i. The highest and second highest bids of the previous 100 rounds
ii. The amount of capital they have left
iii. The number of players participating in that round of the auction.
Once a bot runs out of capital, it will no longer be able to participate in the future rounds in the auction.
If a player makes an illegal bid (bid > capital available, or bid does not lie in [0, min(100, capital available)]), then that player’s bid for the round will automatically be set to 0.

**Auction Variants:**
**Variant 1 -** Clock is Ticking
i. The value x_i for each player is drawn from a uniform random distribution over the range [0, 100]. All players know that the values are uniformly distributed. 

ii. Every round, a clock will tick from 100 to 0. The bots need to return a time (bid) at which they would like to stop the clock. The first 2 bots to stop the clock (highest bids) win that round of the auction.

iii. The payoff for the winners is given by 
Payoff = X - bid_i; where bid_i is the bid of the ith bot and X is the max value amongst all x_i for that round.

iv. All other players receive Payoff = 0.

**Variant 2 -** Confidence is All you need
i. The value x_i for each player is drawn from a uniform random distribution over the range [0, 100]. All players know that the values are uniformly distributed. 

ii. All the bots who wish to participate in the round need to submit a bid along with their confidence score. Confidence score signifies the bot’s confidence of winning the auction round and lies between [0.5, 1].

iii. The bots who do not wish to participate in that round, can submit their bid = 0 and confidence score = 0.

iv. The payoff for the winner is given by 
Payoff = c_i * (x_i - bid_i); where bid_i is the bid of the ith bot and c_i is the confidence score of ith bot.

v. All other bots, which participated in the round but did not win the round, receive a payoff defined by
Payoff = - (c_i * abs(x_i - bid_i))/10; where abs(y) is the absolute value of y

vi. Bots which submitted bid = 0 and confidence = 0 (i.e. did not participate in that round), receive a Payoff = 0.

**Variation 3 -** Precision Matters
i. The value x_i for each player is drawn from a uniform random distribution over the range [0, 100]. All players know that the values are uniformly distributed.

ii. The payoff for the winner is given by 
Payoff = (X - bid_i) - abs(min((bid_i - s_i), (X - bid_i))); where X is the max value amongst all x_i for that round, bid_i is the winning bid, s_i is the second highest bid and min(a, b) is the minimum of a and b.

iii. In addition to this, the second-highest bidder will have to pay (50%) of what the winner earned (or lost) i.e. for second-highest bidders, payoff is given by
Payoff = - 0.5 * abs((X - bid_i) - (bid_i - s_i)); where abs(y) is the absolute value of y.

iv. All other players receive Payoff = 0.


**Objective:**
The objective of the game is to maximise the profit over t (~10^3) rounds. Participants must design a strategy for their bot to decide on the optimal bid based on the information available during each round.  

**Strategies:**   

**Variant 1:**   

•The threshold value for bid without considering the highest and second highest bids of other contestants for the first 9 rounds is set to 80 considering the mean 
((100+0)/2 = 50) and standard deviation (√(100 − 0)^2/12 = 28.87) of uniform distribution implying 50+28.87 = 78.87 approximating it to 80 i.e. bidding higher than range containing maximum number of values.    


• From the 10th round when the highest and second highest bids of other contestants are considered, 90th percentile of the second-highest bids is taken as threshold as it is high enough and fairly competitive and preventing over-bidding and resulting in losses at the same time.   

• Margin is set to 1 so as to increase the chance of bidding a better value.    

• Bid is considered to be the minimum value amongst threshold + margin, current x_i, capital,100 to ensure that bid doesn’t exceed capital, lies within 100 and also ensuresthat payoff isn’t very less or negative.  
• Second highest bids are considered primarily to set a comparatively better threshold and a better payoff than considering bid a little higher value than highest bids which might result in over-bidding and hence poor payoff.  

**Variant 2:**  

• From the 10th round when the highest and second highest bids of other contestants are considered, 90th percentile of the second-highest bids is taken as threshold as it ishigh enough and fairly competitive and preventing over-bidding and resulting in losses at the same time.   

• Margin is set to 1 so as to increase the chance of bidding a better value.  

• When x_i is greater than threshold + margin, bid is considered to be the minimum of (threshold + margin,  x_i-5, capital,100) to ensure that the bid is less than the capital, less than 100, and also ensures that payoff isn’t very less or negative. It also ensures that I don’t bid the second highest value as that would result in a negative payoff.   

• Confidence is set as min(1, 0.5 + 0.5 * (x_i - threshold) / (100 - threshold)) in order to have in the in the interval [0.5,1] and when the value of x_i is 100 i.e. maximum value, the confidence becomes 1 implying we can bid on very confidently.    

• Setting 90 percentile over second highest bids and following the above bid algorithm ensures that I don’t end being the second highest bidder resulting in a comparatively safer play.   

• Until 9th round, the threshold is set to a very high value to ensure that it doesn’t result to be a non-winning bid and hence a negative payoff.   

**Variant 3:**  
• From the 10th round when the highest and second highest bids of other contestants are considered, 90th percentile of the second-highest bids is taken as threshold as it is high enough and fairly competitive and preventing over-bidding and resulting in losses at the same time.   

• Margin is set to 1 so as to increase the chance of bidding a better value.   

• Until 9th round threshold is set to 70 (little less than 80(mean + standard deviation)) in order to not bid the second highest bid.    

• Bid = min(threshold + 1, x_i - 5, capital, 100) only when x_i is greater than threshold else, bid is set to 0. 
