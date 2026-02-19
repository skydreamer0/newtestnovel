
import os

def count_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Removing whitespace for character count
            # In Chinese contexts, 'word count' usually means character count excluding spaces
            return len("".join(content.split()))
    except Exception as e:
        return 0

def scan_directory(directory_path, volume_name):
    print(f"Scanning {volume_name}...")
    results = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md') and not file.startswith('._'):
                filepath = os.path.join(root, file)
                count = count_words(filepath)
                if count < 3000:
                    results.append((file, count))
    
    # Sort by filename to make it easier to read (assuming chapter numbers are in filename)
    # A simple sort might fail if numbers aren't padded (e.g. 1, 10, 2), but it's better than random.
    results.sort(key=lambda x: x[0]) 

    if not results:
        print("    No chapters found with less than 3000 words.")
    else:
        for filename, count in results:
            print(f"    - {filename}: {count} 字")
    print("-" * 30)

scan_directory(r"d:\專案\novel_Ratforge\章稿\S2-深淵篇\第9卷_墜落地", "第9卷")
scan_directory(r"d:\專案\novel_Ratforge\章稿\S2-深淵篇\第10卷_失落科技樹", "第10卷")
