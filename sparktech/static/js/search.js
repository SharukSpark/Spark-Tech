document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const suggestionsBox = document.getElementById('suggestions-box');

    searchInput.addEventListener('input', function () {
        const query = searchInput.value.trim();
        if (query.length > 0) {
            fetch(`/search-suggestions/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsBox.innerHTML = '';
                    data.forEach(item => {
                        const suggestionItem = document.createElement('li');
                        suggestionItem.classList.add('suggestion-item');
                        suggestionItem.textContent = item.name;

                        // Navigate to the item URL when clicked
                        suggestionItem.addEventListener('click', function () {
                            window.location.href = item.url;
                        });

                        suggestionsBox.appendChild(suggestionItem);
                    });
                });
        } else {
            suggestionsBox.innerHTML = '';
        }
    });

    // Hide suggestions when clicking outside
    document.addEventListener('click', function (event) {
        if (!suggestionsBox.contains(event.target) && !searchInput.contains(event.target)) {
            suggestionsBox.innerHTML = '';
        }
    });
});

