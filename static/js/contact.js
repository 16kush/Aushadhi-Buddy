// Wait for the DOM to be ready
document.addEventListener('DOMContentLoaded', function () {
    // Get the form element
    const contactForm = document.getElementById('contactForm');
  
    // Add event listener to the form submit
    contactForm.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form submission and page reload
  
      // Get the form values
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const message = document.getElementById('message').value;
  
      // Validate the form data (You can add more validation as needed)
      if (name.trim() === '' || email.trim() === '' || message.trim() === '') {
        alert('Please fill in all fields before submitting.');
        return;
      }
  
      // Send the form data to the server (You can use fetch or AJAX here)
      // Replace the URL with your server endpoint to handle the form data
      const formData = {
        name,
        email,
        message,
      };
  
      // Example using fetch (you can use any other AJAX method)
      fetch('/submit_form', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
        .then((response) => response.json())
        .then((data) => {
          // Handle the server response (e.g., show success message)
          alert(data.message);
          // Clear the form fields
          document.getElementById('name').value = '';
          document.getElementById('email').value = '';
          document.getElementById('message').value = '';
        })
        .catch((error) => {
          // Handle any errors that occurred during form submission
          console.error('Error submitting form:', error);
          alert('An error occurred while submitting the form. Please try again later.');
        });
    });
  });
  