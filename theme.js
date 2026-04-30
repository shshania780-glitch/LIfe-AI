// Theme Management
const ThemeManager = {
    // Get current theme from localStorage or system preference
    getCurrentTheme() {
        const savedTheme = localStorage.getItem('lifeai-theme');
        if (savedTheme) {
            return savedTheme;
        }
        
        // Check system preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        return 'light';
    },
    
    // Set theme
    setTheme(theme) {
        const html = document.documentElement;
        
        if (theme === 'dark') {
            html.classList.add('dark-mode');
            localStorage.setItem('lifeai-theme', 'dark');
            this.updateToggleButton('☀️');
        } else {
            html.classList.remove('dark-mode');
            localStorage.setItem('lifeai-theme', 'light');
            this.updateToggleButton('🌙');
        }
    },
    
    // Toggle theme
    toggleTheme() {
        const currentTheme = document.documentElement.classList.contains('dark-mode') ? 'dark' : 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        this.setTheme(newTheme);
    },
    
    // Update toggle button text
    updateToggleButton(text) {
        const toggle = document.querySelector('.theme-toggle span');
        if (toggle) {
            toggle.textContent = text;
        }
    },
    
    // Initialize theme
    init() {
        const theme = this.getCurrentTheme();
        this.setTheme(theme);
        
        // Setup toggle button
        const toggleBtn = document.querySelector('.theme-toggle');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', () => this.toggleTheme());
        }
        
        // Listen for system theme changes
        if (window.matchMedia) {
            window.matchMedia('(prefers-color-scheme: dark)').addListener((e) => {
                if (!localStorage.getItem('lifeai-theme')) {
                    this.setTheme(e.matches ? 'dark' : 'light');
                }
            });
        }
    }
};

// Initialize theme when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    ThemeManager.init();
});

// Also try to init immediately in case script loads after DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        ThemeManager.init();
    });
} else {
    ThemeManager.init();
}
