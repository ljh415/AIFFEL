alert('Start!');
button = document.querySelector('button');
function alertClick() {
	alert('Click!');
};
button.onclick = alertClick;
