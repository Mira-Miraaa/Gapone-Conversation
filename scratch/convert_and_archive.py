import os
import shutil
import sys
from markitdown import MarkItDown

# Adjust stdout to handle UTF-8 printing
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"F:\Gapone Conversation"
archive_dir = os.path.join(root_dir, ".archive_docx")

def main():
    # Initialize MarkItDown
    md = MarkItDown()
    
    docx_files = []
    # Find all .docx files, excluding hidden directories
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories like .git, .vscode, .archive_docx
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.lower().endswith('.docx'):
                docx_files.append(os.path.join(root, file))
                
    print(f"Tìm thấy {len(docx_files)} file .docx.")
    
    converted_count = 0
    skipped_count = 0
    
    for docx_path in docx_files:
        rel_path = os.path.relpath(docx_path, root_dir)
        dir_name = os.path.dirname(docx_path)
        base_name = os.path.splitext(os.path.basename(docx_path))[0]
        md_path = os.path.join(dir_name, f"{base_name}.md")
        
        # Check if .md file already exists
        if os.path.exists(md_path):
            print(f"Bỏ qua (đã chuyển đổi trước đó): {rel_path}")
            skipped_count += 1
        else:
            print(f"Đang chuyển đổi: {rel_path} -> {base_name}.md")
            try:
                result = md.convert(docx_path)
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(result.text_content)
                print(f"Chuyển đổi thành công: {rel_path}")
                converted_count += 1
            except Exception as e:
                print(f"Lỗi khi chuyển đổi {rel_path}: {e}")
                
    print(f"Kết quả chuyển đổi: Đã chuyển đổi {converted_count} file, bỏ qua {skipped_count} file.")
    
    # Move docx files to .archive_docx
    print("Bắt đầu di chuyển các file .docx vào thư mục lưu trữ ẩn...")
    moved_count = 0
    for docx_path in docx_files:
        rel_path = os.path.relpath(docx_path, root_dir)
        dest_path = os.path.join(archive_dir, rel_path)
        dest_parent = os.path.dirname(dest_path)
        os.makedirs(dest_parent, exist_ok=True)
        
        try:
            # If target exists (e.g. from previous runs), remove it first
            if os.path.exists(dest_path):
                os.remove(dest_path)
            shutil.move(docx_path, dest_path)
            print(f"Đã lưu trữ: {rel_path} -> .archive_docx\\{rel_path}")
            moved_count += 1
        except Exception as e:
            print(f"Lỗi khi di chuyển {rel_path} vào lưu trữ: {e}")
            
    print(f"Kết quả lưu trữ: Đã lưu trữ {moved_count}/{len(docx_files)} file .docx vào {archive_dir}.")

if __name__ == "__main__":
    main()
