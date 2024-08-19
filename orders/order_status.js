
document.getElementById("check-status-button").addEventListener("click", function() {
    const orderId = document.getElementById("order-id").value;

    fetch(`/api/order_status/${orderId}/`)
        .then(response => response.json())
        .then(data => {
            console.log("Received status:", data.status); // Log the received status
            updateProgressBar(data.status);
        })
        .catch(error => console.error('Error:', error));
});

function updateProgressBar(status) {
    const steps = document.querySelectorAll(".progress-step");
    console.log(steps)
    // Reset all steps
    steps.forEach(step => step.classList.remove("active"));

    // Map status to progress index
    const statusMapping = {
        'Order placed': 0,
        'Shipped': 1,
        'Out for Delivery': 2,
        'Delivered': 3
    };

    const statusIndex = statusMapping[status] || 0;  // Default to 'Order placed'

    // Activate steps up to the current status
    for (let i = 0; i <= statusIndex; i++) {

        steps[i].classList.add("active");

    }
}

console.log("Order status:", status); 

