import re

css_file = 'public/css/styles.css'

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace variables
replacements = {
    '--obsidian': '--bg-primary',
    '--charcoal': '--bg-secondary',
    '--slate': '--bg-tertiary',
    '--fiji-gold': '--accent-gold',
    '--deep-ocean': '--accent-ocean',
    '--sunset-coral': '--accent-coral',
    '--text-white': '--text-primary',
    '--text-light': '--text-secondary'
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Now, we need to replace the root block.
# We'll locate the `:root {` block and replace it.
root_pattern = re.compile(r':root\s*\{[^}]+\}', re.MULTILINE)
new_root = '''/* ================================
   THEME VARIABLES
   ================================ */

/* DEFAULT: LIGHT THEME (loads first) */
:root {
  /* Backgrounds */
  --bg-primary: #FFFFFF;
  --bg-secondary: #F8F9FA;
  --bg-tertiary: #E9ECEF;
  
  /* Accents */
  --accent-gold: #D4AF37;
  --accent-ocean: #0A5F62;
  --accent-coral: #E85D5D;
  
  /* Text */
  --text-primary: #1A1A1A;
  --text-secondary: #4A4A4A;
  --text-muted: #6C757D;
  
  /* UI */
  --nav-bg: rgba(255, 255, 255, 0.95);
  --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  --border-color: rgba(0, 0, 0, 0.1);
  --hero-overlay: rgba(255, 255, 255, 0.85);

  /* Typography */
  --font-heading: 'Poppins', sans-serif;
  --font-body: 'Inter', sans-serif;

  /* Layout */
  --max-width: 1200px;
  --radius-card: 12px;
  --radius-button: 8px;
  --transition: all 0.3s ease;
  
  --text-contrast-ratio: 4.5;
}

/* DARK THEME (user toggles to this) */
:root[data-theme="dark"] {
  /* Backgrounds */
  --bg-primary: #1A1A1A;
  --bg-secondary: #2B2B2B;
  --bg-tertiary: #3A3A3A;
  
  /* Accents - SAME GOLD */
  --accent-gold: #D4AF37;
  --accent-ocean: #0D7377;
  --accent-coral: #FF6B6B;
  
  /* Text */
  --text-primary: #FFFFFF;
  --text-secondary: #E0E0E0;
  --text-muted: #999999;
  
  /* UI */
  --nav-bg: rgba(26, 26, 26, 0.95);
  --card-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
  --border-color: rgba(255, 255, 255, 0.1);
  --hero-overlay: rgba(26, 26, 26, 0.85);
  
  --text-contrast-ratio: 7;
}'''

content = root_pattern.sub(new_root, content, count=1)

# Add transition to body if not present
if 'transition: background-color' not in content:
    body_pattern = re.compile(r'body\s*\{([^}]+)\}')
    def body_repl(match):
        inner = match.group(1)
        if 'transition:' not in inner:
            inner += '  transition: background-color 0.3s ease, color 0.3s ease;\n'
        return 'body {' + inner + '}'
    content = body_pattern.sub(body_repl, content)

# Append specific light theme styles at the end
light_theme_styles = '''
/* ================================
   THEME TOGGLE STYLING
   ================================ */

.theme-toggle-container {
  display: flex;
  align-items: center;
  margin-left: 24px;
}

.theme-toggle-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 8px 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  color: var(--text-primary);
  font-size: 14px;
  font-weight: 500;
}

.theme-toggle-btn:hover {
  background: var(--bg-tertiary);
  border-color: var(--accent-gold);
  transform: translateY(-1px);
}

.theme-toggle-btn:active {
  transform: translateY(0);
}

/* Theme Icons */
.theme-icon {
  width: 20px;
  height: 20px;
  transition: transform 0.3s ease;
}

/* Show/Hide Icons Based on Theme */
:root .sun-icon {
  display: none;
}

:root .moon-icon {
  display: block;
}

:root[data-theme="dark"] .sun-icon {
  display: block;
}

:root[data-theme="dark"] .moon-icon {
  display: none;
}

.theme-toggle-btn:hover .theme-icon {
  transform: rotate(20deg);
}

@media (max-width: 768px) {
  .theme-toggle-label {
    display: none;
  }
  
  .theme-toggle-btn {
    padding: 10px;
    border-radius: 50%;
    width: 44px;
    height: 44px;
    justify-content: center;
  }
  
  .theme-toggle-container {
    margin-left: 12px;
  }
}

/* ================================
   LIGHT THEME SPECIFIC STYLES
   ================================ */

/* Hero Section - Light Mode */
:root[data-theme="light"] .hero {
  background: linear-gradient(135deg, #FFFFFF 0%, #F8F9FA 100%);
  position: relative;
}

:root[data-theme="light"] .hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(255, 255, 255, 0.85);
  z-index: 1;
}

:root[data-theme="light"] .hero-content {
  position: relative;
  z-index: 2;
}

/* Navigation - Light Mode */
:root[data-theme="light"] .navbar {
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

/* Buttons - Light Mode Adjustments */
:root[data-theme="light"] .btn-primary-gold {
  color: #1A1A1A;
  box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3);
}

:root[data-theme="light"] .btn-primary-gold:hover {
  box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
}

/* Cards - Light Mode */
:root[data-theme="light"] .service-block,
:root[data-theme="light"] .testimonial {
  background: #FFFFFF;
  border: 1px solid var(--border-color);
}

/* Footer - Light Mode */
:root[data-theme="light"] .footer {
  background: #F8F9FA;
  border-top: 2px solid var(--accent-gold);
}

/* WhatsApp Float - Always Green */
.whatsapp-float {
  background: #25D366;
}

/* Logo - Light Mode (if needed) */
:root[data-theme="light"] .footer-logo {
  filter: brightness(0.9);
}

/* Form Elements - Light Mode */
:root[data-theme="light"] input,
:root[data-theme="light"] textarea,
:root[data-theme="light"] select {
  background: #FFFFFF;
  border: 1px solid #DEE2E6;
}

:root[data-theme="light"] input::placeholder,
:root[data-theme="light"] textarea::placeholder {
  color: #6C757D;
}

/* ================================
   THEME TRANSITION ANIMATION
   ================================ */

body.theme-transitioning,
body.theme-transitioning * {
  transition: background-color 0.3s ease, 
              color 0.3s ease, 
              border-color 0.3s ease,
              box-shadow 0.3s ease !important;
}

* {
  transition-property: background-color, color, border-color, box-shadow;
  transition-duration: 0.3s;
  transition-timing-function: ease;
}

img, video, iframe {
  transition: none !important;
}

/* Focus indicators */
button:focus-visible,
a:focus-visible,
input:focus-visible {
  outline: 3px solid var(--accent-gold);
  outline-offset: 2px;
}
'''
if '.theme-toggle-container' not in content:
    content += light_theme_styles

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS updated successfully")
