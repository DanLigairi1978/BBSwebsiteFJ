import glob

html_files = glob.glob('public/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add favicon right before </head> if not already there
    if 'rel="icon"' not in content:
        content = content.replace('</head>', '    <link rel="icon" type="image/png" href="./assets/images/bbs-logo-favicon.png">\n</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f'Updated favicons.')
