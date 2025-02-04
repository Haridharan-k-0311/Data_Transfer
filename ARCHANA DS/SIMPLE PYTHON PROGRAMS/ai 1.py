import itertools
def word_to_number(word,letter_to_digit):
    return int(''.join(str(letter_to_digit[letter]) for letter in word))
def solve_cryptarithmetic(word,result):
    unique_letters=set(''.join(words)+result)
    if len (unique_letters)>10:
        print("too many unique letters,cannot solve.")
        return
   for digits in itertools.permutations(range(10),len(unique_letters)):
      letter_to_digit=dict(zip(unique_letters,digits))
      if any(letter_to_digit[word[0]]==0 for word in words+[result]):
        continue
      word_values=[word_to_number(word,letter_to_digit)for word in words]
      result_value=word_to_number(result,letter_to_digit)         
      if sum(word_values)==result_value: 
       print("solution found:")
       print(letter_to_digit)
       return letter_to_digit
print("no solution found")
words=["SEND","MORE"]
result="MONEY"
solve_cryptarithmetic(words,result)
