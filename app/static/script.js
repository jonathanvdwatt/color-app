document.addEventListener('DOMContentLoaded', () => {
    const targetShape = document.getElementById('target-shape');
    const colorValueDisplay = document.getElementById('color-value');

    function fetchAndUpdateColor() {
        fetch('/config')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                const color = data.color || 'grey';
                console.log('Received color:', color);
                targetShape.style.backgroundColor = color;
                colorValueDisplay.textContent = color;
            })
            .catch(error => {
                console.error('Error fetching config:', error);
                targetShape.style.backgroundColor = 'grey';
                colorValueDisplay.textContent = 'Error';
            });
    }

    fetchAndUpdateColor();

    // Optionally, poll every few seconds to show updates without full page refresh
    // (though Argo CD rollouts usually involve new pods, making polling less critical here)
    // setInterval(fetchAndUpdateColor, 5000); // Poll every 5 seconds
}); 