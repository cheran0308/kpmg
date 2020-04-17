$(document).ready(function () {
    $("#submitit").click(function() {
        console.log("helldsao")
        var name = $("#name").val();
        var desc = $("#desc").val();
        var approver = $("#approver").val();
        $.post("/add_new/",
            {
                name: name,
                desc: desc,
                approver: approver
            },
            function(data, status){
                console.log(data[0].success)
                if(data[0].success == true) {
                  window.location.href = "http://localhost:8000/created/";
                }
        });
    });
})