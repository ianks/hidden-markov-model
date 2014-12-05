from verbati import Verbati

class run_verbati(object):
  def __init__(self, data, hmm):
    self.data = data
    self.hmm = hmm
    self.run_verbati()

  def run_verbati(self):
    data = self.data
    hmm = self.hmm
    verbati = Verbati(hmm)

    #Start probabilitites
    print "Start probabilities:"

    #Transition probabilities
    print "Transition probabilities:"

    #Output probabilities
    print "Output probabilities:"

    #Most likely sequence
    print "Most likely sequence:"
