"use strict";
var pk;
document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('myButton');
    if (button) {
        button.addEventListener('click', () => {
            // Utiliza la función `confirm` para mostrar un cuadro de confirmación
            const confirmacion = confirm('Confirm action');
            const url = `buy/${pk}`;
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
                const payload = JSON.stringify({ pk: pk });
                xhr.send(payload);
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE) {
                        if (xhr.status === 200) {
                            console.log('Response gotten');
                        }
                        else {
                            console.error('Error:', xhr.status);
                        }
                    }
                };
            }
            else {
                // El usuario canceló, no se realiza la acción
                alert('Canceled action');
            }
        });
    }
});
