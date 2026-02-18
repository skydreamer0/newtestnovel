import os
import re

def count_words(text):
    # Simple count of non-whitespace characters
    return len(re.findall(r'\S', text))

def main():
    target_dir = r'd:\專案\novel_Ratforge\章稿\第9卷_墜落地'
    results = []
    
    print(f"Checking directory: {target_dir}")
    
    if not os.path.exists(target_dir):
        print("Directory not found!")
        return

    for filename in os.listdir(target_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(target_dir, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    count = count_words(content)
                    results.append((filename, count))
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    # Sort by filename naturally if possible, or just string sort
    results.sort(key=lambda x: x[0]) 
    
    print(f"{'Chapter':<40} | {'Word Count':<10}")
    print("-" * 55)
    for filename, count in results:
        marker = " <--- LOW" if count < 3000 else ""
        print(f"{filename:<40} | {count:<10}{marker}")

if __name__ == "__main__":
    main()
