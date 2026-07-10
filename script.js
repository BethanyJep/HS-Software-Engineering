(function () {
  'use strict';

  const slides = Array.from(document.querySelectorAll('.slide'));
  const dots = Array.from(document.querySelectorAll('.dot'));
  const previousButton = document.querySelector('#previous-button');
  const nextButton = document.querySelector('#next-button');
  const currentSlideLabel = document.querySelector('#current-slide');
  const progressBar = document.querySelector('#progress-bar');
  const slideStatus = document.querySelector('#slide-status');
  const fullscreenButton = document.querySelector('#fullscreen-button');
  let currentIndex = 0;

  function formatNumber(number) {
    return String(number + 1).padStart(2, '0');
  }

  function updateUrl(index) {
    const hash = `#slide-${index + 1}`;
    if (window.location.hash !== hash) {
      window.history.replaceState(null, '', hash);
    }
  }

  function showSlide(index, updateHash = true) {
    currentIndex = Math.max(0, Math.min(index, slides.length - 1));

    slides.forEach((slide, slideIndex) => {
      const isActive = slideIndex === currentIndex;
      slide.classList.toggle('is-active', isActive);
      slide.setAttribute('aria-hidden', String(!isActive));
    });

    dots.forEach((dot, dotIndex) => {
      const isActive = dotIndex === currentIndex;
      dot.classList.toggle('is-active', isActive);
      if (isActive) {
        dot.setAttribute('aria-current', 'true');
      } else {
        dot.removeAttribute('aria-current');
      }
    });

    currentSlideLabel.textContent = formatNumber(currentIndex);
    progressBar.style.width = `${((currentIndex + 1) / slides.length) * 100}%`;
    previousButton.disabled = currentIndex === 0;
    nextButton.disabled = currentIndex === slides.length - 1;
    slideStatus.textContent = `Slide ${currentIndex + 1} of ${slides.length}`;

    if (updateHash) {
      updateUrl(currentIndex);
    }
  }

  function moveBy(amount) {
    showSlide(currentIndex + amount);
  }

  function indexFromHash() {
    const match = window.location.hash.match(/^#slide-(\d+)$/);
    if (!match) {
      return 0;
    }
    return Math.max(0, Math.min(Number(match[1]) - 1, slides.length - 1));
  }

  previousButton.addEventListener('click', () => moveBy(-1));
  nextButton.addEventListener('click', () => moveBy(1));

  dots.forEach((dot, index) => {
    dot.addEventListener('click', () => showSlide(index));
  });

  document.addEventListener('keydown', (event) => {
    const activeElement = document.activeElement;
    const isTyping = activeElement && ['INPUT', 'TEXTAREA', 'SELECT'].includes(activeElement.tagName);

    if (isTyping) {
      return;
    }

    if (['ArrowRight', 'PageDown', ' '].includes(event.key)) {
      event.preventDefault();
      moveBy(1);
    } else if (['ArrowLeft', 'PageUp'].includes(event.key)) {
      event.preventDefault();
      moveBy(-1);
    } else if (event.key === 'Home') {
      event.preventDefault();
      showSlide(0);
    } else if (event.key === 'End') {
      event.preventDefault();
      showSlide(slides.length - 1);
    } else if (event.key.toLowerCase() === 'f') {
      event.preventDefault();
      toggleFullscreen();
    }
  });

  let touchStartX = 0;

  document.querySelector('.slide-viewport').addEventListener('touchstart', (event) => {
    touchStartX = event.changedTouches[0].screenX;
  }, { passive: true });

  document.querySelector('.slide-viewport').addEventListener('touchend', (event) => {
    const distance = event.changedTouches[0].screenX - touchStartX;
    if (Math.abs(distance) > 45) {
      moveBy(distance < 0 ? 1 : -1);
    }
  }, { passive: true });

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen?.();
    } else {
      document.exitFullscreen?.();
    }
  }

  fullscreenButton.addEventListener('click', toggleFullscreen);

  document.addEventListener('fullscreenchange', () => {
    const isFullscreen = Boolean(document.fullscreenElement);
    fullscreenButton.setAttribute('aria-label', isFullscreen ? 'Exit fullscreen' : 'Enter fullscreen');
    fullscreenButton.setAttribute('title', isFullscreen ? 'Exit fullscreen' : 'Enter fullscreen');
  });

  window.addEventListener('hashchange', () => showSlide(indexFromHash(), false));

  showSlide(indexFromHash(), false);
}());
