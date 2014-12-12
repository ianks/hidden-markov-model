import sys
import math as Math

class Viterbi(object):
    def __init__(self, hmm):
        self.hmm = hmm
        self.states = hmm.states

    # Returns the most likely state sequence for the given
    # 'output' sequence, i.e., the state sequence of the highest
    # conditional probability given the output sequence, according to
    # the hmm that was provided by the constructor. The returned
    # state sequence should have the same number of elements as the
    # given output sequence

    def _init_backpointer(self, output):
        back_pointer = [{}]
        path = {}

        # Initialize base cases (t == 0)
        for state in self.states:
            back_pointer[0][state] = self.hmm.start_prob(state) * \
                    self.hmm.output_prob(state, output[0])
            path[state] = [state]

        # Normalize backpointer values
        alpha = sum(back_pointer[0].values())
        for key in back_pointer[0]:
            back_pointer[0][key] = back_pointer[0][key] / alpha

        return back_pointer, path

    def most_likely_sequence(self, output):
        lookup_lambda = lambda x: x[0]
        hmm = self.hmm
        states = self.states
        back_pointer, path = self._init_backpointer(output)

        # The cache is warm, use these
        trans_prob = hmm.transitions_probabilities
        output_prob = hmm.output_probabilities

        # Run Viterbi for t > 0
        for t in range(1, len(output)):
            back_pointer.append({})
            newpath = {}

            for state in states:
                current_max_prob = (0, None)

                for state_0 in states:
                    state_0_prob = back_pointer[t-1][state_0] * \
                            trans_prob[state_0][state]

                    if state_0_prob >= current_max_prob[0]:
                        current_max_prob = (state_0_prob, state_0)

                (prob, max_state) = current_max_prob
                newpath[state] = path[max_state] + [state]

                # output_prob is a constant wrt t, so only multiply once
                back_pointer[t][state] = prob * output_prob[state][output[t]]

            # Normalize backpointer values
            alpha = sum(back_pointer[t].values())
            for key in back_pointer[t]:
                back_pointer[t][key] = back_pointer[t][key] / alpha

            # Don't need to remember the old paths
            path = newpath

        # if only one element is observed max is sought in the initialization values
        n = t if len(output) != 1 else 0

        (prob, state) = max((back_pointer[n][state], state) for state in self.states)

        return (prob, path[state])
