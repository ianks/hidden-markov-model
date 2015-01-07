from .. import data
import re


class Topic(data.Collection):
    def __init__(self, file):
        def sequence_parser(raw_sequence):
            split_sequence = re.split('\s+', raw_sequence.rstrip())
            topic = split_sequence.pop(0)

            return [(topic, word) for word in split_sequence]

        def point_parser(raw):
            inp, out = raw

            return {'input': inp, 'output': out}

        sequence_delimiter = '\n'
        data.Collection.__init__(self, file, sequence_delimiter,
                                 sequence_parser, point_parser)
