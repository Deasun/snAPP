$(document).ready(function(){

// index page animations
$(".intro-1").hide(0).delay(500).show("fast");
$(".intro-2").hide(0).delay(2500).show("fast");
$(".intro-3").hide(0).delay(3500).show("fast");
$(".intro-4").hide(0).delay(4500).show("fast");
$(".home-btn").hide(0).delay(6000).show("slow");


$(".toggle").hide()
$( ".toggle-button" ).click(function() {
  $( ".toggle" ).slideToggle( "slow" );
});

$(".toggle2").hide()
$( ".toggle-button2" ).click(function() {
  $( ".toggle2" ).slideToggle( "slow" );
});

});





