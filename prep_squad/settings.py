DIR_ROOT = './'

SQUAD_TAGS = ('train', 'dev')

SQUAD_VERSIONS = (1.1, 2.0)

TASKS = ('GEN_QA', 'GEN_QG', 'EXT_QA', 'CORPUS')

PARSERS = {
    'GEN_QA': 'GenerativeQAParser',
    'GEN_QG': 'GenerativeQGParser',
    'EXT_QA': 'ExtractiveQAParser',
    'CORPUS': 'CorpusParser'
}