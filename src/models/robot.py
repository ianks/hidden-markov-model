from .. import data


class Robot(data.Collection):
    def __init__(self, file):
        def sequence_parser(raw_sequence):
            return raw_sequence.splitlines()

        def point_parser(raw):
            if raw == '':
                return

            i, o = raw.split(' ')

            return {'input': i, 'output': o}

        sequence_delimiter = '.'
        data.Collection.__init__(self, file, sequence_delimiter,
                                 sequence_parser, point_parser)
