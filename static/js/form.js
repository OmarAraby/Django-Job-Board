
window.addEventListener('pageshow', function (event) {
    var form = document.getElementById('myForm');
    form.reset();
});


function preventFormResubmission(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Disable the submit button
    var submitButton = document.getElementById('submitBtn');
    submitButton.disabled = true;

    // Submit the form using AJAX
    var form = document.getElementById('myForm');
    var formData = new FormData(form);

    // Get the selected language from the language select element
    var languageSelect = document.getElementById('languageSelect');
    var selectedLanguage = languageSelect.value;

    // Add the selected language to the form data
    formData.append('language', selectedLanguage);

    // Display processing message
    var processingMessage = document.createElement('p');
    processingMessage.textContent = getProcessingMessage(selectedLanguage);
    processingMessage.style.color = 'black'; // Set the font color to black
    form.appendChild(processingMessage);

    // Make an AJAX request to submit the form data
    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.onload = function () {
        // Handle the AJAX response if needed
        // Optionally, display a success message to the user
        processingMessage.remove();

        var successMessage = document.createElement('p');
        successMessage.textContent = getSuccessMessage(selectedLanguage);
        successMessage.style.color = 'black'; // Set the font color to black
        form.appendChild(successMessage);

        // Reset the form fields
        form.reset();

        // Remove the success message after 5 seconds
        setTimeout(function () {
            successMessage.remove();

            // Enable the submit button
            submitButton.disabled = false;
        }, 5000);
    };
    xhr.send(formData);
}

function getProcessingMessage(language) {
    // Check the language and return the appropriate processing message
    if (language === 'ar') {
        return 'جاري الإرسال...';
    } else {
        return 'Submitting...';
    }
}

function getSuccessMessage(language) {
    // Check the language and return the appropriate success message
    if (language === 'ar') {
        return 'تم إرسال النموذج بنجاح!';
    } else {
        return 'Form submitted successfully!';
    }
}

