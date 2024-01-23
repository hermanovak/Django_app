submitB = document.getElementById("submit");

submitB.addEventListener("click", function(){
    $(function() {
        $.ajax({
            type: 'POST',
            url:"/weekly",
            data: {csrfmiddlewaretoken: window.CSRF_TOKEN, tlacitko1: submitB.value},
            success:function(response){}});
    });
});