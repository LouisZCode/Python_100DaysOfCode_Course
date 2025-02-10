document.addEventListener('DOMContentLoaded', function() {
    const confirmBtn = document.getElementById('confirmBtn');
    const declineBtn = document.getElementById('declineBtn');
    const responseMessage = document.getElementById('response-message');

    confirmBtn.addEventListener('click', function() {
        responseMessage.style.color = '#4CAF50';
        responseMessage.textContent = 'Thank you for confirming! We look forward to seeing you! 🎉';
        
        // Disable both buttons after response
        confirmBtn.disabled = true;
        declineBtn.disabled = true;
        
        // Add some visual feedback
        confirmBtn.style.opacity = '0.7';
        declineBtn.style.opacity = '0.5';
    });

    declineBtn.addEventListener('click', function() {
        responseMessage.style.color = '#ff4444';
        responseMessage.textContent = 'We\'re sorry you can\'t make it. Maybe next time! 😢';
        
        // Disable both buttons after response
        confirmBtn.disabled = true;
        declineBtn.disabled = true;
        
        // Add some visual feedback
        confirmBtn.style.opacity = '0.5';
        declineBtn.style.opacity = '0.7';
    });
}); 