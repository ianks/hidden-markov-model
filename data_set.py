try:
    from IPython import embed
except:
    pass

class DataSet(object):
    def __init__(self, file, sequence_delimiter):
        self.file = file
        self.set_delimiter = '..'
        self.sequence_delimiter = sequence_delimiter
        self.sets = self._parse_sets()
        self.data = None

    def _parse_sets(self):
        sets = open(self.file).read().split(self.set_delimiter)
        return map(self._parse_sequences, sets)

    def _parse_sequences(self, sets):
        return sets.split(self.sequence_delimiter)

    def training(self):
        return self.data[0]

    def testing(self):
        return self.data[1]

class Robot(DataSet):
    def __init__(self, file, sequence_delimiter):
        DataSet.__init__(self, file, sequence_delimiter)
        self.data = self.split_sequences()

    def _create_pair(self, val):
        if val == '': return

        input, output = val.split(' ')
        x, y = input.split(':')
        point = (x, y)

        return Pair(point, output)

    def split_sequences(self):
        sets = []

        for set in self.sets:
            sequences = []

            for seq in set:
                paired_seq = map(self._create_pair, seq.splitlines())
                sequences.append(paired_seq)

            sequences.pop()
            sets.append(sequences)

        return sets

class Pair(object):
    def __init__(self, input, output):
        self.input = input
        self.output = output

data = Robot('data/robot_no_momemtum.data', '.')
