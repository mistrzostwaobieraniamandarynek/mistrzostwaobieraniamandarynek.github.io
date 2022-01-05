$(function () {
	let bannerElement = `
	<div class="page-banner-container">
	<div class="banner-image-container">
		<button class="banner-close-button" id="banner-close" aria-label="Close banner" type="button" data-close>
    		<svg xmlns="http://www.w3.org/2000/svg" width="9mm" height="9mm" version="1.1" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd" viewBox="0 0 9144 9144"> <defs> <style type="text/css">  .fil0 {fill:transparent} .fil1 {fill:#ffffff;fill-rule:nonzero}  </style> </defs> <g id="Layer_x0020_1"> <metadata id="CorelCorpID_0Corel-Layer"/> <g id="_2744712244800"> <polygon class="fil0" points="0,0 9144,0 9144,9144 0,9144 "/> <path class="fil1" d="M3568 3692c-35,-34 -35,-90 0,-124 34,-35 90,-35 124,0l880 879 880 -879c34,-35 90,-35 124,0 35,34 35,90 0,124l-879 880 879 880c35,34 35,90 0,124 -34,35 -90,35 -124,0l-880 -879 -880 879c-34,35 -90,35 -124,0 -35,-34 -35,-90 0,-124l879 -880 -879 -880zm3033 880c0,-560 -227,-1067 -594,-1435 -368,-367 -875,-594 -1435,-594 -560,0 -1067,227 -1435,594 -367,368 -594,875 -594,1435 0,560 227,1067 594,1435 368,367 875,594 1435,594 560,0 1067,-227 1435,-594 367,-368 594,-875 594,-1435zm-470 -1559c399,399 646,950 646,1559 0,609 -247,1160 -646,1559 -399,399 -950,646 -1559,646 -609,0 -1160,-247 -1559,-646 -399,-399 -646,-950 -646,-1559 0,-609 247,-1160 646,-1559 399,-399 950,-646 1559,-646 609,0 1160,247 1559,646z"/> </g> </g> </svg>
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