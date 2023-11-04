// JavaScript code to toggle the selected state of boxes
const boxes = document.querySelectorAll('.choice');
const startButton = document.getElementById('startButton');

boxes.forEach((box) => {
    box.addEventListener('click', () => {
    box.classList.toggle('selected');
    });
});

startButton.addEventListener('click', () => {
    const selectedBoxes = document.querySelectorAll('.selected');
    const selectedIDs = Array.from(selectedBoxes).map((box) => box.id);
    console.log('Selected Box IDs:', selectedIDs);
    // Do something with the selected box IDs, e.g., send them to the server.
});
