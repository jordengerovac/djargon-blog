const title_field = document.querySelector('input[name=title]');
const url_field = document.querySelector('input[name=url]');

const create_url = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-') // replace & with and
        .replace(/[\s\W-]+/g, '-') // replaces spaces, non-word characters and dashes with single dash
};

title_field.addEventListener('keyup', (e) => {
    url_field.setAttribute('value', create_url(title_field.value))
});