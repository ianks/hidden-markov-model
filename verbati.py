try:
    from IPython import embed
except:
    pass

class Verbati(object):
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
