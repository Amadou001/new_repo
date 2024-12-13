
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

function addNewImageField(input) {
    // Check if the file input has a value (an image was selected)
    if (input.files.length > 0) {
        // Create a new div for the additional image input
        const newDiv = document.createElement('div'); // No class assignment
        newDiv.className = 'col-md-6 mb-3';

        // Create new file input
        const newFileInput = document.createElement('input');
        newFileInput.type = 'file';
        newFileInput.className = 'form-control';
        newFileInput.accept = 'image/*';
        newFileInput.name = 'additionalImages';
        newFileInput.required = false;
        newFileInput.onchange = function() { addNewImageField(this); };

        // Create label for image description
        const label = document.createElement('label');
        label.className = 'form-label'; // Ensure it has form-label class for styling
        label.innerText = 'Image Description';

        // Create new select input for description
        const newSelect = document.createElement('select');
        newSelect.className = 'form-select'; // Ensure it has form-select class for styling
        newSelect.name = 'additionalDescriptions'; // Name for the form
        newSelect.required = false; // Make it required

        // Add options to the select input
        const options = [
            { value: "", text: "Select an image description" },
            { value: "main_entrance", text: "Main Entrance" },
            { value: "kitchen", text: "Kitchen" },
            { value: "living_room", text: "Living Room" },
            { value: "bedroom", text: "Bedroom" },
            { value: "bathroom", text: "Bathroom" },
            { value: "balcony", text: "Balcony" }
        ];

        // Create and append options to the select element
        options.forEach(optionData => {
            const option = document.createElement('option');
            option.value = optionData.value;
            option.text = optionData.text;
            newSelect.appendChild(option);
        });

        // Append new elements to the new div
        newDiv.appendChild(newFileInput);
        newDiv.appendChild(label); // Append label before the select
        newDiv.appendChild(newSelect); // Append the select element after the label

        // Append the new div to the container
        document.getElementById('imageContainer').appendChild(newDiv);
    }
}

// Property description text
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


// Close conversation modal
function closeConversation() {
    const modal = document.getElementById('ConversationModal');
    const modalInstance = bootstrap.Modal.getInstance(modal);
    modalInstance.hide();
}

// Initialize socket connection once
const socketio = io();

// Function to send a message
function sendMessage() {
    const messageInput = document.getElementById("newMessage");
    const messageText = messageInput.value.trim();
    const messageList = document.getElementById("messageList");

    if (messageText) {
        const currentDate = new Date();
        const formattedDate = currentDate.toLocaleString();

        // Update UI for the sender's message
        const newMessageItem = document.createElement("div");
        newMessageItem.className = "message-item sender-message";
        newMessageItem.style.display = "flex";
        newMessageItem.style.alignItems = "center";
        newMessageItem.style.justifyContent = "flex-end"; // Align to the right
        newMessageItem.style.margin = "10px 0";

        newMessageItem.innerHTML = `
            <div style="max-width: 60%; background-color: #e1ffc7; border-radius: 15px; padding: 10px;">
                <strong>You</strong>
                <p>${messageText}</p>
                <small style="display: block; margin-top: 5px; font-size: 0.8em; color: gray;">
                    ${formattedDate}
                </small>
            </div>
        `;

        messageList.appendChild(newMessageItem); // Append the sender's message

        // Emit the message to the server with the correct format
        socketio.emit("sendMessageToRoom", { 
            roomId: currentRoomId, 
            data: { message: messageText } // Ensure the message is wrapped inside 'data'
        });

        // Clear input and scroll to bottom
        messageInput.value = "";
        scrollToBottom();
    }
}


// Function to scroll to the bottom of the modal
function scrollToBottom() {
    const modalBody = document.querySelector("#ConversationModal .modal-body");
    modalBody.scrollTop = modalBody.scrollHeight;
}

// Function to handle opening a conversation
let currentRoomId = null;

function openConversation(roomId, name) {
    currentRoomId = roomId;

    // Remove existing listeners to prevent duplication
    socketio.off("message");

    // Listen for incoming messages from the server
    socketio.on("message", (data) => {
        const messageList = document.getElementById("messageList");
        const currentDate = new Date();
        const formattedDate = currentDate.toLocaleString();

        // Update UI for received messages
        const newMessageItem = document.createElement("div");
        newMessageItem.className = "message-item received-message";
        newMessageItem.style.display = "flex";
        newMessageItem.style.alignItems = "center";
        newMessageItem.style.justifyContent = "flex-start"; // Align to the left
        newMessageItem.style.margin = "10px 0";

        newMessageItem.innerHTML = `
            <div style="max-width: 60%; background-color: #d1e7ff; border-radius: 15px; padding: 10px;">
                <strong>${data.name || "Anonymous"}</strong>
                <p>${data.message}</p>
                <small style="display: block; margin-top: 5px; font-size: 0.8em; color: gray;">
                    ${formattedDate}
                </small>
            </div>
        `;

        messageList.appendChild(newMessageItem);
        scrollToBottom();
    });

    // Hide the message modal and show the conversation modal
    $("#MessageModalLabel").modal("hide");
    $("#ConversationModal").modal("show").on("shown.bs.modal", function () {
        scrollToBottom();
    });

    // Fetch messages from the backend
    fetch(`/auth/messages/${roomId}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to fetch conversation messages.");
            }
            return response.json();
        })
        .then((conversationData) => {
            // Update the conversation property (if available)
            const conversationProperty = $("#conversationProperty");
            if (conversationData.property_name && conversationData.property_url) {
                conversationProperty.html(
                    `<a href="${conversationData.property_url}" target="_blank" style="text-decoration: none; color: #00a547;">${conversationData.property_name}</a>`
                );
            } else {
                conversationProperty.text("Conversation");
            }

            // Populate messages
            const messageList = $("#messageList");
            messageList.empty();

            conversationData.messages.forEach((message) => {
                const messageElement = `
                    <div class="message-item" style="display: flex; justify-content: ${message.sender ? "flex-start" : "flex-end"}; margin-bottom: 10px;">
                        <div style="max-width: 60%; background-color: ${message.sender ? "#d1e7ff" : "#e1ffc7"}; border-radius: 15px; padding: 10px;">
                            <strong>${message.sender_name}</strong>
                            <p>${message.text}</p>
                            <small style="display: block; margin-top: 5px; font-size: 0.8em; color: gray;">${message.timestamp}</small>
                        </div>
                    </div>
                `;
                messageList.append(messageElement);
            });

            scrollToBottom();
        })
        .catch((error) => {
            console.error("Error fetching conversation messages:", error);
            $("#messageList").html("<p>Error loading messages. Please try again later.</p>");
        });
}

// Close the connection when the modal is closed
$("#ConversationModal").on("hidden.bs.modal", function () {
    currentRoomId = null; // Clear the current room ID
    socketio.off("message"); // Remove all listeners for the room
});

// Event listener for DOM content loaded
document.addEventListener('DOMContentLoaded', () => {
    const modalElement = document.getElementById('MessageModalLabel');
        
    if (modalElement) {
        modalElement.addEventListener('show.bs.modal', function () {
            console.log('Modal is opening, loading messages...');
            loadMessages();  // Load messages when modal opens
        });
    }
});
        
// Function to load messages for the message modal in th inbox bar 
async function loadMessages() {
    const messageList = document.querySelector('.message-list');
    if (!messageList) {
        console.error('Message list not found!');
        return;
    }
        
    messageList.innerHTML = ''; // Clear the previous messages
        
    try {
        const response = await fetch('/auth/messages');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        const messagesData = await response.json();
        
        // Populate the list with the fetched message data
        messagesData.forEach(msg => {
            const messageItemHTML = `
                <a href="#" style="text-decoration: none; color: inherit;" onclick="openConversation('${msg.room_id}')">
                    <div class="message-item" style="display: flex; align-items: center; cursor: pointer; margin-bottom: 10px;">
                        <img src="${msg.contact_image_url}" alt="${msg.contact_name}" style="height: 50px; width: 50px; border-radius: 50%; margin-right: 10px;">
                        <div>
                            <strong style="color: #007bff;">${msg.contact_name}</strong>
                            <p style="margin: 0; color: #333; ${msg.read_status ? '' : 'color: green;font-weight: bold;'}">${msg.latest_message}</p>
                        </div>
                    </div>
                </a>
            `;
        
            messageList.innerHTML += messageItemHTML;
        });
    } catch (error) {
        console.error('Error loading messages:', error);
        messageList.innerHTML = '<p>Error loading messages. Please try again later.</p>';
    }
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


/**
 * password checking while signing up
 */
function validateForm() {
    var password = document.getElementById("signUpPassword").value;
    var confirmPassword = document.getElementById("confirmPassword").value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return false; // Prevent form submission
    }
    return true; // Allow form submission
}

    // When the number of fields is entered, generate the fields
    document.getElementById('agentFieldCount').addEventListener('input', function() {
        const fieldCount = parseInt(this.value);  // Get the number of fields entered
        const container = document.getElementById("agentFieldsContainer");

        // Clear existing fields in case user changes the number
        container.innerHTML = "";

        // Generate the specified number of fields
        for (let i = 1; i <= fieldCount; i++) {
            const newField = document.createElement("div");
            newField.className = "col-12 col-sm-6 col-md-6 mb-3";

            // Create the file input for the agent image
            const imageInput = document.createElement("input");
            imageInput.type = "file";
            imageInput.className = "form-control";
            imageInput.accept = "image/*";
            imageInput.required = true;
            imageInput.name = `agentImage${i}`;

            // Create the text input for the agent name
            const nameInput = document.createElement("input");
            nameInput.type = "text";
            nameInput.className = "form-control mt-2";
            nameInput.placeholder = "Agent name";
            nameInput.required = true;
            nameInput.name = `agentName${i}`;

            // Append the new fields to the container
            newField.appendChild(imageInput);
            newField.appendChild(nameInput);

            // Add the new field to the container
            container.appendChild(newField);
        }
    });
