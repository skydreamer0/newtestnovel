
import os
import re

def count_words(text):
    # Remove markdown headers and other common artifacts if necessary
    # But for a simple novel count, we usually just count the characters in the body.
    # Let's count:
    # 1. Every Chinese character
    # 2. Every punctuation mark
    # 3. Every word for English (sequences of letters/numbers)
    
    # Simple approach: Count all non-whitespace characters
    # This is a common way to count "字數" in Chinese novel platforms.
    return len(re.findall(r'\S', text))

def main():
    base_dir = r'd:\專案\novel_Ratforge\章稿'
    threshold = 3000
    results = []

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    rel_path = os.path.relpath(file_path, base_dir)
                    # Filter for Volume 5 and onwards
                    # Assumes folder naming convention like "第5卷_..." or "第6卷_..."
                    match = re.search(r'第(\d+)卷', rel_path)
                    if match:
                        vol_num = int(match.group(1))
                        if vol_num < 5:
                            continue

                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        count = count_words(content)
                        if count < threshold:
                            results.append((rel_path, count))
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Sort results by count ascending
    results.sort(key=lambda x: x[1])

    print(f"總共有 {len(results)} 章少於 3000 字。")
    print("\n字數最少的 5 章：")
    print("-" * 30)
    for i, (path, count) in enumerate(results[:5], 1):
        print(f"{i}. {path} ({count} 字)")
    
    # Optionally print all of them if needed, but keeping it brief for now.
    # print("\n所有少於 3000 字的章節清單：")
    # for path, count in results:
    #     print(f"{count:4} : {path}")

if __name__ == "__main__":
    main()
