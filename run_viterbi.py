try:
    from IPython import embed
except:
    pass

import sys
from viterbi import Viterbi

class run_viterbi(object):
    def __init__(self, data, hmm, verbose):
        self.data = data
        self.hmm = hmm
        self.run_viterbi(verbose)

    def run_viterbi(self, verbose):
        data = self.data
        hmm = self.hmm
        viterbi = Viterbi(hmm)

        #Start probabilitites
        print "Start probabilities:"
        for state in data.statekeys:
            print state, ':\t', "{0:.3f}".format(hmm.start_prob(state))

        #Transition probabilities
        print "\nTransition probabilities:"

        for state in data.states:
            sys.stdout.write('\t' + state)
        sys.stdout.write('\n')
        sys.stdout.flush()
        for from_state in data.states:
            sys.stdout.write(from_state + ' :')
            for to_state in data.states:
                sys.stdout.write('\t' + "{0:.3f}".format(hmm.trans_prob(from_state, to_state)))
            sys.stdout.write('\n')
            sys.stdout.flush()

        #Output probabilities
        print "\nOutput probabilities:"

        print_outputs = (len(data.outputs) < 30) or verbose

        if not print_outputs:
            print "*" * 32
            print "Too many outputs to display... Still Calculating the outputs"
            print "Run with '-v' to see all outputs"
            print "*" * 32

        if print_outputs:
            for output in sorted(data.outputs):
                sys.stdout.write('\t' + output)
        if print_outputs:
            sys.stdout.write('\n')
            sys.stdout.flush()

        for state in data.states:
            sys.stdout.write(state + ' :')
            for output in sorted(data.outputs):
                out_prob = hmm.output_prob(state, output)
                if print_outputs:
                    sys.stdout.write('\t' + "{0:.3f}".format(out_prob))
            if print_outputs:
                sys.stdout.write('\n')
                sys.stdout.flush()

        #Most likely sequence
        overall_error = 0
        for i, sequence in enumerate(data.testing.sequences):
            print_mls = (i < 4) or verbose
            if (i == 4) and not verbose:
                print ""
                print "*" * 32
                print "There are too many sequences to display... Calculating"
                print "Run with '-v' to see all outputs"
                print "*" * 32

            outputs = sequence.outputs()
            inputs = sequence.inputs()
            _, mls = viterbi.most_likely_sequence(outputs)

            if print_mls:
                print "\nMost likely sequence #"+str(i)+":"
                print 'input\tcalc\toutput'

            errors = 0
            inputs_len = len(inputs)
            for i in range(inputs_len):
                if print_mls:
                    print inputs[i], '\t', mls[i], '\t', outputs[i]
                if inputs[i] != mls[i]:
                    errors += 1
                else:
                    pass

            error_percentage = errors/float(inputs_len)
            if print_mls:
                print 'Errors:', errors, '/', len(inputs), '=', error_percentage
            overall_error += error_percentage / \
                    float(len(data.testing.sequences))

        correct_percent = 1 - overall_error
        print "\nThe overall percent correct is " + \
                "{0:.3f}".format(correct_percent) + "%"
