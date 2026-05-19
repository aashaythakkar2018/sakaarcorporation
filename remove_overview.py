import os
import re

directory = '.'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Pattern 1: Any link containing "Back to Overview"
# Example: <a href="..." class="...">Back to Overview</a>
# Example 2: <a href="..."><i class="..."></i> Back to Overview</a>
back_to_overview_pattern = re.compile(r'<a[^>]*>\s*(?:<i[^>]*></i>\s*)?Back to Overview\s*</a>', re.IGNORECASE)

# Pattern 2: The mobile dropdown "Overview" link
# Example:
# <a href="./Our-Businesses.html" class="flex items-center py-2 px-4 text-gray-600 hover:text-primary">
# <i class="ri-grid-line mr-3 text-primary"></i>Overview
# </a>
overview_mobile_pattern = re.compile(r'<a href="\./Our-Businesses\.html"[^>]*>\s*<i[^>]*></i>\s*Overview\s*</a>', re.IGNORECASE)

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = back_to_overview_pattern.sub('', content)
    new_content = overview_mobile_pattern.sub('', new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed Overview links from {filename}")

print("Done.")
