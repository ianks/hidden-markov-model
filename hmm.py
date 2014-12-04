try:
    from IPython import embed
except:
    pass

class Hmm(object):

  # numStates, numOutputs are integer values
  # state, output are 2D Arrays
  def __init__(self, numStates, numOutputs, state, output):
    # TODO
    self.numStates = numStates
    self.numOutputs = numOutputs
    self._state = state
    self._output = output

  # Returns the log probability assigned by this HMM to a
  # transition fromt he dummy start state to a given state
  def logStartProbability(self, state):
    #TODO
    pass

  # Returns the log probability assigned by this HMM to a
  # transition from 'fromState' to 'toState'
  def logTransProb(self, fromState, toState):
    #TODO
    pass

  # Returns the log probability of 'state' emitting
  # 'output'
  def logOutputProb(self, state, output):
    #TODO
    pass
