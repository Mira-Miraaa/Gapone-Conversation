import os
import shutil
import sys
import urllib.parse

# Adjust stdout to handle UTF-8 printing
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"F:\Gapone Conversation"
target_dir = os.path.join(root_dir, r"Docs\AI_Chatbot")

mapping = {
    "SRS AI chatbot - AI.md": "srs-ai-settings.md",
    "SRS AI chatbot - Automation.md": "srs-chatbot-scenarios.md",
    "SRS AI chatbot - Conversation Memory.md": "srs-conversation-memory.md",
    "SRS AI chatbot - Conversation Summary.md": "srs-conversation-summary.md",
    "SRS AI chatbot - Knowledge base.md": "srs-knowledge-base.md",
    "[GAPCON] AI Chatbot for e-commerce (PRD).md": "prd-ai-chatbot.md",
    "[GAPCON] AI Chatbot for e-commerce (PRD) (1).md": "prd-ai-chatbot-intro.md",
    "[GAPCON] AI Chatbot for e-commerce (PRD) (2).md": "prd-reminder-agent.md",
    "[GAPCON] AI Chatbot for e-commerce (PRD) (3).md": "prd-image-upload-feasibility.md",
    "[GAPCON] AI Chatbot for e-commerce (PRD) (4).md": "prd-file-processing.md",
    "[GAPCON] AI Chatbot for e-commerce (PRD) 9.md": "prd-tool-calling-architecture.md"
}

def get_replacements(old, new):
    replaces = []
    # 1. Raw
    replaces.append((old, new))
    
    # 2. URL-encoded standard (e.g. quote spaces and special characters)
    # By default, urllib.parse.quote encodes brackets but might skip parentheses depending on settings,
    # so we explicitly generate both standard quote and custom replacements.
    quoted_old = urllib.parse.quote(old)
    quoted_new = urllib.parse.quote(new)
    
    replaces.append((quoted_old, quoted_new))
    
    # 3. Custom quote for URL matching in markdown links
    # Sometimes brackets like [ and ] are encoded, and spaces as %20
    quoted_old_c1 = old.replace(" ", "%20").replace("[", "%5B").replace("]", "%5D").replace("(", "%28").replace(")", "%29")
    quoted_new_c1 = new.replace(" ", "%20").replace("[", "%5B").replace("]", "%5D").replace("(", "%28").replace(")", "%29")
    if (quoted_old_c1, quoted_new_c1) not in replaces:
        replaces.append((quoted_old_c1, quoted_new_c1))
        
    quoted_old_c2 = old.replace(" ", "%20").replace("[", "%5B").replace("]", "%5D")
    quoted_new_c2 = new.replace(" ", "%20").replace("[", "%5B").replace("]", "%5D")
    if (quoted_old_c2, quoted_new_c2) not in replaces:
        replaces.append((quoted_old_c2, quoted_new_c2))
        
    return replaces

def main():
    all_replaces = []
    for old, new in mapping.items():
        all_replaces.extend(get_replacements(old, new))
        
    print("Các chuỗi liên kết sẽ được thay thế trong nội dung:")
    for src, dst in all_replaces:
        if src != dst:
            print(f"  '{src}' -> '{dst}'")
            
    # 1. Update contents of all markdown files
    print("\nCập nhật nội dung trong các file .md...")
    for root, dirs, files in os.walk(root_dir):
        # Skip dot directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    modified = False
                    new_content = content
                    for src, dst in all_replaces:
                        if src in new_content:
                            new_content = new_content.replace(src, dst)
                            modified = True
                            
                    if modified:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Đã cập nhật liên kết trong file: {os.path.relpath(file_path, root_dir)}")
                except Exception as e:
                    print(f"Lỗi khi xử lý nội dung file {file}: {e}")
                    
    # 2. Rename the files physically
    print("\nTiến hành đổi tên file vật lý...")
    for old, new in mapping.items():
        old_path = os.path.join(target_dir, old)
        new_path = os.path.join(target_dir, new)
        if os.path.exists(old_path):
            try:
                shutil.move(old_path, new_path)
                print(f"Đã đổi tên: {old} -> {new}")
            except Exception as e:
                print(f"Lỗi khi đổi tên {old}: {e}")
        else:
            print(f"File không tồn tại hoặc đã được đổi tên: {old}")

if __name__ == "__main__":
    main()
