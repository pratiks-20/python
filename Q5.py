from collections import Counter

text = """Python is a powerful programming language. 
Python is easy to learn and widely used in data science. 
This tool will analyze Python text easily."""

text_lower = text.lower()

words = text_lower.split()

total_words = len(words)
print("Total words:", total_words)

word_freq = Counter(words)
print("\nWord Frequencies:")
for word, freq in word_freq.items():
    print(word, ":", freq)

top_3 = word_freq.most_common(3)
print("\nTop 3 most frequent words:")
for word, freq in top_3:
    print(word, ":", freq)

vowels = "aeiou"
vowel_count = sum(1 for char in text_lower if char in vowels)
print("\nTotal vowels in text:", vowel_count)