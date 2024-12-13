/**
 * EValuate cost and corfirm payement function
 */
document.getElementById('evaluateButton').addEventListener('click', async function(event) {
    event.preventDefault(); // Prevent page refresh

    const propertyId = document.getElementById('propertyIdInput').value;
    const monthlyCostElement = document.getElementById('subscriptionStatus');
    const costSection = document.getElementById('costSection');

    if (propertyId) {
        try {
            // Send the property ID to the backend for cost evaluation
            const response = await fetch('/auth/evaluate-cost', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ property_id: propertyId })
            });

            if (response.ok) {
                const data = await response.json();
                const monthlyCost = data.monthly_cost;
                
                // Store monthly cost in session storage
                sessionStorage.setItem('monthly_cost', monthlyCost);
                
                monthlyCostElement.textContent = `${monthlyCost} GNF`; // Update displayed amount
                costSection.style.display = "block"; // Show the cost section
            } else {
                alert('Failed to retrieve cost. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again later.');
        }
    } else {
        alert("Please enter a valid Property ID.");
    }
});

// Redirect to confirmation page with property_id and monthly_cost
document.getElementById('payButton').addEventListener('click', async function() {
    const propertyId = document.getElementById('propertyIdInput').value;
    const storedMonthlyCost = sessionStorage.getItem('monthly_cost');

    if (propertyId && storedMonthlyCost) {
        try {
            // Confirming the monthly cost value before proceeding
            const response = await fetch('/auth/evaluate-cost', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ property_id: propertyId })
            });

            if (response.ok) {
                const data = await response.json();
                const monthlyCost = data.monthly_cost;
                
                // Redirect to the confirmation page with property_id and monthly_cost as query parameters
                window.location.href = `/auth/confirmation?property_id=${propertyId}&monthly_cost=${monthlyCost}`;
            } else {
                alert('Failed to proceed. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again later.');
        }
    } else {
        alert("Please complete the cost evaluation first.");
    }
});

/**
 * Update user infos
 */
document.getElementById("toggleUpdateBtn").addEventListener("click", function() {
    document.getElementById("userInfo").style.display = "none"; // Hide read-only info
    document.getElementById("updateForm").style.display = "block"; // Show editable form
});

document.getElementById("cancelUpdateBtn").addEventListener("click", function() {
    document.getElementById("updateForm").style.display = "none"; // Hide editable form
    document.getElementById("userInfo").style.display = "block"; // Show read-only info again
    window.scrollTo(0, 0);
    location.reload();  
});

// Property Boosting
document.getElementById('subscribeButton').addEventListener('click', function() {
    const subscriptionForm = document.getElementById('subscriptionForm');
    const propertyIdInput = document.getElementById('propertyIdInput');
            
     // Toggle visibility of the subscription form
    subscriptionForm.style.display = subscriptionForm.style.display === "none" ? "block" : "none";
            
    // Set the property ID input to required if the form is shown
    if (subscriptionForm.style.display === "block") {
        propertyIdInput.setAttribute('required', 'required');
    } else {
        propertyIdInput.removeAttribute('required');
        propertyIdInput.value = ''; // Clear input when hiding the form
    }
});

