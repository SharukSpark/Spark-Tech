let carousel = document.querySelector('.carousel');
let listHTML = document.querySelector('.carousel .list');

const showSlider = (type) => {
    let items = document.querySelectorAll('.carousel .list .item');
    if (type === 'next') {
        listHTML.appendChild(items[0]);
        carousel.classList.add('next');
    } else {
        listHTML.prepend(items[items.length - 1]);
        carousel.classList.add('prev');
    }
    setTimeout(() => {
        carousel.classList.remove('next', 'prev');
    }, 2000);
}

// Automatically change slides every 5 seconds
setInterval(() => {
    showSlider('next');
}, 5000);