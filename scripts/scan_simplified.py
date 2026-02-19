
import os
import re

# 常見簡繁差異極大的簡體字特徵表 (偵測用)
SIMPLIFIED_SAMPLES = "这说国发对进过给车风们时为体门学产经现实证变长样话书显继军义"

def scan_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        found = []
        for char in SIMPLIFIED_SAMPLES:
            if char in content:
                found.append(char)
        
        return found
    except Exception as e:
        print(f"無法讀取 {file_path}: {e}")
        return []

def main():
    target_dir = r"d:\專案\novel_Ratforge\章稿"
    results = []
    
    print(f"開始掃描簡體字於: {target_dir}...")
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                found_chars = scan_file(full_path)
                if found_chars:
                    relative_path = os.path.relpath(full_path, target_dir)
                    results.append((relative_path, found_chars))
    
    if not results:
        print("未偵測到明顯的簡體字內容。")
    else:
        print(f"\n--- 發現 {len(results)} 個檔案含有簡體字 ---")
        for path, chars in results:
            chars_str = "".join(chars[:10]) + ("..." if len(chars) > 10 else "")
            print(f"[{path}] 偵測到: {chars_str}")

if __name__ == "__main__":
    main()
