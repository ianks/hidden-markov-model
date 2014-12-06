try:
    from IPython import embed
except:
    pass

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
        test = viterbi.most_likely_sequence(self.data.testing.sequences[0].outputs())


        #Start probabilitites
        print "Start probabilities:"

        #Transition probabilities
        print "Transition probabilities:"

        #Output probabilities
        print "Output probabilities:"

        #Most likely sequence
        print "Most likely sequence:"
