console.log('Holas');

const message_timeout = document.getElementById('message-timer');

if (message_timeout) {
    setTimeout(function() {
        message_timeout.style.display = 'none';
    }, 4000);
}

