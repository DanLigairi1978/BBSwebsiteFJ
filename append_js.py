import os

js_file = 'public/js/main.js'

js_code = """
/* ================================
   THEME TOGGLE FUNCTIONALITY
   ================================ */

// Initialize theme on page load (runs immediately to prevent flash)
(function initTheme() {
  const savedTheme = localStorage.getItem('bbs-theme');
  if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('bbs-theme', 'light');
  }
})();

document.addEventListener('DOMContentLoaded', () => {
  setupThemeToggle();
});

// Setup theme toggle button
function setupThemeToggle() {
  const toggleBtn = document.getElementById('theme-toggle');
  
  if (!toggleBtn) {
    return;
  }
  
  toggleBtn.addEventListener('click', function() {
    toggleTheme();
  });
  
  toggleBtn.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      toggleTheme();
    }
  });
}

// Toggle between light and dark theme
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('bbs-theme', newTheme);
  
  document.body.classList.add('theme-transitioning');
  setTimeout(() => {
    document.body.classList.remove('theme-transitioning');
  }, 300);
}
"""

with open(js_file, 'a', encoding='utf-8') as f:
    f.write(js_code)

print("JS appended")
