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

        #Start probabilitites
        print "Start probabilities:"
        for state in self.data.statekeys:
            print state, ':\t', "{0:.3f}".format(hmm.start_prob(state))

        #Transition probabilities
        print "\nTransition probabilities:"

        for state in self.data.states:
            sys.stdout.write('\t' + state)
        sys.stdout.write('\n')
        sys.stdout.flush()
        for from_state in self.data.states:
            sys.stdout.write(from_state + ' :')
            for to_state in self.data.states:
                sys.stdout.write('\t' + "{0:.3f}".format(hmm.trans_prob(from_state, to_state)))
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
                sys.stdout.write('\t' + "{0:.3f}".format(hmm.output_prob(state, output)))
            sys.stdout.write('\n')
            sys.stdout.flush()

        #Most likely sequence
        overall_error = 0
        for i, sequence in enumerate(self.data.testing.sequences):
            outputs = sequence.outputs()
            inputs = sequence.inputs()
            prob, mls = viterbi.most_likely_sequence(outputs)

            print "\nMost likely sequence #"+str(i)+":"
            errors = 0
            print 'input\tcalc\toutput'
            inputs_len = len(inputs)
            for i in range(inputs_len):
                print inputs[i], '\t', mls[i], '\t', outputs[i]
                if inputs[i] != mls[i]:
                    errors += 1
            error_percentage = errors/float(inputs_len)
            print 'Errors:', errors, '/', len(inputs), '=', error_percentage
            overall_error += error_percentage / \
                    float(len(self.data.testing.sequences))
        correct_percent = 1 - overall_error
        print "\nThe overall percent correct is " + \
                "{0:.3f}".format(correct_percent) + "%"
