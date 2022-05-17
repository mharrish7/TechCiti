

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