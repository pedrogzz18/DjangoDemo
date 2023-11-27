/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./static/readers/ts/confirm_purchase.ts":
/*!***********************************************!*\
  !*** ./static/readers/ts/confirm_purchase.ts ***!
  \***********************************************/
/***/ (() => {

eval("\ndocument.addEventListener('DOMContentLoaded', () => {\n    console.log('DOMContentLoaded evento activado');\n    const button = document.getElementById('myButton');\n    if (button) {\n        button.addEventListener('click', () => {\n            // Utiliza la función `confirm` para mostrar un cuadro de confirmación\n            const confirmacion = confirm('¿Desea confirmar la acción?');\n            if (confirmacion) {\n                // El usuario confirmó, realiza la acción\n                alert('Acción confirmada');\n                // Aquí puedes agregar la lógica para realizar la acción deseada\n            }\n            else {\n                // El usuario canceló, no se realiza la acción\n                alert('Acción cancelada');\n            }\n        });\n    }\n});\n\n\n//# sourceURL=webpack:///./static/readers/ts/confirm_purchase.ts?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./static/readers/ts/confirm_purchase.ts"]();
/******/ 	
/******/ })()
;