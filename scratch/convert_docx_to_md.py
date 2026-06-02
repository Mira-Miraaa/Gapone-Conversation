import zipfile
import xml.etree.ElementTree as ET
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Namespaces for OOXML
ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

def parse_paragraph(p_elem):
    # Check style
    style_val = ""
    pPr = p_elem.find('w:pPr', ns)
    is_list = False
    
    if pPr is not None:
        pStyle = pPr.find('w:pStyle', ns)
        if pStyle is not None:
            style_val = pStyle.get('{' + ns['w'] + '}val', '')
        
        numPr = pPr.find('w:numPr', ns)
        if numPr is not None:
            is_list = True

    # Process runs
    text_parts = []
    for r_elem in p_elem.findall('w:r', ns):
        # Check text
        t_elems = r_elem.findall('w:t', ns)
        if not t_elems:
            continue
        
        r_text = "".join([t.text for t in t_elems if t.text])
        if not r_text:
            continue
        
        # Check styling inside run
        rPr = r_elem.find('w:rPr', ns)
        is_bold = False
        is_italic = False
        if rPr is not None:
            if rPr.find('w:b', ns) is not None:
                is_bold = True
            if rPr.find('w:i', ns) is not None:
                is_italic = True
        
        if is_bold and is_italic:
            r_text = f"***{r_text}***"
        elif is_bold:
            r_text = f"**{r_text}**"
        elif is_italic:
            r_text = f"*{r_text}*"
            
        text_parts.append(r_text)
    
    para_text = "".join(text_parts).strip()
    if not para_text:
        return ""
    
    # Map heading styles
    if style_val:
        style_lower = style_val.lower()
        if 'heading' in style_lower:
            # Extract heading level
            level_str = ''.join(filter(str.isdigit, style_val))
            level = int(level_str) if level_str else 1
            # Limit levels to 1-6
            level = min(max(level, 1), 6)
            return f"\n{'#' * level} {para_text}\n"
    
    if is_list:
        return f"- {para_text}"
        
    return para_text

def parse_table(tbl_elem):
    rows_data = []
    max_cols = 0
    
    for tr_elem in tbl_elem.findall('w:tr', ns):
        row_cells = []
        for tc_elem in tc_elem_list(tr_elem):
            # A cell can contain multiple paragraphs
            cell_paras = []
            for p_elem in tc_elem.findall('w:p', ns):
                p_text = parse_paragraph(p_elem)
                if p_text:
                    cell_paras.append(p_text)
            cell_text = " ".join(cell_paras).replace("\n", " ").strip()
            row_cells.append(cell_text)
        if row_cells:
            rows_data.append(row_cells)
            max_cols = max(max_cols, len(row_cells))
            
    if not rows_data:
        return ""
        
    # Standardize column count
    markdown_lines = []
    for r_idx, row in enumerate(rows_data):
        # Pad row cells to max_cols
        if len(row) < max_cols:
            row.extend([""] * (max_cols - len(row)))
        # Join with pipes
        markdown_lines.append("| " + " | ".join(row) + " |")
        
        # Add separator after header row
        if r_idx == 0:
            separator = "| " + " | ".join(["---"] * max_cols) + " |"
            markdown_lines.append(separator)
            
    return "\n" + "\n".join(markdown_lines) + "\n"

def tc_elem_list(tr_elem):
    # Find all table cells under table row
    # Note: sdtContent might wrap table cells
    cells = []
    for child in tr_elem:
        if child.tag == '{' + ns['w'] + '}tc':
            cells.append(child)
        elif child.tag == '{' + ns['w'] + '}sdt':
            sdtContent = child.find('w:sdtContent', ns)
            if sdtContent is not None:
                for sub_child in sdtContent:
                    if sub_child.tag == '{' + ns['w'] + '}tc':
                        cells.append(sub_child)
    return cells

def docx_to_markdown(docx_path):
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            xml_content = zip_ref.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            body = tree.find('w:body', ns)
            if body is None:
                return "Không tìm thấy nội dung body trong XML."
                
            markdown_blocks = []
            
            # Iterate through direct children of body to maintain order
            for child in body:
                tag = child.tag
                if tag == '{' + ns['w'] + '}p':
                    p_text = parse_paragraph(child)
                    if p_text:
                        markdown_blocks.append(p_text)
                elif tag == '{' + ns['w'] + '}tbl':
                    tbl_text = parse_table(child)
                    if tbl_text:
                        markdown_blocks.append(tbl_text)
                elif tag == '{' + ns['w'] + '}sdt':
                    # Structured Document Tag block
                    sdtContent = child.find('w:sdtContent', ns)
                    if sdtContent is not None:
                        for sub_child in sdtContent:
                            if sub_child.tag == '{' + ns['w'] + '}p':
                                p_text = parse_paragraph(sub_child)
                                if p_text:
                                    markdown_blocks.append(p_text)
                            elif sub_child.tag == '{' + ns['w'] + '}tbl':
                                tbl_text = parse_table(sub_child)
                                if tbl_text:
                                    markdown_blocks.append(tbl_text)
                                    
            return "\n\n".join(markdown_blocks)
    except Exception as e:
        import traceback
        return f"Lỗi chuyển đổi: {str(e)}\n{traceback.format_exc()}"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Sử dụng: python convert_docx_to_md.py <file_docx> <file_md>")
        sys.exit(1)
        
    docx_path = sys.argv[1]
    md_path = sys.argv[2]
    
    print(f"Đang chuyển đổi {docx_path}...")
    markdown_content = docx_to_markdown(docx_path)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
        
    print(f"Chuyển đổi thành công! Đã lưu file Markdown tại: {md_path}")
