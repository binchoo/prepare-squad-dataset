from .settings import PARSERS
import sys

class SquadParser:
    '''It parses the given squad context, question and answers
        into one input-target pair, where tokenization can be applied.
    '''
    def __init__(self):
        self.tokenizer = None
        self.do_tokenize = False
    
    def set_tokenizer(self, tokenizer):
        self.tokenizer = tokenizer
        self.do_tokenize = tokenizer != None
    
    def try_tokenizer(self, x, y):
        if self.do_tokenize:
            return self.use_tokenizer(x), self.use_tokenizer(y)
        else:
            return x, y
        
    def use_tokenizer(self, text):
        return " ".join(self.tokenizer.tokenize(text))
    
    def parse(self, context, question, answers):
        raise NotImplementedError("Use derived class of SquadParser.")

    def sep(self, s1, s2):
        return "{} [SEP] {}".format(s1, s2)
    
    @staticmethod
    def from_nlp_task(task):
        thismodule = sys.modules[__name__]
        if task not in PARSERS.keys():
            raise Exception('Unsupported Task "%s"' % task)
        else:
            parser_cls = getattr(thismodule, PARSERS[task])
            parser = parser_cls()
        return parser
    
class GenerativeQAParser(SquadParser):
    
    def parse(self, context, question, answers):
        x = self.sep(context, question)
        for ans in answers:
            y = ans['text']
            yield self.try_tokenizer(x, y)

class GenerativeQGParser(SquadParser):
    
    def parse(self, context, question, answers):
        y = question
        for ans in answers:
            x = self.sep(context, ans['text'])
            yield self.try_tokenizer(x, y)
        
class ExtractiveQAParser(SquadParser):
    
    def parse(self, context, question, answers):
        x = self.sep(context, question)
        for ans in answers:
            y = ans['text']
            x,y = self.try_tokenizer(x, y)
            yield x, (x.find(y), len(y))

class CorpusParser(SquadParser):
    
    def __init__(self):
        self.prev_context = ''
        
    def parse(self, context, *args, **kwargs):
        if self.prev_context != context:
            yield context, None
            self.prev_context = context
            
'''
class AnotherParserClass(SquadParser):
    Do implement parse(self, context, question, answers)
'''