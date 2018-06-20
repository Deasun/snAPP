$(document).ready(function() {

    /*index page animations*/
    $(".intro-2").hide(0).delay(2000).show(0);
    $(".intro-3").hide(0).delay(4000).show(0);
    $(".intro-4").hide(0).delay(6000).show(0);
    $(".intro-1").hide(0).fadeIn(8000);
    $(".home-btn-1").hide(0).delay(8000).show(0);

    /*Index page tooltips*/
    $('[data-toggle="tooltip"]').tooltip()

    /*toggle featureticket report details*/
    $(".toggle").hide()
    $(".toggle-button").click(function() {
        $(".toggle").slideToggle("slow");
    });
    $(".toggle2").hide()
    $(".toggle-button2").click(function() {
        $(".toggle2").slideToggle("slow");
    });

    /*profile tabs*/
    $(".nav-tabs a").click(function() {
        $(this).tab('show');
    });

    /*dropdown menu*/
    $('.dropdown').on('show.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
    });

    /*Add slideUp animation to Bootstrap dropdown when collapsing.*/
    $('.dropdown').on('hide.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
    });

    /*Hover over tabs and icons*/
    $('.tab-pane, .fa-info-circle')
        .mouseenter(function() {
            $(this).animate({ "opacity": "1" }, 250)
        })
        .mouseleave(function() {
            $(this).animate({ "opacity": ".7" }, 250)
        });

    /*Turn message off after 10 secs*/
    setTimeout(function() {
        $('.message-fade').fadeOut('slow');
    }, 10000);

    /*Delete message*/
    $('.delete-message').on('click', function() {
        $('.delete-message').parent().attr('style', 'display:none;');
    })

    /*
    Marquee plug-in for scrolling member alerts - 
    https://www.jqueryscript.net/animation/Text-Scrolling-Plugin-for-jQuery-Marquee.html
    */
    $('.marquee').marquee({
        allowCss3Support: true,
        css3easing: 'linear',
        easing: 'linear',
        delayBeforeStart: 300,
        direction: 'left',
        duplicated: true,
        duration: 20000,
        gap: 150,
        pauseOnHover: true,
        startVisible: true,
    })
});
