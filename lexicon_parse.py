class ParseError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, object):
        self.subject = subject[0]
        self.verb = verb[0]
        self.object = object[0]

    def peek(self, word_list):
        self.word_list = word_list
        if self.word_list:
            word = self.word_list[0]
            return word[0]

        else:
            return None

    def match(self, word_list, expecting):
        self.word_list = word_list
        self.expecting = expecting
        if self.word_list:
            word = self.word_list.pop(0)

            if word[0] == self.expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(self, word_list, word_type):
        self.word_list = word_list
        self.word_type = word_type
        while self.peek(self.word_list) == self.word_type:
            self.match(self.word_list, self.word_type)

    def parse_verb(self, word_list):
        skip(self.word_list, 'stop')

        if self.peek(self.word_list) == 'verb':
            return self.match(self.word_list, 'verb')
        else:
            raise ParseError("expected a verb next.")

    def parse_object(self, word_list):
        skip(self.word_list, 'stop')
        next = peek(self.word_list)

        if next == 'noun':
            return match(self.word_list, 'noun')
        if next == 'direction':
            return match(self.word_list, 'direction')
        else:
            raise ParseError("expected a noun or direction next.")

    def parse_subject(self, word_list, subj):
        verb = parse_verb(self.word_list)
        obj = parse_object(self.word_list)

        return Sentence(subj, verb, obj)

    def parse_sentence(self, word_list):
        skip(self.word_list, 'stop')

        start = peek(self.word_list)

        if start == 'noun':
            subj = match(self.word_list, 'noun')
            return parse_subject(self.word_list, subj)
        elif start == 'verb':
            return parse_subject(self.word_list, ('noun', 'player'))
        else:
            raise ParseError("must start with subject, object or verb not: %s" % start)