"use strict";

$(document).ready(function() {
    
    // Плагины
    $('.popup').magnificPopup();
    
    // Эффекты наведения в блоге
    $('.post').hover(
        function() {
            $(this).find('.post__title').addClass('activeBlock');
        }, function() {
            $( this ).find('.post__title').removeClass('activeBlock');
    });
    
});




$(this).find('.post__title').addClass('activeBlock');