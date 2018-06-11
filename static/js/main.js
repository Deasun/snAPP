$(document).ready(function() {

    /*index page animations*/
    $(".intro-1").hide(0).fadeIn(6000);
    $(".intro-2").hide(0).delay(1000).show(0);
    $(".intro-3").hide(0).delay(2000).show(0);
    $(".intro-4").hide(0).delay(3000).show(0);
    $(".home-btn").hide(0).delay(4000).show(0);

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
    $('.tab-pane, i, .stick-head')
        .mouseenter(function() {
            $(this).css({ "opacity": ".7" })
        })
        .mouseleave(function() {
            $(this).css({ "opacity": "1" })
        });

    /*Reduce size/pinch on click*/
    $('i').click(function() {
        $(this).animate({opacity: "1"}, 500)
    })
});

