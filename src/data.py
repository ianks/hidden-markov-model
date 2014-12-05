class Collection(object):
    def __init__(self, file, sequence_delimiter, point_parser):
        self.file = self._sanitize_file(file)
        self.set_delimiter = '..'
        self.sequence_delimiter = sequence_delimiter
        self.point_parser = point_parser
        self.states = {}
        self.outputs = {}

        self.sets = self._create_sets()
        self.training = self.sets[0]
        self.testing = self.sets[1]
        self.unique_state_count = len(self.states)
        self.unique_outputs_count = len(self.outputs)

    def _create_sets(self):
        return [Set(s, self) for s in self._parse_raw_collection()]

    def _parse_raw_collection(self):
        return self.file.split(self.set_delimiter)

    def _sanitize_file(self, file):
        file = open(file).read().splitlines()

        return '\n'.join(file[:-1])


class Set(object):
    def __init__(self, raw_set, collection):
        self.collection = collection
        self.sequences = self._create_sequences(raw_set)

    def _create_sequences(self, raw_set):
        return [Sequence(s, self.collection) for s in self._parse_raw_set(raw_set)]

    def _parse_raw_set(self, raw_set):
        return raw_set.split(self.collection.sequence_delimiter)


class Sequence(object):
    def __init__(self, raw_sequence, collection):
        self.collection = collection
        self.points = self._create_points(raw_sequence)

    def _create_points(self, raw_sequence):
        return [Point(p, self.collection) for p in self._parse_raw_sequence(raw_sequence) if p]

    def _parse_raw_sequence(self, raw_sequence):
        return raw_sequence.splitlines()


class Point(object):
    def __init__(self, raw_point, collection):
        self.collection = collection
        self.data = self._parse_raw_point(raw_point)

        self.input = self.data['input']
        self.output = self.data['output']

    def _parse_raw_point(self, raw_point):
        # Insert raw point into dict to ensure uniqueness
        parsed_point = self.collection.point_parser(raw_point)
        output = parsed_point['output']

        self.collection.states[raw_point] = True
        self.collection.outputs[output] = True

        return parsed_point
