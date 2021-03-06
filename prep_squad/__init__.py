# Gurus
from .guru import SquadGuru

# Parsers
from .parser import (
    SquadParser, 
    ExtractiveQAParser, 
    GenerativeQAParser, 
    GenerativeQGParser,
    CorpusParser,
)

# Library Checks
from .settings import TASKS, PARSERS
assert( set(TASKS) == PARSERS.keys() )
