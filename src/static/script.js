document.querySelector('form').addEventListener('submit', function(event) {
    const input = document.querySelector('#userInput').value;
    if (!input) {
        alert('Input is required!');
        event.preventDefault();
    }
});
