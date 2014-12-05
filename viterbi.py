try:
    from IPython import embed
except:
    pass

class Viterbi(object):
  def __init__(self, hmm):
    self.hmm = hmm

  # Returns the most likely state sequence for the given
  # 'output' sequence, i.e., the state sequence of the highest
  # conditional probability given the output sequence, according to
  # the hmm that was provided by the constructor. The returned
  # state sequence should have the same number of elements as the
  # given output sequence
  def mostLikelySequence(output):
    #TODO
    pass

    # Given an hmm with state space X, initial probabilities Pi transition matrix Aij that
    # is P(i<t>| i<t-1>) and observations y1....yt the most likely state sequence x1..xt
    # is calculated by:

    # v<1,i> = P(y1|i) * Pi #base case
    # v<t,i> = P(yt|i) * max(x in X)(A<x,i> * V<t-1, x>)
    # where
    # v<t,i> is the value for the most probable state sequence for t observations ending at state i
    # xt = argmax(x in X)(v<t,x>) the state at time t is the one with the max v<t,x> value\\\\\\
