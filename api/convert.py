"""
temporary solution to update files. To be fixed with a new approach to data storage
"""


import pickle

from brain import Brain

b = Brain()

text = open ("pkl_text.txt", "r").read().split("\n\n")
context_embeddings = b.compute_text_embeddings(text)

with open('files/context_embeddings_file.obj', 'wb') as fp:
 	pickle.dump(context_embeddings, fp)

with open('files/textfile.obj', 'wb') as fp:
 	pickle.dump(text, fp)