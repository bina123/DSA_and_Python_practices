from collections import Counter

def count_words_in_file(filename):
    words_count = []
    
    try:
        with open(filename,'r') as file:
            text = file.read().strip()
            
            for char in '.,!?;:"()[]':
                text.replace(char," ")
                
            words = text.split()
            
            word_count = Counter(words)
            
            return word_count
        
    except FileNotFoundError:
        print(f"{filename} not found")
        return []

def write_word_report(words,output_file,top_n):
    with open(output_file,'w') as file:
        file.write("Words frequncy count\n")
        file.write("="*50+ "\n\n")
        
        file.write(f"Total unique words: {len(words)}\n")
        file.write(f"Total words: {sum(words.values())}\n\n")
        
        file.write(f"Top {top_n} most common words:\n")
        file.write("-" * 50 + "\n")
        
        for word, count in words.most_common(top_n):
            file.write(f"{word:20} {count:5}\n")


word_count = count_words_in_file('python-practice/article.txt')
write_word_report(word_count, 'python-practice/word_report.txt', top_n=20)
print("Report generated!")