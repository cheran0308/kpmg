$(document).ready(function(){
    $(document).on('click', '#log', function() {
        var id = $(this).attr('bid');
        console.log(id);
        $.post("/get_wf_log/",
            {
                id:id
            },
            function(data, status){
                if(data[0].success == true) {
                    element = $('#logData');
                    console.log(data[0].data);
                    element.empty();
                    for(var i=0; i<data[0].data.length; i++){
                        var p = "<div class='row'><div class='col'>"+data[0].data[i].date+"</div><div class='col'>"+data[0].data[i].activity+"</div></div>";
                        element.append(p);
                    }
                }
        });
    });  
});