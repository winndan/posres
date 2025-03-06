
    // Add click handler for category items
    const categoryItems = document.querySelectorAll('.category-item');
    const foodCategories = document.querySelectorAll('.food-category');
    
    categoryItems.forEach(item => {
        item.addEventListener('click', () => {
            // Remove active class from all items
            categoryItems.forEach(i => i.classList.remove('active'));
            // Add active class to clicked item
            item.classList.add('active');
            
            // Show the corresponding food category
            const categoryId = item.getAttribute('data-category');
            
            // Hide all food categories
            foodCategories.forEach(category => {
                category.classList.remove('active');
            });
            
            // Show the selected category
            if (categoryId === 'all') {
                document.getElementById('all').classList.add('active');
            } else {
                document.getElementById(categoryId).classList.add('active');
            }
        });
    });
    
    // Add to cart functionality
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const menuItem = this.closest('.menu-item');
            const menuName = menuItem.querySelector('.menu-name').textContent;
            const menuPrice = menuItem.querySelector('.menu-price').textContent;
            
            alert(`Added to cart: ${menuName} - ${menuPrice}`);
            // In a real app, you would add the item to a cart object and update the UI
        });
    });
