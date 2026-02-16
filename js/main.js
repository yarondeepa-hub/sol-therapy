/**
 * Main JavaScript - Sol Therapy
 * Interactions and functionality
 */

(function() {
    'use strict';

    // ========================================
    // DOM Elements
    // ========================================

    const header = document.querySelector('.header');
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav');
    const navBackdrop = document.querySelector('.nav-backdrop');
    const navLinks = document.querySelectorAll('.nav__link');
    const modals = document.querySelectorAll('.modal');
    const modalTriggers = document.querySelectorAll('[data-modal]');
    const modalCloses = document.querySelectorAll('.modal__close, .modal__backdrop');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery__item');
    const audioPlayerBtn = document.querySelector('.audio-player__btn');
    const audioProgress = document.querySelector('.audio-player__progress-bar');
    const floatingCta = document.querySelector('.floating-cta');
    const eventsSection = document.querySelector('#events');

    // ========================================
    // Header Scroll Effect
    // ========================================

    function handleScroll() {
        // Header scroll effect
        if (window.scrollY > 50) {
            header.classList.add('is-scrolled');
        } else {
            header.classList.remove('is-scrolled');
        }

        // Floating CTA visibility
        if (floatingCta && eventsSection) {
            const eventsRect = eventsSection.getBoundingClientRect();
            const isEventsVisible = eventsRect.top < window.innerHeight && eventsRect.bottom > 0;

            if (isEventsVisible) {
                floatingCta.classList.add('is-hidden');
            } else {
                floatingCta.classList.remove('is-hidden');
            }
        }
    }

    window.addEventListener('scroll', handleScroll, { passive: true });

    // ========================================
    // Mobile Navigation
    // ========================================

    function openNav() {
        nav.classList.add('is-open');
        navBackdrop.classList.add('is-visible');
        menuToggle.classList.add('is-active');
        document.body.style.overflow = 'hidden';
    }

    function closeNav() {
        nav.classList.remove('is-open');
        navBackdrop.classList.remove('is-visible');
        menuToggle.classList.remove('is-active');
        document.body.style.overflow = '';
    }

    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            if (nav.classList.contains('is-open')) {
                closeNav();
            } else {
                openNav();
            }
        });
    }

    if (navBackdrop) {
        navBackdrop.addEventListener('click', closeNav);
    }

    // Close nav when clicking a link
    navLinks.forEach(link => {
        link.addEventListener('click', closeNav);
    });

    // ========================================
    // Smooth Scroll for Anchor Links
    // ========================================

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();

                const headerHeight = header.offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ========================================
    // Modal Functionality
    // ========================================

    function openModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.add('is-active');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeModal(modal) {
        modal.classList.remove('is-active');
        document.body.style.overflow = '';
    }

    function closeAllModals() {
        modals.forEach(modal => closeModal(modal));
    }

    // Open modal on trigger click
    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', function(e) {
            e.preventDefault();
            const modalId = this.getAttribute('data-modal');
            openModal(modalId);
        });
    });

    // Close modal on close button or backdrop click
    modalCloses.forEach(closer => {
        closer.addEventListener('click', function() {
            const modal = this.closest('.modal');
            closeModal(modal);
        });
    });

    // Close modal on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeAllModals();
            closeNav();
        }
    });

    // ========================================
    // Gallery Filters
    // ========================================

    if (filterBtns.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                // Remove active class from all buttons
                filterBtns.forEach(b => b.classList.remove('is-active'));
                // Add active class to clicked button
                this.classList.add('is-active');

                const filter = this.getAttribute('data-filter');

                galleryItems.forEach(item => {
                    if (filter === 'all') {
                        item.style.display = '';
                        item.style.opacity = '1';
                    } else {
                        const category = item.getAttribute('data-category');
                        if (category === filter) {
                            item.style.display = '';
                            item.style.opacity = '1';
                        } else {
                            item.style.opacity = '0';
                            setTimeout(() => {
                                item.style.display = 'none';
                            }, 300);
                        }
                    }
                });
            });
        });
    }

    // ========================================
    // Audio Player
    // ========================================

    let isPlaying = false;
    let audioElement = null;

    if (audioPlayerBtn) {
        audioPlayerBtn.addEventListener('click', function() {
            if (!audioElement) {
                // Create audio element on first play
                audioElement = new Audio();
                audioElement.src = 'assets/audio/sample.mp3'; // Replace with actual audio file

                audioElement.addEventListener('timeupdate', function() {
                    const progress = (audioElement.currentTime / audioElement.duration) * 100;
                    if (audioProgress) {
                        audioProgress.style.width = progress + '%';
                    }
                });

                audioElement.addEventListener('ended', function() {
                    isPlaying = false;
                    updatePlayButton();
                    if (audioProgress) {
                        audioProgress.style.width = '0%';
                    }
                });
            }

            if (isPlaying) {
                audioElement.pause();
                isPlaying = false;
            } else {
                audioElement.play().catch(e => {
                    console.log('Audio playback failed:', e);
                });
                isPlaying = true;
            }

            updatePlayButton();
        });
    }

    function updatePlayButton() {
        if (audioPlayerBtn) {
            const icon = audioPlayerBtn.querySelector('svg');
            if (icon) {
                if (isPlaying) {
                    // Pause icon
                    icon.innerHTML = '<rect x="6" y="4" width="4" height="16" fill="currentColor"/><rect x="14" y="4" width="4" height="16" fill="currentColor"/>';
                } else {
                    // Play icon
                    icon.innerHTML = '<path d="M8 5v14l11-7z" fill="currentColor"/>';
                }
            }
        }
    }

    // ========================================
    // Newsletter Form
    // ========================================

    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value;

            if (validateEmail(email)) {
                // Here you would send to your newsletter service
                console.log('Newsletter signup:', email);

                // Show success message
                showNotification('תודה על ההרשמה!', 'success');
                emailInput.value = '';
            } else {
                showNotification('נא להזין כתובת אימייל תקינה', 'error');
            }
        });
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // ========================================
    // Notification System
    // ========================================

    function showNotification(message, type = 'info') {
        // Remove existing notifications
        const existingNotification = document.querySelector('.notification');
        if (existingNotification) {
            existingNotification.remove();
        }

        const notification = document.createElement('div');
        notification.className = `notification notification--${type}`;
        notification.innerHTML = `
            <span class="notification__message">${message}</span>
            <button class="notification__close" aria-label="סגור">&times;</button>
        `;

        // Add styles inline (or move to CSS)
        notification.style.cssText = `
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            padding: 16px 24px;
            background-color: ${type === 'success' ? 'var(--color-gold)' : type === 'error' ? 'var(--color-vermilion)' : 'var(--color-ink)'};
            color: ${type === 'success' ? 'var(--color-ink)' : 'var(--color-text-light)'};
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            gap: 12px;
            z-index: 9999;
            animation: slideUp 0.3s ease;
        `;

        document.body.appendChild(notification);

        // Close on button click
        notification.querySelector('.notification__close').addEventListener('click', function() {
            notification.remove();
        });

        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.style.animation = 'slideDown 0.3s ease forwards';
                setTimeout(() => notification.remove(), 300);
            }
        }, 5000);
    }

    // Add notification animation keyframes
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideUp {
            from {
                transform: translateX(-50%) translateY(100%);
                opacity: 0;
            }
            to {
                transform: translateX(-50%) translateY(0);
                opacity: 1;
            }
        }
        @keyframes slideDown {
            from {
                transform: translateX(-50%) translateY(0);
                opacity: 1;
            }
            to {
                transform: translateX(-50%) translateY(100%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);

    // ========================================
    // Intersection Observer for Animations
    // ========================================

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements that should animate on scroll
    document.querySelectorAll('.event-card, .gallery__item, .about__content, .about__image').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Add animation styles for observed elements
    const animStyle = document.createElement('style');
    animStyle.textContent = `
        .is-visible {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(animStyle);

    // ========================================
    // Language Toggle (placeholder)
    // ========================================

    const langToggle = document.querySelector('.lang-toggle');
    if (langToggle) {
        langToggle.addEventListener('click', function() {
            // This would toggle between Hebrew and English
            // For now, just show a notification
            showNotification('שינוי שפה בקרוב', 'info');
        });
    }

    // ========================================
    // Event Card Registration (placeholder)
    // ========================================

    document.querySelectorAll('.event-card .btn--primary').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const eventCard = this.closest('.event-card');
            const eventTitle = eventCard.querySelector('.event-card__title').textContent;

            // Here you would redirect to registration or open a form
            console.log('Registration for:', eventTitle);
            showNotification(`נרשמים ל: ${eventTitle}`, 'info');
        });
    });

    // ========================================
    // Initialize
    // ========================================

    // Run scroll handler once on load
    handleScroll();

    console.log('Sol Therapy website initialized');

})();
