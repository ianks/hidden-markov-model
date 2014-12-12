try:
    from IPython import embed
except:
    pass

import math as Math

class Hmm(object):

    # numStates, unique_outputs_count are integer values
    # state, output are 2D Arrays
    def __init__(self, data):
        self.unique_state_count = data.unique_state_count
        self.unique_outputs_count = data.unique_outputs_count
        self.training_set = data.training
        self.training_sequences = data.training.sequences
        self.states = data.statekeys
        self.transitions_probabilities = {}
        self.output_probabilities = {}
        self.from_to_trans_counts = {}
        self.from_trans_counts = {}
        self._initialize_trans_count()

    # Returns the log probability assigned by this HMM to a
    # transition from the dummy start state to a given state
    def start_prob(self, state):
        state_count = 0
        # Count the number of sequences starting with the given state
        for sequence in self.training_sequences:
            if sequence.points[0].input == state:
                state_count += 1
        # divide by the number of total sequences
        state_probability = state_count / float(len(self.training_sequences))

        return state_probability

    # cache the transition counts, running the loop only once
    def _initialize_trans_count(self):
        for sequence in self.training_sequences:
            points_len = len(sequence.points) - 1

            for i in range(points_len):
                from_state = sequence.points[i].input
                to_state = sequence.points[i+1].input
                from_to = (from_state, to_state)

                if from_to not in self.from_to_trans_counts:
                    self.from_to_trans_counts[from_to] = 1
                else:
                    self.from_to_trans_counts[from_to] = \
                            self.from_to_trans_counts[from_to] + 1

                if from_state not in self.from_trans_counts:
                    self.from_trans_counts[from_state] = 1
                else:
                    self.from_trans_counts[from_state] = \
                            self.from_trans_counts[from_state] + 1

    # Cache the trans probabilities
    def trans_prob(self, from_state, to_state):
        if from_state not in self.transitions_probabilities:
            self.transitions_probabilities[from_state] = {}

        if to_state in self.transitions_probabilities[from_state]:
            return self.transitions_probabilities[from_state][to_state]

        prob = self._trans_prob(from_state, to_state)
        self.transitions_probabilities[from_state][to_state] = prob

        return prob

    # Returns the log probability assigned by this HMM to a
    # transition from 'from_state' to 'to_state'
    def _trans_prob(self, from_state, to_state):
        transition_from_to_count = 0
        from_to = (from_state, to_state)

        # For all testing sequences
        # Count the number of transitions between from_state and to State
        if from_to in self.from_to_trans_counts:
            transition_from_to_count = self.from_to_trans_counts[from_to]
        transitions_count = self.from_trans_counts[from_state]

        # Using Laplace smoothing:
        # Divide by number of transitions from the from_state to any State
        transition_probability = (transition_from_to_count+1) / \
                float(transitions_count + self.unique_state_count)

        return transition_probability

    # Cache output probabilities
    def output_prob(self, state, output):
        if state not in self.output_probabilities:
            self.output_probabilities[state] = {}

        if output in self.output_probabilities[state]:
            return self.output_probabilities[state][output]

        prob = self._output_prob(state, output)
        self.output_probabilities[state][output] = prob

        return prob

    # Returns the log probability of 'state' emitting
    # 'output'
    def _output_prob(self, state, output):
        output_count = 0
        state_count = 0
        state_output = (state, output)

        # For all testing sequences
        # Count number of times the output occurs for the given state
        if state_output in self.training_set.state_output_counts:
            output_count = self.training_set.state_output_counts[state_output]

        # Get state count for training set
        if state in self.training_set.state_counts:
            state_count = self.training_set.state_counts[state]

        # Using Laplace smoothing:
        # Divide by the number of times the state occurs
        output_probability = (output_count + 1) / \
                float(state_count + self.unique_outputs_count)

        return output_probability
