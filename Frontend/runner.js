let Layout;
let result = [64];
//Gets Layout
function fetchChessLayout(callback) {
    fetch('Layout.json')
      .then(response => response.json())
      .then(data => {
        Layout = data.imgs;
        callback();
      })
      .catch(error => console.error('Error fetching JSON:', error));
}
function assignImagesToSquares() {
    const squares = document.querySelectorAll('.square');   
    //2D array -> 1D array
    let i = 0
    for (let row = 0; row < Layout.length; row++) {
        for (let col = 0; col < Layout[row].length; col++) {
            if(Layout[row][col]){
                result[i] = (Layout[row][col]);
                i++;
            }
        }
    }
    //Layout onto Squares
    squares.forEach((square, index) => {
        piece = result[index]
        if (piece !== '-') {
            const img = document.createElement('img');
            img.src = `./images/${piece}.png`;
            img.alt = '';
            square.appendChild(img)
        }
        
    });
}
document.addEventListener('DOMContentLoaded', () => {fetchChessLayout(assignImagesToSquares);});
