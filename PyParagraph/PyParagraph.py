import re
test ="Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold."
res = len(re.findall(r'\w+', test)) 
print(res)
count = 0
count1 = []
for i in test:
    if  i == ".":
        count = count + 1
print(count)
letterCount = test.split()
sum = 0
for i in letterCount:
    sum = sum + len(i)
letterCount_word = sum / len(letterCount)
print(round((letterCount_word),2))
averageSentence  = res/ count
print(round(averageSentence))
print("Paragraph Analysis")
print("..............................")
print("Approximate Word Count: " + str(res))
print("Approximate Sentence Count: "+ str(count))
print("Average Letter Count: "+ str(round((letterCount_word), 2)))
print("Average Sentence length: "+ str(averageSentence))