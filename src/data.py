class Collection(object):
    def __init__(self, file, sequence_delimiter, point_parser):
        self.file = self._sanitize_file(file)
        self.set_delimiter = '..'
        self.sequence_delimiter = sequence_delimiter
        self.point_parser = point_parser
        self.sets = self._create_sets()
        self.training = self.sets[0]
        self.testing = self.sets[1]

    def _create_sets(self):
        return [Set(s, self) for s in self._parse_raw()]

    def _parse_raw(self):
        return self.file.split(self.set_delimiter)

    def _sanitize_file(self, file):
        file = open(file).read().splitlines()

        return '\n'.join(file[:-1])


class Set(object):
    def __init__(self, raw, collection):
        self.collection = collection
        self.sequences = self._create_sequences(raw)

    def _create_sequences(self, raw):
        return [Sequence(s, self.collection) for s in self._parse_raw(raw)]

    def _parse_raw(self, raw):
        return raw.split(self.collection.sequence_delimiter)


class Sequence(object):
    def __init__(self, raw, collection):
        self.collection = collection
        self.points = self._create_points(raw)

    def _create_points(self, raw):
        return [Point(p, self.collection) for p in self._parse_raw(raw) if p]

    def _parse_raw(self, raw):
        return raw.splitlines()


class Point(object):
    def __init__(self, raw, collection):
        self.collection = collection
        self.data = self._parse_raw(raw)

        self.input = self.data['input']
        self.output = self.data['output']

    def _parse_raw(self, raw):
        return self.collection.point_parser(raw)
