"use strict";

$(document).ready(function() {

    // Выпадающее меню
    $('.nav > li').hover(function() {
        $(this).find('.subnav').show(200);
    }, function() {
        $(this).find('.subnav').hide(400);
    });
    
    // Мобильное меню
    $('#nav-btn').click(function() {
        $(this).toggleClass('fa-bars fa-times');
        $('.navigation .nav').slideToggle();
    });
    $(window).resize(function() {
        let width = $(this).width();
        if (width > 992) {
            $('.navigation .nav').show();
        } else {
            $('.navigation .nav').hide();
        }
        $('#nav-btn').removeClass('fa-times').addClass('fa-bars');
    })
    
    // Подсказка в форме
    $('#offer input[name="phone"]').on({
        focusin: function() {
            $('#offer .tip').show(200);
        },
        focusout: function() {
            $('#offer .tip').hide(400);
        }
    });
    
    // Маска телефона
    $(function($) {
       $('input[name=phone]').mask('+7 (999) 999-9999');
    });
    
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
