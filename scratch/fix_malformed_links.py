import os
import sys

# Adjust stdout to handle UTF-8 printing
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"F:\Gapone Conversation"

# Malformed pattern -> Fixed pattern
corrections = {
    "PRD%20AI%20Chatbot%20for%20e-commerce%20%281).md)": "PRD%20AI%20Chatbot%20for%20e-commerce%20%281%29.md)",
    "PRD%20AI%20Chatbot%20for%20e-commerce%20%282).md)": "PRD%20AI%20Chatbot%20for%20e-commerce%20%282%29.md)",
    "PRD%20AI%20Chatbot%20for%20e-commerce%20%283).md)": "PRD%20AI%20Chatbot%20for%20e-commerce%20%283%29.md)",
    "PRD%20AI%20Chatbot%20for%20e-commerce%20%284).md)": "PRD%20AI%20Chatbot%20for%20e-commerce%20%284%29.md)"
}

def main():
    print("Sửa lỗi định dạng dấu ngoặc đơn trong các liên kết URL...")
    for root, dirs, files in os.walk(root_dir):
        # Skip dot directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    new_content = content
                    modified = False
                    
                    for wrong, right in corrections.items():
                        if wrong in new_content:
                            new_content = new_content.replace(wrong, right)
                            modified = True
                            
                    if modified:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Đã sửa liên kết lỗi trong file: {os.path.relpath(file_path, root_dir)}")
                except Exception as e:
                    print(f"Lỗi khi xử lý file {file}: {e}")

if __name__ == "__main__":
    main()
