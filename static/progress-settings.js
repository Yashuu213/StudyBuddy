// Progress and Settings Management System
// This file contains all functionality for tracking user progress and managing settings

// ============================================
// PROGRESS TRACKING SYSTEM
// ============================================

// Initialize progress data structure
function initializeProgress() {
    const defaultProgress = {
        completedTopics: [],
        quizScores: {},
        studyTime: {},
        lastStudied: null,
        streak: 0,
        totalTopics: 0,
        activityLog: []
    };

    const saved = localStorage.getItem('cbse_progress');
    return saved ? JSON.parse(saved) : defaultProgress;
}

// Save progress to localStorage
function saveProgress(progressData) {
    localStorage.setItem('cbse_progress', JSON.stringify(progressData));
}

// Get current progress
function getProgress() {
    return initializeProgress();
}

// Mark a topic as completed
function markTopicComplete(topicId, topicName) {
    const progress = getProgress();

    if (!progress.completedTopics.includes(topicId)) {
        progress.completedTopics.push(topicId);
        progress.lastStudied = new Date().toISOString();

        // Add to activity log
        if (!progress.activityLog) progress.activityLog = [];
        progress.activityLog.push({
            type: 'completion',
            topicName: topicName,
            date: new Date().toISOString()
        });

        saveProgress(progress);

        // Show completion notification
        showNotification(`✅ Completed: ${topicName}`, 'success');
    }
}

// Record quiz score
function recordQuizScore(topicId, topicName, score, total) {
    const progress = getProgress();

    if (!progress.quizScores[topicId]) {
        progress.quizScores[topicId] = [];
    }

    progress.quizScores[topicId].push({
        score: score,
        total: total,
        percentage: Math.round((score / total) * 100),
        date: new Date().toISOString(),
        topicName: topicName
    });

    // Add to activity log
    if (!progress.activityLog) progress.activityLog = [];
    progress.activityLog.push({
        type: 'quiz',
        topicName: topicName,
        score: score,
        total: total,
        percentage: Math.round((score / total) * 100),
        date: new Date().toISOString()
    });

    saveProgress(progress);
    showNotification(`Quiz Score: ${score}/${total} (${Math.round((score / total) * 100)}%)`, 'info');
}

// Calculate overall statistics
function calculateStats() {
    const progress = getProgress();
    const stats = {
        totalCompleted: progress.completedTopics.length,
        totalQuizzes: Object.keys(progress.quizScores).length,
        averageScore: 0,
        streak: calculateStreak(progress),
        recentActivity: getRecentActivity(progress)
    };

    // Calculate average quiz score
    let totalScore = 0;
    let totalAttempts = 0;

    Object.values(progress.quizScores).forEach(quizzes => {
        quizzes.forEach(quiz => {
            totalScore += quiz.percentage;
            totalAttempts++;
        });
    });

    stats.averageScore = totalAttempts > 0 ? Math.round(totalScore / totalAttempts) : 0;

    return stats;
}

// Calculate study streak
function calculateStreak(progress) {
    // Simple implementation: days since last studied
    if (!progress.lastStudied) return 0;

    const lastDate = new Date(progress.lastStudied);
    const today = new Date();
    const diffTime = Math.abs(today - lastDate);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

    return diffDays <= 1 ? (progress.streak || 1) : 0;
}

// Get recent activity
function getRecentActivity(progress) {
    // Return activity log if exists, otherwise fallback (or empty)
    let activities = progress.activityLog || [];

    // Sort by date (most recent first)
    activities.sort((a, b) => new Date(b.date) - new Date(a.date));

    return activities.slice(0, 10); // Return last 10 activities
}

// ============================================
// PROGRESS DASHBOARD UI
// ============================================

function showProgress() {
    const stats = calculateStats();
    const progress = getProgress();

    const container = document.getElementById('view-container');
    container.innerHTML = `
        <h1 style="margin-bottom: 2rem;">📊 Your Learning Progress</h1>
        
        <!-- Stats Grid -->
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Topics Completed</h3>
                <div class="stat-value">${stats.totalCompleted}</div>
                <div class="stat-label">Keep going!</div>
            </div>
            <div class="stat-card">
                <h3>Quiz Average</h3>
                <div class="stat-value">${stats.averageScore}%</div>
                <div class="stat-label">${stats.totalQuizzes} quizzes taken</div>
            </div>
            <div class="stat-card">
                <h3>Study Streak</h3>
                <div class="stat-value">${stats.streak}</div>
                <div class="stat-label">days</div>
            </div>
        </div>
        
        <!-- Recent Activity -->
        <div class="progress-section">
            <h2>📝 Recent Activity</h2>
            ${stats.recentActivity.length > 0 ? `
                <ul class="activity-list">
                    ${stats.recentActivity.map(activity => `
                        <li class="activity-item">
                            <div class="activity-info">
                                <div class="activity-title">${activity.topicName}</div>
                                <div class="activity-meta">
                                    ${formatDate(activity.date)} • ${activity.type === 'quiz' ? 'Quiz' : 'Completed'}
                                </div>
                            </div>
                            <div class="activity-score">
                                ${activity.type === 'quiz' ? activity.percentage + '%' : '✅'}
                            </div>
                        </li>
                    `).join('')}
                </ul>
            ` : `
                <div class="empty-state">
                    <div class="empty-state-icon">📚</div>
                    <div class="empty-state-title">No activity yet</div>
                    <div class="empty-state-description">Start learning to see your progress here!</div>
                </div>
            `}
        </div>
        
        <!-- Data Management -->
        <div class="progress-section">
            <h2>💾 Data Management</h2>
            <div class="settings-actions">
                <button class="settings-btn primary" onclick="exportProgress()">
                    📥 Export Progress
                </button>
                <button class="settings-btn danger" onclick="clearProgress()">
                    🗑️ Clear All Progress
                </button>
            </div>
        </div>
    `;

    updateBreadcrumb(['Progress']);
    updateNavActive('progress');
}

// ============================================
// SETTINGS SYSTEM
// ============================================

// Initialize settings
function initializeSettings() {
    const defaultSettings = {
        theme: 'dark',
        fontSize: 'medium',
        autoSave: true
    };

    const saved = localStorage.getItem('cbse_settings');
    return saved ? JSON.parse(saved) : defaultSettings;
}

// Save settings
function saveSettings(settings) {
    localStorage.setItem('cbse_settings', JSON.stringify(settings));
    applySettings(settings);
}

// Apply settings to the page
function applySettings(settings) {
    // Apply theme
    if (settings.theme === 'light') {
        document.body.classList.add('light-theme');
    } else {
        document.body.classList.remove('light-theme');
    }

    // Apply font size
    document.body.classList.remove('font-small', 'font-medium', 'font-large');
    document.body.classList.add(`font-${settings.fontSize}`);
}

// ============================================
// SETTINGS UI
// ============================================

function showSettings() {
    const settings = initializeSettings();

    const container = document.getElementById('view-container');
    container.innerHTML = `
        <h1 style="margin-bottom: 2rem;">⚙️ Settings</h1>
        
        <!-- Appearance Settings -->
        <div class="settings-section">
            <h2>🎨 Appearance</h2>
            <div class="setting-item">
                <div>
                    <div class="setting-label">Theme</div>
                    <div class="setting-description">Choose your preferred color scheme</div>
                </div>
                <div class="setting-control">
                    <select id="theme-select" onchange="updateSetting('theme', this.value)">
                        <option value="dark" ${settings.theme === 'dark' ? 'selected' : ''}>Dark</option>
                        <option value="light" ${settings.theme === 'light' ? 'selected' : ''}>Light</option>
                    </select>
                </div>
            </div>
            <div class="setting-item">
                <div>
                    <div class="setting-label">Font Size</div>
                    <div class="setting-description">Adjust text size for better readability</div>
                </div>
                <div class="setting-control">
                    <select id="font-size-select" onchange="updateSetting('fontSize', this.value)">
                        <option value="small" ${settings.fontSize === 'small' ? 'selected' : ''}>Small</option>
                        <option value="medium" ${settings.fontSize === 'medium' ? 'selected' : ''}>Medium</option>
                        <option value="large" ${settings.fontSize === 'large' ? 'selected' : ''}>Large</option>
                    </select>
                </div>
            </div>
        </div>
        
        <!-- Data Settings -->
        <div class="settings-section">
            <h2>💾 Data Management</h2>
            <div class="settings-actions">
                <button class="settings-btn primary" onclick="exportAllData()">
                    📥 Export All Data
                </button>
                <button class="settings-btn secondary" onclick="importData()">
                    📤 Import Data
                </button>
                <button class="settings-btn danger" onclick="resetAllData()">
                    ⚠️ Reset Everything
                </button>
            </div>
        </div>
        
        <!-- About -->
        <div class="settings-section">
            <h2>ℹ️ About</h2>
            <p style="color: var(--text-secondary); line-height: 1.6;">
                <strong>CBSE Learning Hub</strong><br>
                Version 1.0.0<br>
                AI-powered learning platform for CBSE students
            </p>
        </div>
    `;

    updateBreadcrumb(['Settings']);
    updateNavActive('settings');
}

// Update a single setting
function updateSetting(key, value) {
    const settings = initializeSettings();
    settings[key] = value;
    saveSettings(settings);
    showNotification(`Setting updated: ${key}`, 'success');
}

// ============================================
// DATA MANAGEMENT FUNCTIONS
// ============================================

// Export progress data
function exportProgress() {
    const progress = getProgress();
    const dataStr = JSON.stringify(progress, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `cbse-progress-${new Date().toISOString().split('T')[0]}.json`;
    link.click();
    URL.revokeObjectURL(url);
    showNotification('Progress exported successfully!', 'success');
}

// Export all data (progress + settings)
function exportAllData() {
    const data = {
        progress: getProgress(),
        settings: initializeSettings(),
        exportDate: new Date().toISOString()
    };
    const dataStr = JSON.stringify(data, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `cbse-data-${new Date().toISOString().split('T')[0]}.json`;
    link.click();
    URL.revokeObjectURL(url);
    showNotification('All data exported successfully!', 'success');
}

// Import data
function importData() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.json';
    input.onchange = (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.onload = (event) => {
            try {
                const data = JSON.parse(event.target.result);
                if (data.progress) {
                    localStorage.setItem('cbse_progress', JSON.stringify(data.progress));
                }
                if (data.settings) {
                    localStorage.setItem('cbse_settings', JSON.stringify(data.settings));
                    applySettings(data.settings);
                }
                showNotification('Data imported successfully!', 'success');
                showSettings(); // Refresh the settings page
            } catch (error) {
                showNotification('Error importing data. Invalid file format.', 'error');
            }
        };
        reader.readAsText(file);
    };
    input.click();
}

// Clear progress
function clearProgress() {
    if (confirm('Are you sure you want to clear all progress? This cannot be undone.')) {
        localStorage.removeItem('cbse_progress');
        showNotification('Progress cleared!', 'success');
        showProgress(); // Refresh the progress page
    }
}

// Reset all data
function resetAllData() {
    if (confirm('⚠️ WARNING: This will delete ALL your progress and settings. This cannot be undone. Are you absolutely sure?')) {
        localStorage.removeItem('cbse_progress');
        localStorage.removeItem('cbse_settings');
        const defaultSettings = initializeSettings();
        applySettings(defaultSettings);
        showNotification('All data has been reset!', 'success');
        goHome();
    }
}

// ============================================
// UTILITY FUNCTIONS
// ============================================

// Format date for display
function formatDate(dateString) {
    const date = new Date(dateString);
    const now = new Date();
    const diffTime = Math.abs(now - date);
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));

    if (diffDays === 0) return 'Today';
    if (diffDays === 1) return 'Yesterday';
    if (diffDays < 7) return `${diffDays} days ago`;

    return date.toLocaleDateString();
}

// Show notification
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 2rem;
        right: 2rem;
        background: ${type === 'success' ? 'rgba(34, 197, 94, 0.9)' : type === 'error' ? 'rgba(239, 68, 68, 0.9)' : 'rgba(56, 189, 248, 0.9)'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        z-index: 1000;
        animation: slideIn 0.3s ease;
        font-weight: 500;
    `;
    notification.textContent = message;
    document.body.appendChild(notification);

    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Update navigation active state
function updateNavActive(page) {
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });

    const navItems = document.querySelectorAll('.nav-item');
    if (page === 'home' && navItems[0]) navItems[0].classList.add('active');
    if (page === 'progress' && navItems[1]) navItems[1].classList.add('active');
    if (page === 'settings' && navItems[2]) navItems[2].classList.add('active');
}

// ============================================
// INITIALIZATION
// ============================================

// Apply saved settings on page load
document.addEventListener('DOMContentLoaded', () => {
    const settings = initializeSettings();
    applySettings(settings);
});

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
