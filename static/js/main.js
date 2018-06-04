$(document).ready(function() {

    // index page animations
    $(".intro-1").hide(0).fadeIn(4000);
    $(".intro-2").hide(0).delay(1000).show("slow");
    $(".intro-3").hide(0).delay(2000).show("slow");
    $(".intro-4").hide(0).delay(3000).show("slow");
    $(".home-btn").hide(0).delay(4000).show("slow");

    // toggle featureticket report details
    $(".toggle").hide()
    $(".toggle-button").click(function() {
        $(".toggle").slideToggle("slow");
    });

    $(".toggle2").hide()
    $(".toggle-button2").click(function() {
        $(".toggle2").slideToggle("slow");
    });

    // hover effects

    
    // profile slide effects
    
    
    // dropdown menu
    $('.dropdown').on('show.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
    });

  // Add slideUp animation to Bootstrap dropdown when collapsing.
    $('.dropdown').on('hide.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
    });

});
