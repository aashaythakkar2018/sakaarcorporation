import re
import glob

# Read index.html to extract the desired header
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the header block from index.html
# It starts after <body class="bg-white"> and ends before <!-- Hero Section -->
match = re.search(r'<body[^>]*>\s*(.*?)\s*(?:<!-- Hero Section -->\s*)?<section', index_content, re.DOTALL | re.IGNORECASE)
if not match:
    print("Could not find header in index.html")
    exit(1)

new_header = match.group(1)
print(f"Extracted header length: {len(new_header)}")

html_files = glob.glob('*.html')
for file in html_files:
    if file == 'index.html':
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace everything between <body> and the first <section
    def replacer(m):
        body_tag = m.group(1)
        hero_comment = m.group(3) or ''
        section_tag = m.group(4)
        return f"{body_tag}\n{new_header}\n{hero_comment}{section_tag}"
    
    new_content, count = re.subn(r'(<body[^>]*>)\s*(.*?)\s*(<!-- Hero Section -->\s*)?(<section)', replacer, content, count=1, flags=re.DOTALL | re.IGNORECASE)
    
    if count > 0:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Failed to update {file}")
