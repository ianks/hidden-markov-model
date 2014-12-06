try:
    from IPython import embed
except:
    pass

import sys
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
        outputs = self.data.testing.sequences[0].outputs()
        inputs = self.data.testing.sequences[0].inputs()



        #Start probabilitites
        print "Start probabilities:"
        for state in self.data.statekeys:
            print state, ':\t', "{0:.3f}".format(hmm.log_start_prob(state))


        #Transition probabilities
        print "\nTransition probabilities:"

        for state in self.data.states:
            sys.stdout.write('\t' + state)
        sys.stdout.write('\n')
        sys.stdout.flush()
        for from_state in self.data.states:
            sys.stdout.write(from_state + ' :')
            for to_state in self.data.states:
                sys.stdout.write('\t' + "{0:.3f}".format(hmm.log_trans_prob(from_state, to_state)))
            sys.stdout.write('\n')
            sys.stdout.flush()

        #Output probabilities
        print "\nOutput probabilities:"
        for output in sorted(self.data.outputs):
            sys.stdout.write('\t' + output)
        sys.stdout.write('\n')
        sys.stdout.flush()
        for state in self.data.states:
            sys.stdout.write(state + ' :')
            for output in sorted(self.data.outputs):
                sys.stdout.write('\t' + "{0:.3f}".format(hmm.log_output_prob(state, output)))
            sys.stdout.write('\n')
            sys.stdout.flush()

        #Most likely sequence
        prob, mls = viterbi.most_likely_sequence(outputs)
        print "\nMost likely sequence:"
        errors = 0
        for i in range(len(inputs)):
            print inputs[i], '\t', mls[i], '\t', outputs[i]
            if inputs[i] != mls[i]:
                errors += 1
        print 'Errors:', errors, '/', len(inputs), '=', (errors/float(len(inputs)))





