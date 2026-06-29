import os
import sys

# Adjust stdout to handle UTF-8 printing
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"F:\Gapone Conversation\Docs\AI_Chatbot"

prd_configs = {
    "prd-ai-chatbot.md": {
        "title": "PRD AI Chatbot for e-commerce - Core Specifications",
        "version": "1.0.0"
    },
    "prd-ai-chatbot-intro.md": {
        "title": "PRD AI Chatbot for e-commerce - Introduction",
        "version": "1.0.0"
    },
    "prd-reminder-agent.md": {
        "title": "PRD AI Chatbot for e-commerce - Reminder Agent",
        "version": "1.0.0"
    },
    "prd-image-upload-feasibility.md": {
        "title": "PRD AI Chatbot for e-commerce - Image Upload & Feasibility Verification",
        "version": "1.0.0"
    },
    "prd-file-processing.md": {
        "title": "PRD AI Chatbot for e-commerce - File Processing Specification",
        "version": "1.0.0"
    },
    "prd-tool-calling-architecture.md": {
        "title": "PRD AI Chatbot for e-commerce - Tool Calling Architecture",
        "version": "1.0.0"
    }
}

srs_configs = {
    "srs-ai-settings.md": {
        "title": "SRS AI Settings",
        "version": "1.0.5"
    },
    "srs-chatbot-scenarios.md": {
        "title": "SRS Chatbot Scenarios",
        "version": "1.1.1"
    },
    "srs-conversation-memory.md": {
        "title": "SRS Conversation Memory",
        "version": "1.0.0"
    },
    "srs-conversation-summary.md": {
        "title": "SRS Conversation Summary",
        "version": "1.0.0"
    },
    "srs-knowledge-base.md": {
        "title": "SRS Knowledge Base",
        "version": "1.0.0"
    }
}

def standardize_prd(filename, config):
    file_path = os.path.join(root_dir, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if frontmatter already exists
    if content.startswith('---'):
        print(f"Bỏ qua PRD (đã có frontmatter): {filename}")
        return
        
    frontmatter = f"""---
title: {config['title']}
version: {config['version']}
status: verified-by-ba
related_code: F:/Gapone Conversation/Docs/AI_Chatbot/{filename}
last_updated: 2026-06-26
---

# Nhật ký thay đổi (Revision History)

| Phiên bản | Ngày | Người cập nhật | Vị trí thay đổi | Lý do chi tiết |
| :--- | :--- | :--- | :--- | :--- |
| 1.0.0 | 2026-06-26 | Mira-Miraaa | Toàn bộ tài liệu | Chuẩn hóa tài liệu từ tệp cũ |

---

"""
    new_content = frontmatter + content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Đã chuẩn hóa PRD: {filename}")

def standardize_srs(filename, config):
    file_path = os.path.join(root_dir, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if frontmatter already exists
    if content.startswith('---'):
        print(f"Bỏ qua SRS (đã có frontmatter): {filename}")
        return
        
    frontmatter = f"""---
title: {config['title']}
version: {config['version']}
status: verified-by-ba
related_code: F:/Gapone Conversation/Docs/AI_Chatbot/{filename}
last_updated: 2026-06-26
---

"""
    new_content = frontmatter + content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Đã chuẩn hóa SRS: {filename}")

def main():
    print("Bắt đầu chuẩn hóa cấu trúc 11 file tài liệu...")
    
    # Process PRDs
    for filename, config in prd_configs.items():
        if os.path.exists(os.path.join(root_dir, filename)):
            standardize_prd(filename, config)
            
    # Process SRSs
    for filename, config in srs_configs.items():
        if os.path.exists(os.path.join(root_dir, filename)):
            standardize_srs(filename, config)
            
    print("Hoàn tất chuẩn hóa.")

if __name__ == "__main__":
    main()
