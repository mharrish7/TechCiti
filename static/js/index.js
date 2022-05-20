

$('.login').on('submit',function(ev){
    var e = $('.einp').val();
    var p = $('.pinp').val();
    
    $.ajax({
        url : '/log',
        data: {et : e,
                pt : p},
        type: 'POST'
    }).done(function(data){
        if(data['login']){
            console.log('success');
            $(location).prop('href', '/home')
        }
        else{
            $('.inc').text("Incorrect username or password");
        }
    });

    ev.preventDefault();
})

$('.register').on('submit',function(ev){
    var e = $('.re').val();
    var p = $('.rp').val();
    var cp = $('.rpc').val();
    $.ajax({
        url : '/reg',
        data: {ret : e,
            rpt : p,
            rcpt : cp},
        type: 'POST'
    }).done(function(data){
        $(".rinfo").text(data['info']);
    });

    ev.preventDefault();
})
