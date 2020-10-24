# prepare-squad-dataset
How to preprocess the SQuAD dataset for various NLP tasks.

# Classes and Methods
## SquadGuru

`SuqadGuru` is an NLP expert who can easily change the original SQuAD dataset into one of the required format of NLP task models. Currently, GEN_QA, GEN_QG and EXT_QA task input format is available. Extract the end-to-end feature X and groud-truth Y from SQuAD dataset using `SquadGuru` class.

- Constructor Signature

  ```python
  SquadGuru(parser: SquadParser, #parser which implement SquadParser
            tokenizer=None, #tokenizer which implement .tokenize(text: str)
            tags=SQUAD_TAGS, #iterable of str
            versions=SQUAD_VERSIONS #iterable of float
  )
  ```

  - Inject a `parser`, which the guru will use to extract X and Y data from the original suqad dataset.
  - Inject a `tokenizer` that will be used to create tokenized X and Y.
  - Inject an iterable of `tags` that describes the tags of the dataset to load.
  - Inject an iterable of `versions` that describes the versions of the dataset to load. Version's datatype is `float`.

- `.gather(only_first_answer=False, verbose=False)`
  - `SquadGuru` gathers feature X and Y.
  - Set `only_first_answer` to extract the first answer in each of question-answers sets.
  - Set `verbose` to print some logs.
- `.to_dataframe()`
  - Get `pandas.DataFrame` object.
  - X is mapped into `'Input'` series.
  - Y is mapped into `'Target'` series.
- `.to_numpy()`
  - Get `numpy` array shaped (N, 2) where N is the number of data.
  - Column of 0 is X, Column of 1 is Y.

## SquadParser

Implements methods to parser the original SQuAD data into task-specific X, Y format.

- `.from_nlp_task(task: str)`
  - Currently Available `task` : "GEN_QA" or "GEN_QG" or "EXT_QA"

## Tokenizer

Any tokenizer that implements `.tokenizer(text: str)`. In examples, `transformers/BertTokenizer` object is used.


# Check Examples

[Extractive QA Dataset.ipynb](https://github.com/binchoo/prepare-squad-dataset/blob/master/Example\)Extractive%20QA%20Dataset.ipynb)

[Generative QA Dataset.ipynb](https://github.com/binchoo/prepare-squad-dataset/blob/master/Example\)Generative%20QA%20Dataset.ipynb)

[Generative QG Dataset.ipynb](https://github.com/binchoo/prepare-squad-dataset/blob/master/Example\)Generative%20QG%20Dataset.ipynb)

