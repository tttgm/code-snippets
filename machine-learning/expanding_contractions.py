### Removing word contractions in NLP ###

"""
Before tokenizing words in a natural language processing workflow it is often useful
to expand out any contractions (e.g. can't => can not).

This can be easily performed using the 'contractions' python library.

"""

import contractions

def replace_contractions(text):
    """Replace contractions in a string of text"""

    return contractions.fix(text)

# e.g.
sample = replace_contractions(sample)
