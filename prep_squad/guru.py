from .settings import SQUAD_TAGS, SQUAD_VERSIONS
from .utils import SquadLoader
from .parser import SquadParser
            
class SquadGuru:
    
    #using tokenizer is not yet supported
    def __init__(self, parser: SquadParser, 
                 tokenizer=None, tags=SQUAD_TAGS, versions=SQUAD_VERSIONS):
        self.parser = parser
        self.parser.set_tokenizer(tokenizer)
        
        self.tags = tags
        self.versions = versions

        self.X, self.Y = [], []
        
    def gather(self, only_first_answer=False, verbose=False):
        for tag in self.tags:
            for version in self.versions:
                squad = SquadLoader.load(tag, version)
                self._parse(squad, self.X, self.Y, only_first_answer)
                if verbose:
                    print("SQuAD-v%s %s dataset has been parsed." % (version, tag))
                    
    def _parse(self, squad, X, Y, only_first_answer):
        for d in squad['data']:
            for p in d['paragraphs']:
                con = p['context']
                con = con.replace('\n', '')
                for qa in p['qas']:
                    q = qa['question']
                    answers = qa['answers'][:1 if only_first_answer else 100]
                    for x, y in self.parser.parse(con, q, answers):
                        X.append(x)
                        Y.append(y)
    
    def to_dataframe(self):
        import pandas
        return pandas.DataFrame({'Input': self.X, 'Target':self.Y})
        
    def to_numpy(self):
        return self.to_dataframe().to_numpy()
    
    def to_file(self, outfile_X, outfile_Y):
        with open(outfile_X, 'w', encoding='utf-8') as ox:
            with open(outfile_Y, 'w', encoding='utf-8') as oy:
                ox.writelines("\n".join(self.X))
                oy.writelines("\n".join(list(map(str, self.Y))))