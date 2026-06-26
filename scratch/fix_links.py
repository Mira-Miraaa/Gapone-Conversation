import os
import re
import sys

# Adjust stdout to handle UTF-8 printing
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"F:\Gapone Conversation"

replacements = [
    # Fix paths for files that were moved to Docs/AI_Chatbot
    ("Docs/srs-ai-settings.md", "Docs/AI_Chatbot/srs-ai-settings.md"),
    ("Docs/srs-chatbot-scenarios.md", "Docs/AI_Chatbot/srs-chatbot-scenarios.md"),
    ("Docs/srs-conversation-memory.md", "Docs/AI_Chatbot/srs-conversation-memory.md"),
    ("Docs/srs-conversation-summary.md", "Docs/AI_Chatbot/srs-conversation-summary.md"),
    ("Docs/srs-knowledge-base.md", "Docs/AI_Chatbot/srs-knowledge-base.md"),
    ("Docs/prd-ai-chatbot.md", "Docs/AI_Chatbot/prd-ai-chatbot.md"),
    ("Docs/prd-ai-chatbot-intro.md", "Docs/AI_Chatbot/prd-ai-chatbot-intro.md"),
    ("Docs/prd-reminder-agent.md", "Docs/AI_Chatbot/prd-reminder-agent.md"),
    ("Docs/prd-image-upload-feasibility.md", "Docs/AI_Chatbot/prd-image-upload-feasibility.md"),
    ("Docs/prd-file-processing.md", "Docs/AI_Chatbot/prd-file-processing.md"),
    ("Docs/prd-tool-calling-architecture.md", "Docs/AI_Chatbot/prd-tool-calling-architecture.md"),

    # Docx to Md replacements
    ("Docs/%5BGAPCON%5D%20AI%20Chatbot%20for%20e-commerce%20(PRD).docx", "Docs/AI_Chatbot/prd-ai-chatbot.md"),
    ("Docs/%5BGAPCON%5D%20AI%20Chatbot%20for%20e-commerce%20%28PRD%29.docx", "Docs/AI_Chatbot/prd-ai-chatbot.md"),
    ("Docs/SRS%20AI%20chatbot%20-%20Conversation%20Summary.md", "Docs/AI_Chatbot/srs-conversation-summary.md"),
    ("Docs/SRS%20AI%20chatbot%20-%20Conversation%20Summary.docx", "Docs/AI_Chatbot/srs-conversation-summary.md"),
    ("Docs/SRS%20AI%20chatbot%20-%20Conversation%20Memory.md", "Docs/AI_Chatbot/srs-conversation-memory.md"),
]

def main():
    print("Sửa các liên kết hỏng hoặc lỗi đường dẫn sau khi đổi tên...")
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
                    
                    for src, dst in replacements:
                        # Regex replacement ignoring case
                        pattern = re.compile(re.escape(src), re.IGNORECASE)
                        if pattern.search(new_content):
                            new_content = pattern.sub(dst, new_content)
                            modified = True
                            
                    if modified:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Đã sửa liên kết trong file: {os.path.relpath(file_path, root_dir)}")
                except Exception as e:
                    print(f"Lỗi khi xử lý file {file}: {e}")

if __name__ == "__main__":
    main()
