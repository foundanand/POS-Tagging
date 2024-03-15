import nltk

# Download the necessary resources by uncommenting the below lines, comment after downloading
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

sentence = "The Students went to the class"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Perform POS tagging
pos_tags = nltk.pos_tag(tokens)

print(pos_tags)
