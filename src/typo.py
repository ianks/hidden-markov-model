import data

class Typo(data.Collection):
    def __init__(self, file):
        def point_parser(raw):
            x, y = raw.split(' ')

            return { 'input': x, 'output': y }

        sequence_delimiter = '_ _'
        data.Collection.__init__(self, file, sequence_delimiter, point_parser)
