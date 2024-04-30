import nltk

# # Download the necessary resources by uncommenting the below lines, comment after downloading
# # nltk.download('punkt')
# # nltk.download('averaged_perceptron_tagger')

# sentence = "The Students went to the class"

# # Tokenize the sentence
# tokens = nltk.word_tokenize(sentence)

# # Perform POS tagging
# pos_tags = nltk.pos_tag(tokens)

# print(pos_tags)


# from nltk.parse.generate import generate
# from nltk import CFG

# # Define the grammar
# grammar = CFG.fromstring("""
# S -> NP VP
# NP -> Det N | N
# VP -> V NP
# Det -> 'the' | 'a'
# N -> 'dog' | 'cat'
# V -> 'chased'
# """)

# # Generate sentences
# for sentence in generate(grammar,n=10):
#     print(' '.join(sentence))


from nltk.parse.generate import generate
from nltk import CFG

# Define the grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det Adj N | Det N PP
VP -> V NP | V NP PP
PP -> P NP
Det -> 'the' | 'a'
N -> 'house' | 'car' | 'book' | 'chair'
Adj -> 'big' | 'red' | 'old'
V -> 'is' | 'belongs' | 'owns' | 'purchased'
P -> 'in' | 'on' | 'under'
""")

# Generate sentences
for sentence in generate(grammar,n=10):
    print(' '.join(sentence))
