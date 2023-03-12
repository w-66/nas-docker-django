var editor = new Editor({
    el: document.querySelector('#editor'),
    height: 640,
    toolbar: [
        'bold', 'italic', 'heading', '|',
        'quote', 'code', 'table', 'link', 'image', '|',
        'undo', 'redo', 'preview', 'fullscreen'
    ]
});
editor.render();
