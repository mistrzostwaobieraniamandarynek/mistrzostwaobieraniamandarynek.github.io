$(function () {
    console.log("Hello")
    $('.article-content').each(function() {
        limitArticleLines($(this), 4);
    })
})
function limitArticleLines(articleContent, lineLimit)
{
    let maxHeight = parseInt(articleContent.css('line-height')) * lineLimit;
    while(articleContent.height() > maxHeight) {
        let text = articleContent.text();
        articleContent.text(text.substring(0,text.length-10)).text(articleContent.text()+'(...)');
    }
}
