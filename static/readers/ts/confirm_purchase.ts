document.addEventListener('DOMContentLoaded', () => {
    console.log('DOMContentLoaded evento activado');
    const button = document.getElementById('myButton');
  
    if (button) {
      button.addEventListener('click', () => {
        // Utiliza la función `confirm` para mostrar un cuadro de confirmación
        const confirmacion = confirm('¿Desea confirmar la acción?');
  
        if (confirmacion) {
          // El usuario confirmó, realiza la acción
          alert('Acción confirmada');
          // Aquí puedes agregar la lógica para realizar la acción deseada
        } else {
          // El usuario canceló, no se realiza la acción
          alert('Acción cancelada');
        }
      });
    }
  });