import os

def count_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Count non-whitespace characters
            count = len(''.join(content.split()))
            return count
    except Exception as e:
        return f"Error: {e}"

files = [
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第289章-以戰養戰.md",
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第290章-消化道陷阱.md",
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第291章-活死人大軍.md",
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第294章-反攻號角.md",
    r"d:\專案\novel_Ratforge\章稿\第9卷_墜落地\第295章-恐懼的收割.md"
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
