"""
Given some parameters, tells you the criteria at which your animal must
perform to be above chance level, depending on chance probability.

Author: Dr. Jack Scott
Email: jack.scott2@nih.gov
"""

from scipy.stats import binom
import numpy as np

def sig_criterion(n=50,c=0.50,p=0.05):

    '''
    Define the threshold percentage level for a session of trials that performance is sigificantly better than chance.
    n: number of trials per session (default=50)
    c: probability of performance according to chance (default=0.5)
    p: significance criterion, p (default=0.05)
    '''

    n_trials = np.arange(1,n+1,1)
    for trial in n_trials:
        p_value = 1 - binom.cdf(trial - 1, n, c)
        if p_value < p:
            crit_trial = trial
            break

    crit_perc = (crit_trial/n)*100

    print('In a session of %s trials where the probability of chance is %s%%, performance is sigificantly different from chance (p<%s) at %s correct trials, or %s%% success (p=%s)'\
          %(n,c*100,p,crit_trial,crit_perc,"{:.3f}".format(p_value)))

    return crit_trial, crit_perc

# input params and run function here
crit_trial, crit_perc = sig_criterion(n=50,c=0.3,p=0.05)



