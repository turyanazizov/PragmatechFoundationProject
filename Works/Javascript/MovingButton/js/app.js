let mainButton = document.querySelector('.button');
let poslr = 200;
let postb = 200;

function left() {
    if (poslr != 0) {
        poslr -= 50;
        mainButton.style.left = `${poslr}px`;

    }

}

function right() {
    if (poslr != 400) {
        poslr += 50;
        mainButton.style.left = `${poslr}px`;
    }

}

function up() {
    if (postb != 0) {
        postb -= 50;
        mainButton.style.top = `${postb}px`;
    }

}

function bottom() {
    if (postb != 400)
        postb += 50;
    mainButton.style.top = `${postb}px`;
}