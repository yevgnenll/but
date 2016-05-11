(function(){
    $(document).ready(function(){
        var phone_number = $('#phone_number');
        var send_button = $('#send_cert_num');

        var certificate_button = $('#cert_num_check');
        
        send_button.click(function(){
            $.ajax({
                url: send_button.data('phone-check'),
                method: "POST",
                // data: "phone_number="+phone_number.val()
                data: { "phone_number": phone_number.val()}
            }).success(function(data){
            });
        });

        certificate_button.click(function(){
            $.ajax({
                url: certificate_button.data('phone-cert'),
                method: "POST",
                data: "cert_number=" + $('#cert_number').val()
            }).success(function(data){
                location.reload();
            });
        });
    });
})();
