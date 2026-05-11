import glob

nav_find = """            <a href="./index.html" class="logo">
                <img src="./assets/images/bbs_logo.png" alt="BBS Logo" style="height: 60px; width: auto; object-fit: contain;">
            </a>"""
nav_replace = """            <a href="./index.html" class="logo logo-link">
                <img src="./assets/images/bbs-logo.png" alt="Bulisolevu Bookkeeping Services - BBS" class="logo-img" width="120" height="48">
            </a>"""

footer_find = """                    <div class="logo" style="margin-bottom: 1rem;">
                        <img src="./assets/images/bbs_logo.png" alt="BBS Logo" class="footer-logo" style="height: 60px; width: auto; object-fit: contain;">
                    </div>"""
footer_replace = """                    <div class="logo" style="margin-bottom: 1rem;">
                        <img src="./assets/images/bbs-logo.png" alt="Bulisolevu Bookkeeping Services - BBS" class="footer-logo" width="150" height="60">
                    </div>"""

head_find = """    <link rel="stylesheet" href="./css/styles.css">
</head>"""
head_replace = """    <link rel="stylesheet" href="./css/styles.css">
    <link rel="icon" type="image/png" href="./assets/images/bbs-logo-favicon.png">
</head>"""

html_files = glob.glob('public/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace(nav_find, nav_replace)
    content = content.replace(footer_find, footer_replace)
    content = content.replace(head_find, head_replace)

    # fallback
    content = content.replace('bbs_logo.png', 'bbs-logo.png')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Updated {len(html_files)} files.')
