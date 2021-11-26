const modalElement = $('#images-modal');
const modalElementImage = $('#images-modal-image');
const modalElementCaption = $('#images-modal-caption');

$(function() {
    $('img.clickable').click(function() {
        modalElement.css("display", "block");
        modalElementImage.attr('src',this.src);
        modalElementCaption.text(this.alt);
    })
    $('#images-modal').click(function() {
        modalElement.css('display', 'none');
    })
    $('#images-modal-close').click(function() {
        modalElement.css('display', 'none');
    })
})