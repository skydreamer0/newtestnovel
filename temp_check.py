
import os
import re

def count_words(text):
    return len(re.findall(r'\S', text))

base_dir = r'd:\專案\novel_Ratforge\章稿'
results = []

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                count = count_words(f.read())
                results.append((file, count))

results.sort(key=lambda x: x[1])

print("TOP 5 SMALLEST:")
for i, (name, count) in enumerate(results[:5], 1):
    print(f"{i}. {name}: {count} words")

short_count = len([r for r in results if r[1] < 3000])
print(f"Total < 3000: {short_count}")
