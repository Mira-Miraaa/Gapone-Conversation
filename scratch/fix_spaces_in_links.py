import os
import re
import sys
import urllib.parse

# Adjust stdout to handle UTF-8 printing
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"F:\Gapone Conversation"

def fix_links_in_content(content):
    # Pattern matches ](file:///...) handling up to one level of nested parentheses in the URL
    pattern = re.compile(r'\]\((file:///[^)]*(?:\([^)]*\)[^)]*)*)\)')
    
    def replace_match(match):
        url = match.group(1)
        prefix = ""
        path = url
        if "file:///" in url:
            parts = url.split("file:///", 1)
            prefix = parts[0] + "file:///"
            path = parts[1]
        
        # Decode first to avoid double encoding if some parts were already encoded
        decoded = urllib.parse.unquote(path)
        # Encode spaces and parentheses
        encoded = decoded.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
        return "](" + prefix + encoded + ")"
        
    return pattern.sub(replace_match, content)

def main():
    print("Mã hóa các khoảng trắng và dấu ngoặc đơn trong các liên kết file:///...")
    for root, dirs, files in os.walk(root_dir):
        # Skip dot directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    new_content = fix_links_in_content(content)
                    
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Đã mã hóa liên kết trong file: {os.path.relpath(file_path, root_dir)}")
                except Exception as e:
                    print(f"Lỗi khi xử lý file {file}: {e}")

if __name__ == "__main__":
    main()
