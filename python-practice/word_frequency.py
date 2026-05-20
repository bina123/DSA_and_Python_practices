from collections import Counter

def analyze_text(text):
    words = text.lower().split()
    
    words = [word.strip(':.,"!?()[]') for word in words]
    
    freq = Counter(words)
    
    return freq
    
def get_most_common(text,n):
    words = analyze_text(text)
    
    return words.most_common(n)

def get_unique_words(text):
    words = text.lower().split()
    
    words = [word.strip('.,:?!"()[]') for word in words]
    
    return set(words)

sample = """
Python is an amazing programming language.
Python is easy to learn and Python is powerful.
Many developers love Python for its simplicity.
"""

print("Most common words:", get_most_common(sample, 3))
print("Unique words:", len(get_unique_words(sample)))
print("Full frequency:", analyze_text(sample))