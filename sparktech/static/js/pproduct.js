
// < !--Bootstrap 5 JS and dependencies-- >

    document.addEventListener('DOMContentLoaded', () => {
        const buttons = document.querySelectorAll('#productButtonGroup button');
        const products = document.querySelectorAll('#productList .pproduct');

        buttons.forEach(button => {
            button.addEventListener('click', () => {
                const filter = button.getAttribute('data-filter');

                buttons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');

                products.forEach(product => {
                    if (filter === '*' || product.classList.contains(filter.substring(1))) {
                        product.classList.add('show');
                    } else {
                        product.classList.remove('show');
                    }
                });
            });
        });
    });
    
// <!--Products Section End-- >
