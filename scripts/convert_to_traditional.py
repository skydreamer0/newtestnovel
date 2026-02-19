
import os
import zhconv

def convert_to_traditional(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 轉換為繁體 (zh-hant)
        converted = zhconv.convert(content, 'zh-hant')
        
        if converted != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(converted)
            return True
        return False
    except Exception as e:
        print(f"處理失敗 {file_path}: {e}")
        return False

def main():
    target_dir = r"d:\專案\novel_Ratforge\章稿"
    count = 0
    total = 0
    
    print(f"開始執行全自動繁體化轉換: {target_dir}...")
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".md"):
                total += 1
                full_path = os.path.join(root, file)
                if convert_to_traditional(full_path):
                    count += 1
                    print(f"[已修復] {os.path.relpath(full_path, target_dir)}")
    
    print(f"\n--- 任務完成 ---")
    print(f"掃描檔案總數: {total}")
    print(f"已修正含有簡體字的檔案: {count}")

if __name__ == "__main__":
    main()
