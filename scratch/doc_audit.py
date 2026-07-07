import os
import re
import sys

# Adjust stdout to handle UTF-8 printing
sys.stdout.reconfigure(encoding='utf-8')

root_dir = sys.argv[1] if len(sys.argv) > 1 else r"F:\Gapone Conversation\Docs"

def audit_file(file_path):
    issues = []
    warnings = []
    passed = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    
    # 1. Check YAML Frontmatter
    has_frontmatter = False
    frontmatter_content = []
    if len(lines) > 0 and lines[0].strip() == '---':
        end_idx = -1
        for idx in range(1, len(lines)):
            if lines[idx].strip() == '---':
                end_idx = idx
                break
        if end_idx != -1:
            has_frontmatter = True
            frontmatter_content = lines[1:end_idx]
            
    if has_frontmatter:
        passed.append("YAML Frontmatter: Có tồn tại")
        # Check required fields
        required_fields = ['title', 'version', 'status', 'related_code', 'last_updated']
        fm_keys = {}
        for line in frontmatter_content:
            if ':' in line:
                key, val = line.split(':', 1)
                fm_keys[key.strip()] = val.strip()
                
        for field in required_fields:
            if field in fm_keys:
                passed.append(f"Frontmatter Field '{field}': '{fm_keys[field]}'")
            else:
                issues.append(f"Thiếu trường '{field}' trong YAML Frontmatter")
    else:
        issues.append("Không tìm thấy YAML Frontmatter ở đầu file")
        
    # 2. Check Revision History
    has_rev_history = "Nhật ký thay đổi" in content or "History" in content or "BẢNG GHI NHẬN THAY ĐỔI" in content or "BẢNG GHI NHẬN THAY ĐỔI TÀI LIỆU" in content
    if has_rev_history:
        passed.append("Nhật ký thay đổi: Có tồn tại")
        # Extract the Revision History section to avoid false positives in other tables (e.g. Competitive Matrix)
        rev_history_lines = []
        in_rev_history = False
        
        for idx, line in enumerate(lines, 1):
            line_str = line.strip().lower()
            if any(term in line_str for term in ["nhật ký thay đổi", "history", "ghi nhận thay đổi"]):
                in_rev_history = True
                continue
            if in_rev_history:
                # End of section when we meet a new main header or divider
                if (line.startswith('#') or line.startswith('---')) and not line.strip().startswith('|'):
                    in_rev_history = False
                else:
                    rev_history_lines.append((idx, line))
                    
        # Check for forbidden authors like "AI", "AI Assistant", "Gemini", "ChatGPT"
        forbidden_pattern = re.compile(r'\|\s*(AI|AI Assistant|Gemini|ChatGPT|Assistant|Antigravity)\s*\|', re.IGNORECASE)
        for line_num, line in rev_history_lines:
            if '|' in line:
                match = forbidden_pattern.search(line)
                if match:
                    issues.append(f"Dòng {line_num} (Phần Nhật ký thay đổi): Người cập nhật được ghi là '{match.group(1)}' (Cấm ghi là AI/AI Assistant theo quy tắc AGENTS.md)")
    else:
        warnings.append("Không tìm thấy bảng Nhật ký thay đổi (Revision History)")
        
    # 3. Check Mermaid diagrams
    has_mermaid = "```mermaid" in content
    if has_mermaid:
        passed.append("Sơ đồ Mermaid: Có sử dụng")
    else:
        warnings.append("Tài liệu không sử dụng sơ đồ Mermaid")
        
    # 4. Check LaTeX
    has_latex = "$$" in content or "\\(" in content or "\\[" in content
    if has_latex:
        passed.append("Công thức LaTeX: Có sử dụng")
    else:
        passed.append("Không phát hiện công thức LaTeX")
        
    # 5. Check Alert Blocks
    has_alert = "> [!" in content
    if has_alert:
        passed.append("Alert Block: Có sử dụng")
    else:
        warnings.append("Tài liệu không sử dụng Alert Blocks (> [!NOTE], etc.)")
        
    return {
        "file": os.path.basename(file_path),
        "issues": issues,
        "warnings": warnings,
        "passed": passed
    }

def main():
    print("# BÁO CÁO ĐỒNG BỘ & KIỂM ĐỊNH TÀI LIỆU (DOC AUDIT)\n")
    print(f"Thư mục kiểm định: `{root_dir}`\n")
    
    if not os.path.exists(root_dir):
        print(f"Lỗi: Thư mục không tồn tại: {root_dir}")
        return
        
    files = [f for f in os.listdir(root_dir) if f.lower().endswith('.md')]
    
    total_issues = 0
    total_warnings = 0
    
    for file in files:
        file_path = os.path.join(root_dir, file)
        result = audit_file(file_path)
        
        print(f"## 📄 File: `{result['file']}`")
        
        if result['issues']:
            print("### 🔴 Lỗi nghiêm trọng (Issues):")
            for issue in result['issues']:
                print(f"- {issue}")
                total_issues += 1
        else:
            print("### 🟢 Kiểm định cấu trúc: ĐẠT")
            
        if result['warnings']:
            print("### 🟡 Khuyến nghị (Warnings):")
            for warning in result['warnings']:
                print(f"- {warning}")
                total_warnings += 1
                
        print("\n---\n")
        
    print("## 📊 TỔNG KẾT KIỂM ĐỊNH")
    print(f"- Tổng số file kiểm tra: **{len(files)}**")
    print(f"- Tổng số lỗi cấu trúc (Issues): **{total_issues}**")
    print(f"- Tổng số khuyến nghị (Warnings): **{total_warnings}**")
    
    if total_issues == 0:
        print("\n🎉 **Tất cả các tài liệu đều tuân thủ tốt tiêu chuẩn cấu trúc dự án!**")
    else:
        print("\n⚠️ **Cần khắc phục các lỗi nghiêm trọng để đảm bảo tính chuẩn hóa của tài liệu.**")

if __name__ == "__main__":
    main()
