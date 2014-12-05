import data

class Robot(data.Collection):
    def __init__(self, file):
        def point_parser(raw):
            if raw == '': return

            i, o = raw.split(' ')
            x, y = i.split(':')
            point = (x, y)

            return { 'input': point, 'output': o }

        sequence_delimiter = '.'
        data.Collection.__init__(self, file, sequence_delimiter, point_parser)
