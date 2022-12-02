from janome.tokenizer import Tokenizer
t = Tokenizer()

text = "ありがとうございます。"

tokens = t.tokenize(text, wakati = True)
result = ' '.join(tokens)
print(result)