import pandas

nato_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")
# print(nato_alphabet)
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
# print(nato_dict)

valid_word = False
while not valid_word:
  word = input("Enter a word: ").upper()
  try:
    phonetic_code = [nato_dict[letter] for letter in word]
  except KeyError:
    print("Only letters are available")
  else:
    print(phonetic_code)
    valid_word = True
