import os

def count_words(filepath):
    try:
        if not os.path.exists(filepath):
            return "File not found"
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Count non-whitespace characters as "words" for Chinese context
            # This is a standard way to count "fluid" characters in Chinese writing
            count = len(''.join(content.split()))
            return count
    except Exception as e:
        return f"Error: {e}"

files = [
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第285章-活體避雷針.md",
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第287章-鐵蹄壓境.md",
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第288章-臟器游擊.md",
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第292章-絕對數量.md",
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第293章-強殖屍爆.md"
]

print("Is File Path Valid?")
for file in files:
    try:
        exists = os.path.exists(file)
        print(f"{os.path.basename(file)}: {exists}")
    except:
        print(f"Error checking path: {file}")

print("\nWord Counts (Characters):")
for file in files:
    count = count_words(file)
    print(f"{os.path.basename(file)}: {count}")
