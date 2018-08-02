from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("mice"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("shepherds"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("pleased", pos="v"))
print(lemmatizer.lemmatize("beg", pos="n"))
