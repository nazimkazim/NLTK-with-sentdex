from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "The Astrophysics Data System is an online NASA database of over 7,000,000 astronomy and physics papers from both peer reviewed and non-peer reviewed sources. Abstracts are available free online for almost all articles, and full scanned articles are available in GIF and PDF format for older articles. New articles have links to electronic versions hosted at the journal's webpage, but these are typically available only by subscription (which most astronomy research facilities have)."
#print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)
