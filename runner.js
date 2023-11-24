// JavaScript function to assign images to squares
function assignImagesToSquares() {
    const squares = document.querySelectorAll('.main-container .square');
    const initialLayout = [
        'BR', 'BP', '', '', '', '', 'WP', 'WR',
        'BN', 'BP', '', '', '', '', 'WP', 'WN',
        'BB', 'BP', '', '', '', '', 'WP', 'WB',
        'BQ', 'BP', '', '', '', '', 'WP', 'WQ',
        'BK', 'BP', '', '', '', '', 'WP', 'WK',
        'BB', 'BP', '', '', '', '', 'WP', 'WB',
        'BN', 'BP', '', '', '', '', 'WP', 'WN',
        'BR', 'BP', '', '', '', '', 'WP', 'WR'
    ];

    const pieceImages = [
        './images/BR.png', './images/BN.png', './images/BB.png', './images/BQ.png',
        './images/BK.png', './images/BP.png', './images/WR.png', './images/WN.png',
        './images/WB.png', './images/WQ.png', './images/WK.png', './images/WP.png'
    ];
    
    // Assign images based on initialLayout array
    squares.forEach((square, index) => {
        const piece = initialLayout[index];
        if (piece !== '') {
            const img = document.createElement('img');
            img.src = `./images/${piece}.png`;
            img.alt = '';
            square.appendChild(img);
        }
    });
}


// Run the function when the content is loaded
document.addEventListener('DOMContentLoaded', assignImagesToSquares);
