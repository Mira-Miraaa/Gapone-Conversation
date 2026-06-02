import zipfile
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_text_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            xml_content = zip_ref.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # Namespace for docx
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            paragraphs = []
            for p in tree.findall('.//w:p', ns):
                texts = p.findall('.//w:t', ns)
                if texts:
                    paragraphs.append(''.join([t.text for t in texts]))
            
            return '\n'.join(paragraphs)
    except Exception as e:
        return str(e)

path = r'f:\Gapone Conversation\Docs\SRS Conversation.docx'
content = extract_text_from_docx(path)

output_path = r'f:\Gapone Conversation\scratch\extracted_doc.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Đã trích xuất và ghi vào {output_path} thành công!")

