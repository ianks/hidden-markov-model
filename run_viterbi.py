from viterbi import Viterbi

class run_viterbi(object):
  def __init__(self, data, hmm):
    self.data = data
    self.hmm = hmm
    self.run_viterbi()

  def run_viterbi(self):
    data = self.data
    hmm = self.hmm
    viterbi = Viterbi(hmm)

    #Start probabilitites
    print "Start probabilities:"

    #Transition probabilities
    print "Transition probabilities:"

    #Output probabilities
    print "Output probabilities:"

    #Most likely sequence
    print "Most likely sequence:"
