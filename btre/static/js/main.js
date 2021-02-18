const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


window.setTimeout(function(){
    $('#message').fadeOut('slow');
},3000);