$(document).ready(function () {
    $("#logout").click(function() {
        $.post("/logout/",
            {
                action: "logout"
            },
            function(data, status){
                if(data[0].success == true) {
                    window.location.href = "http://localhost:8000/";
                }
        });
    });
})