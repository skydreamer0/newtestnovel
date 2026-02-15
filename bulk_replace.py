import os
import re

target_dir = "/Users/george/Library/CloudStorage/OneDrive-MSFT/專案/newtestnovel/章稿/第一卷_源代碼重啟"
files = [f for f in os.listdir(target_dir) if f.startswith("第0") and f.endswith(".md")]
files.sort()

# Filter for Ch 10-30
files = [f for f in files if 10 <= int(f.split("第")[1].split("章")[0]) <= 30]

def process_content(content):
    # Protect external screens
    content = content.replace("中控屏幕", "__CONTROL_SCREEN__")
    content = content.replace("監視屏", "__SURV_SCREEN__")
    content = content.replace("防線終端", "__DEF_CONSOLE__") # Protected from C24 manual fix
    content = content.replace("偽裝終端", "__FAKE_TERM__")   # Protected from C27 manual fix
    content = content.replace("舊終端殼", "__OLD_TERM_SHELL__") # Protected from C27
    
    # Generic replacements
    content = re.sub(r"把終端扣回[^\n]*", "拉緊袖口遮住手腕", content)
    content = content.replace("腕式終端", "意識介面")
    
    # Context aware replacements
    # Terminal acting as agent -> Furnace
    content = re.sub(r"終端(彈出|跳出|顯示|給出|更新|同步|檢測|判定|警示|警告|提示)", r"鍊成爐\1", content)
    
    # Looking at terminal -> Looking at interface
    content = re.sub(r"(看|盯|望)著?終端", r"\1著介面", content)
    
    # Remaining Terminals -> Interface (System)
    content = content.replace("終端", "介面")
    
    # Screens -> Interface/Vision
    content = content.replace("屏幕", "介面")
    content = content.replace("光幕", "介面")
    
    # Restore protected
    content = content.replace("__CONTROL_SCREEN__", "中控屏幕")
    content = content.replace("__SURV_SCREEN__", "監視屏")
    content = content.replace("__DEF_CONSOLE__", "防線終端")
    content = content.replace("__FAKE_TERM__", "偽裝終端")
    content = content.replace("__OLD_TERM_SHELL__", "舊終端殼")
    
    return content

for filename in files:
    path = os.path.join(target_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = process_content(content)
    
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename}")
