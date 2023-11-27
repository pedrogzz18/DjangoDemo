"use strict";
var pk;
function showDialog(url) {
    // Use window.prompt to show a dialog box for user input
    const userInput = window.prompt('User you want to share this book with:');
    if (userInput !== null) {
        const confirmacion = confirm('Are you sure you want to share this book with: ' + userInput);
        if (confirmacion) {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', url, true);
            const cookieMatch = document.cookie.match(/csrftoken=([^ ;]+)/);
            if (cookieMatch && cookieMatch[1]) {
                const csrfToken = cookieMatch[1];
                // Now you can include `csrfToken` in your AJAX request headers.
                xhr.setRequestHeader('X-CSRFToken', csrfToken);
            }
            else {
                console.error('CSRF token not found in cookies.');
            }
            console.log(url);
            const payload = JSON.stringify({ pk: pk, username: userInput });
            xhr.send(payload);
            xhr.onreadystatechange = function () {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        const response = JSON.parse(xhr.responseText);
                        console.log('Response gotten');
                        if (response.status == 'Error') {
                            alert("User not found");
                        }
                    }
                    else {
                        const errorData = JSON.parse(xhr.responseText);
                        console.error(errorData);
                    }
                }
            };
        }
        else {
            console.log('User canceled action.');
        }
    }
    else {
        console.log('User canceled input.');
    }
}
document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('share');
    if (button) {
        button.addEventListener('click', () => {
            const url = `share/${pk}`;
            showDialog(url);
        });
    }
});
