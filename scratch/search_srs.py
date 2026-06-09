with open(r"f:\Gapone Conversation\Docs\SRS Conversation.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

search_terms = ["zalo", "facebook", "messenger"]
out_lines = []
for i, line in enumerate(lines):
    for term in search_terms:
        if term in line.lower():
            start = max(0, i - 1)
            end = min(len(lines), i + 2)
            out_lines.append(f"--- Line {i+1} (term: {term}) ---")
            for j in range(start, end):
                out_lines.append(f"{j+1}: {lines[j].strip()}")
            out_lines.append("")
            break

with open(r"f:\Gapone Conversation\scratch\search_results_channels.txt", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(out_lines))
