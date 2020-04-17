$(document).ready(function(){
    var id = 0;
    $(document).on('click', '#status', function(){
        self = $(this);
        self.empty()
        var option = "<select id='statuschange'><option value='created'>Created</option><option value='return'>Return</option><option value='rejected'>Reject</option><option value='approved'>Approve</option></select>";
        self.append(option);
        id = $(this).attr('bid');
    });

    $(document).on('change', '#statuschange', function() {
        var val = $(this).val();
        console.log(id);
        $.post("/update_status/",
            {
                val: val,
                id:id
            },
            function(data, status){
                if(data[0].success == true) {
                  window.location.href = "http://localhost:8000/approval/";
                }
        });
    })

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
})