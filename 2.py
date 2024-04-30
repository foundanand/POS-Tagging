from nltk.parse.generate import generate,demo_grammar
from nltk import CFG
import nltk

# Define the grammar
grammar = CFG.fromstring(demo_grammar)
print(grammar)

# Define the sentence to be parsed
sentence = "the man walked in the park"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Parse the sentence
parser = nltk.ChartParser(grammar)
trees = list(parser.parse(tokens))
# Print the parse tree
print(trees[0])
trees[0].pretty_print()