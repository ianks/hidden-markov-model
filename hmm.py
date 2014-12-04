# HMM involves a hidden state that changes over time, as well as observable
# evidence that is used to make an inference about a hidden state.
#
# An HMM is define by three sets of probabilities:
#    1. Probability of observing each output o at that state:
#        - P(E[t]=o | X[t]=s)
#    2. Probability of moving from current state to every other state:
#        - P(X[t+1]=s' | X[t]=s)
#    3. Distrubution over the start state P(X[0])
