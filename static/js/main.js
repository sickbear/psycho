"use strict";

$(document).ready(function() {
    
    // Плагины
    $('.popup').magnificPopup();
    
    $('.popup-gallery').magnificPopup({
		delegate: 'a',
		type: 'image',
		gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0,1]
		}
	});
    
    $('.collapse').collapse();
    
});
