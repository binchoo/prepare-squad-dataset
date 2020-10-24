from settings import SQUAD_TAGS, SQUAD_VERSIONS, TASKS
from utils import SQuADPath
from utils import SQuADLoader

class PrepareSQuAD:
    
    #using tokenizer is not yet supported
    def __init__(self, task, tokenizer=None, tags=SQUAD_TAGS, versions=SQUAD_VERSIONS):
        self.task = task
        self.tags = tags
        self.versions = versions
        self.X, self.Y = [], []
        
        if task not in TASKS:
            raise Exception('Unsupported Task "%s"' % self.task)
        
    def prepare(self, use_only_first_answer=False, verbose=False):
        for tag in self.tags:
            for version in self.versions:
                if 'GEN_QA' == self.task:
                    self._parse_GEN_QA(SQuADLoader.load(tag, version), self.X, self.Y, use_only_first_answer)
                elif 'EXT_QA' == self.task:
                    self._parse_EXT_QA(SQuADLoader.load(tag, version), self.X, self.Y, use_only_first_answer)
                elif 'GEN_QG' == self.task:
                    self._parse_GEN_QG(SQuADLoader.load(tag, version), self.X, self.Y, use_only_first_answer)
                else:
                    raise Exception('Unsupported Task "%s"' % self.task)
                
                if verbose:
                    print("SQuAD-v%s %s dataset has been parsed." % (version, tag))
    
    def _parse_GEN_QA(self, squad, X, Y, use_only_first_answer):
        for d in squad['data']:
            for p in d['paragraphs']:
                con = p['context']
                con = con.replace('\n', '')
                for qa in p['qas']:
                    q = qa['question']
                    x = self.sep(con, q)
                    for ans in qa['answers'][:1 if use_only_first_answer else 100]:
                        y = ans['text']
                        X.append(x.strip('\n'))
                        Y.append(y.strip('\n'))
                        
    def _parse_EXT_QA(self, squad, X, Y, use_only_first_answer):
        for d in squad['data']:
            for p in d['paragraphs']:
                con = p['context']
                con = con.replace('\n', '')
                for qa in p['qas']:
                    q = qa['question']
                    x = self.sep(con, q)
                    for ans in qa['answers'][:1 if use_only_first_answer else 100]:
                        ans_text = ans['text'].strip('\n')
                        y = (con.find(ans_text), len(ans_text))
                        X.append(x.strip('\n'))
                        Y.append(y)
                        
    def _parse_GEN_QG(self, squad, X, Y, use_only_first_answer):
        for d in squad['data']:
            for p in d['paragraphs']:
                con = p['context']
                con = con.replace('\n', '')
                for qa in p['qas']:
                    y = qa['question']
                    for ans in qa['answers'][:1 if use_only_first_answer else 100]:
                        x = self.sep(con, ans['text'])
                        X.append(x.strip('\n'))
                        Y.append(y.strip('\n'))
    
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
    
    def sep(self, s1, s2):
        return "{} [SEP] {}".format(s1, s2)