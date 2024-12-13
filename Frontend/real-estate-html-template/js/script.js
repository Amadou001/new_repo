document.addEventListener('DOMContentLoaded', () => {
    const minPriceInput = document.getElementById('minPrice');
    const maxPriceInput = document.getElementById('maxPrice');
    const selectedRange = document.getElementById('selectedRange');
    const priceRangeInput = document.getElementById('priceRangeInput');
    const applyPriceRangeBtn = document.getElementById('applyPriceRange');

    function updateSelectedRange() {
        const minPrice = parseInt(minPriceInput.value);
        const maxPrice = parseInt(maxPriceInput.value);

        if (minPrice > maxPrice) {
            minPriceInput.value = maxPrice;
        } else if (maxPrice < minPrice) {
            maxPriceInput.value = minPrice;
        }

        selectedRange.textContent = `Selected: $${minPriceInput.value} - $${maxPriceInput.value}`;
    }

    updateSelectedRange();

    minPriceInput.addEventListener('input', updateSelectedRange);
    maxPriceInput.addEventListener('input', updateSelectedRange);

    applyPriceRangeBtn.addEventListener('click', () => {
        const minPrice = minPriceInput.value;
        const maxPrice = maxPriceInput.value;
        priceRangeInput.value = `Price range: $${minPrice} - $${maxPrice}`;
    });
});




// This function is called when a file input changes
function addNewImageField(input) {
    // Check if the file input has a value (an image was selected)
    if (input.files.length > 0) {
        // Create a new div for the additional image input
        const newDiv = document.createElement('div');
        newDiv.className = 'col-md-6 mb-3';

        // Create new file input
        const newFileInput = document.createElement('input');
        newFileInput.type = 'file';
        newFileInput.className = 'form-control';
        newFileInput.accept = 'image/*';
        newFileInput.required = true;
        newFileInput.onchange = function() { addNewImageField(this); };

        // Create new text input for description
        const newTextInput = document.createElement('input');
        newTextInput.type = 'text';
        newTextInput.className = 'form-control mt-2';
        newTextInput.placeholder = 'Image Description';
        newTextInput.required = true;

        // Append new inputs to the new div
        newDiv.appendChild(newFileInput);
        newDiv.appendChild(newTextInput);

        // Append the new div to the container
        document.getElementById('imageContainer').appendChild(newDiv);
    }
}

// This function is called when a file input changes
function addNewImageField(input) {
    // Check if the file input has a value (an image was selected)
    if (input.files.length > 0) {
        // Create a new div for the additional image input and agent name input
        const newDiv = document.createElement('div');
        newDiv.className = 'col-12 col-sm-6 col-md-6 mb-3';

        // Create new file input for agent image
        const newFileInput = document.createElement('input');
        newFileInput.type = 'file';
        newFileInput.className = 'form-control';
        newFileInput.accept = 'image/*';
        newFileInput.required = true;
        newFileInput.onchange = function() { addNewImageField(this); };

        // Create new text input for agent name
        const newTextInput = document.createElement('input');
        newTextInput.type = 'text';
        newTextInput.className = 'form-control mt-2';
        newTextInput.placeholder = 'Agent name';
        newTextInput.required = true;

        // Append new inputs to the new div
        newDiv.appendChild(newFileInput);
        newDiv.appendChild(newTextInput);

        // Append the new div to the container
        document.getElementById('imageContainer').appendChild(newDiv);
    }
}

// modalHandler.js

function setupModalToggle(signInButtonId, signUpModalId, forgotPasswordModalId, addPropertyModalId) {
    // Get references to the sign-in button and the modals
    const signInButton = document.getElementById(signInButtonId);
    const signUpModal = document.getElementById(signUpModalId);
    const forgotPasswordModal = document.getElementById(forgotPasswordModalId);
    const addPropertyModal = document.getElementById(addPropertyModalId);

    // Function to hide the sign-in button
    function hideSignInButton() {
        signInButton.style.display = 'none';
    }

    // Function to show the sign-in button
    function showSignInButton() {
        signInButton.style.display = 'block';
    }

    // Add event listeners to the sign-up modal
    signUpModal.addEventListener('show.bs.modal', hideSignInButton);
    signUpModal.addEventListener('hidden.bs.modal', showSignInButton);

    // Add event listeners to the forgot password modal
    forgotPasswordModal.addEventListener('show.bs.modal', hideSignInButton);
    forgotPasswordModal.addEventListener('hidden.bs.modal', showSignInButton);

    // Add event listeners to the add property modal
    addPropertyModal.addEventListener('show.bs.modal', hideSignInButton);
    addPropertyModal.addEventListener('hidden.bs.modal', showSignInButton);
}

// Call the function to set up the modal toggle
document.addEventListener('DOMContentLoaded', function () {
    setupModalToggle('signInButton', 'signUpModal', 'forgotPasswordModal', 'addPropertyModal');
});

function readMore() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var linkText = document.getElementById("readMoreLink");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        linkText.innerHTML = "Read more"; 
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        linkText.innerHTML = "Read less"; 
        moreText.style.display = "inline";
    }
}


function closeConversation() {
    const modal = document.getElementById('ConversationModal');
    const modalInstance = bootstrap.Modal.getInstance(modal);
    modalInstance.hide();
}

function sendMessage() {
    const messageInput = document.getElementById('newMessage');
    const messageText = messageInput.value.trim();
    const messageList = document.getElementById('messageList');

    if (messageText) {
        // Create a new message item
        const newMessageItem = document.createElement('div');
        newMessageItem.className = 'message-item sender-message';
        newMessageItem.style.display = 'flex';
        newMessageItem.style.alignItems = 'center';
        newMessageItem.style.justifyContent = 'flex-end';
        newMessageItem.style.margin = '10px 0';

        newMessageItem.innerHTML = `
            <div style="max-width: 60%; background-color: #e1ffc7; border-radius: 15px; padding: 10px;">
                <strong>John Doe</strong>
                <p>${messageText}</p>
            </div>
        `;

        // Append the new message item to the message list
        messageList.appendChild(newMessageItem);

        // Clear the input field and scroll to the bottom
        messageInput.value = '';
        messageList.scrollTop = messageList.scrollHeight; // Scroll to the bottom
    }
}

function openConversation(name) {
    // Hide the message modal
    $('#MessageModalLabel').modal('hide');
    
    // Show the conversation modal
    $('#ConversationModal').modal('show');

    // Optionally, set the conversation name if needed
    $('#conversationName').text(name);
}

  // Function to collapse the navbar if it's open
  function closeNavbarIfOpen() {
    var navbarCollapse = document.getElementById('navbarCollapse');
    if (navbarCollapse.classList.contains('show')) {
        var navbarToggler = document.querySelector('.navbar-toggler');
        navbarToggler.click(); // Trigger the navbar toggle to close it
    }
}

// Listen for the Message modal opening
document.getElementById('MessageModalLabel').addEventListener('show.bs.modal', function () {
    closeNavbarIfOpen();
});

// Listen for the Sign In modal opening
document.getElementById('signInModal').addEventListener('show.bs.modal', function () {
    closeNavbarIfOpen();
});

// Listen for the add property modal opening
document.getElementById('addPropertyModal').addEventListener('show.bs.modal', function () {
    closeNavbarIfOpen();
});

// Function to go back to the message listing
function closeConversation() {
    // Close the Conversation Modal by dismissing it
    var conversationModal = document.getElementById('ConversationModal');
    var bsConversationModal = bootstrap.Modal.getInstance(conversationModal);
    bsConversationModal.hide();

    // Automatically show the Message Modal after the Conversation Modal is hidden
    conversationModal.addEventListener('hidden.bs.modal', function () {
        var messageModal = new bootstrap.Modal(document.getElementById('MessageModalLabel'));
        messageModal.show();
    }, { once: true }); // Event listener will be removed after it's triggered once
}


// Get references to the image and dropdown menu
const profilePic = document.getElementById('profilePic');
const profileDropdown = document.getElementById('profileDropdown');

// Add click event listener to the profile picture
profilePic.addEventListener('click', function (event) {
    // Prevent the click event from bubbling up to the window
    event.stopPropagation();
    
    // Toggle the visibility of the dropdown menu
    if (profileDropdown.style.display === 'none' || profileDropdown.style.display === '') {
        profileDropdown.style.display = 'block';
    } else {
        profileDropdown.style.display = 'none';
    }
});

// Close the dropdown menu if clicked outside of it
window.addEventListener('click', function(event) {
    if (!profilePic.contains(event.target) && !profileDropdown.contains(event.target)) {
        profileDropdown.style.display = 'none';
    }
});



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

document.getElementById('evaluateButton').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the page from refreshing

    const propertyId = document.getElementById('propertyIdInput').value;
    const monthlyCostElement = document.getElementById('subscriptionStatus');
    const costSection = document.getElementById('costSection');

    // Check if a property ID was entered only if the form is visible
    if (document.getElementById('subscriptionForm').style.display === "block" && propertyId) {
        // Simulating a cost calculation based on the property ID
        const monthlyCost = "15 000 GNF"; // Replace with dynamic cost calculation logic
        
        monthlyCostElement.textContent = monthlyCost; // Update the displayed amount
        costSection.style.display = "block"; // Show the cost section
    } else {
        alert("Please enter a valid Property ID.");
    }
});

// Redirect on button click
document.getElementById('payButton').addEventListener('click', function() {
    window.location.href = 'profile.html'; // Update this URL to your payment page
});

