try:
    from IPython import embed
except:
    pass

import math as Math

class Hmm(object):

  # numStates, unique_outputs_count are integer values
  # state, output are 2D Arrays
  def __init__(self, unique_state_count, unique_outputs_count, training_set):
    # TODO
    self.unique_state_count = state_count
    self.unique_outputs_count = unique_outputs_count
    self.training_set = training_set
    self._output = output

  # Returns the log probability assigned by this HMM to a
  # transition from the dummy start state to a given state
  def log_start_prob(self, state):
    state_count = 0
    # Count the number of sequences starting with the given state
    for sequence in self.training_set:
      if sequence[0].input == state:
        state_count += 1
    # divide by the number of total sequences
    state_probability = state_count / float( len(self.training_set) )
    # Natural log that puppy and return it
    return Math.log(state_probability, 2)

  # Returns the log probability assigned by this HMM to a
  # transition from 'from_state' to 'to_state'
  def log_trans_prob(self, from_state, to_state):
    transition_from_to_count = 0
    transition_count = 0
    # For all testing sequences
    # Count the number of transitions between from_state and to State
    for sequence in self.training_set:
      for i in len(sequence)-1:
        if sequence[i].input == from_state and sequence[i+1] == to_state:
          transition_from_to_count += 1
        if sequence[i].input != sequence[i=1].input
          transition_count += 1
    # Using Laplace smoothing:
    # Divide by number of transitions from the from_state to any State
    transition_probability = (transition_from_to_count+1) / float(transition_count + self.unique_state_count)
    # Natural log that puppy and return it
    return Math.log(transition_probability, 2)

  # Returns the log probability of 'state' emitting
  # 'output'
  def log_output_prob(self, state, output):
    output_count = 0
    state_count = 0
    # For all testing sequences
    # Count number of times the output occurs for the given state
    for sequence in self.training_set:
      for point in sequence:
        if point.input == state
          state_count += 1
          if point.output == output:
            output_count += 1
    # Using Laplace smoothing:
    # Divide by the number of times the state occurs
    output_probability = (output_count + 1) / float (state_count + self.unique_outputs_count)
    # Natural log that puppy and return it
    return Math.log(output_probability, 2)
