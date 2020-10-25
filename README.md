# prepare-squad-dataset
How to preprocess the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/) for various NLP tasks.

## Classes and Methods
### SquadGuru

`SuqadGuru` is an NLP expert who can easily change the original SQuAD dataset into one of the required input formats of NLP tasks. Currently, GEN_QA, GEN_QG, and EXT_QA task's input format are available. Extract the end-to-end feature X and ground-truth Y from the SQuAD dataset by using the `SquadGuru` class.

- Constructor Signature

  ```python
  SquadGuru(parser: SquadParser, #parser which implement SquadParser
            tokenizer=None, #tokenizer which implement .tokenize(text: str)
            tags=SQUAD_TAGS, #iterable of str
            versions=SQUAD_VERSIONS #iterable of float
  )
  ```

  - Inject a `parser`, which the guru will use to extract X and Y data from the original squad dataset.
  - Inject a `tokenizer` that will create tokenized X and Y.
  - Inject an str iterable of `tags` that describes the tags of the dataset to load.
  - Inject a float iterable of `versions` that describes the versions of the dataset to load.

- `.gather(only_first_answer=False, verbose=False)`
  - `SquadGuru` gathers feature X and Y from the dataset.
  - Set `only_first_answer` to extract the first answer in each of question-answers sets.
  - Set `verbose` to print some logs.
- `.to_dataframe()`
  - Returns `pandas.DataFrame` object.
  - X is mapped into `'Input'` series.
  - Y is mapped into `'Target'` series.
- `.to_numpy()`
  - Returns numpy array shaped (N, 2) where N is the number of data.
  - Column of 0 is X, Column of 1 is Y.
- `.to_file(x_outfile, y_outfile)`
  - Writes text files saving X and Y.

### SquadParser

`SquadParser` implements methods to parse the original SQuAD dataset into the task-specific X, Y format.

- `.from_nlp_task(task: str)`
  - Currently Available `task` are "GEN_QA" or "GEN_QG" or "EXT_QA".
- `.parse(context: str, question: str:, answers: str iterable)`
  - Parse given quesition-answers pair in given context(paragraph) from the SQuAD dataset.

### Tokenizer

Any tokenizer that implements `.tokenizer(text: str)`. In examples, `transformers/BertTokenizer` object is used.


## Check Examples

[Extractive QA Dataset.ipynb](https://github.com/binchoo/prepare-squad-dataset/blob/master/Example\)Extractive%20QA%20Dataset.ipynb)

[Generative QA Dataset.ipynb](https://github.com/binchoo/prepare-squad-dataset/blob/master/Example\)Generative%20QA%20Dataset.ipynb)

[Generative QG Dataset.ipynb](https://github.com/binchoo/prepare-squad-dataset/blob/master/Example\)Generative%20QG%20Dataset.ipynb)

