// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileMenuBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Active link highlighting
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const links = document.querySelectorAll('.nav-links a');
    
    links.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        }
    });

    // FAQ Accordion
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const item = question.parentElement;
            const isActive = item.classList.contains('active');
            
            // Close all
            document.querySelectorAll('.faq-item').forEach(faq => {
                faq.classList.remove('active');
                faq.querySelector('.fas').classList.remove('fa-chevron-up');
                faq.querySelector('.fas').classList.add('fa-chevron-down');
            });

            // Open clicked if it wasn't active
            if (!isActive) {
                item.classList.add('active');
                question.querySelector('.fas').classList.remove('fa-chevron-down');
                question.querySelector('.fas').classList.add('fa-chevron-up');
            }
        });
    });

    // Simple Contact Form submission (prevent default for demo)
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;

            // Simulate form submission
            setTimeout(() => {
                contactForm.reset();
                submitBtn.textContent = 'Message Sent Successfully!';
                submitBtn.classList.remove('btn-primary');
                submitBtn.classList.add('bg-success', 'text-white');
                submitBtn.style.backgroundColor = 'var(--success)';
                
                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.backgroundColor = '';
                    submitBtn.classList.add('btn-primary');
                    submitBtn.classList.remove('bg-success', 'text-white');
                }, 3000);
            }, 1500);
        });
    }
});

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
