$(function () {
	let bannerElement = `
	<div class="page-banner-container">
	<div class="banner-image-container">
		<button class="banner-close-button" id="banner-close" aria-label="Close banner" type="button" data-close>
    		<span aria-hidden="true">&times;</span>
  		</button>
		<a class="page-banner-image" href="https://zrzutka.pl/85uckm" target="_blank" title="Oficjalna zrzutka MOM 2022"></a>
	</div>
	</div<
	`
	$('body').append(bannerElement);
	$('#banner-close').on('click', () => {
		$('.page-banner-container').css('display', 'none')
	})
})