(function(){
    $(document).ready(function(){

        var phone_number = $('#phone_number');
        var send_button = $('#send_cert_num');
        send_button.click(function(){
            $.ajax({
                url: send_button.data('phone-check'),
                method: "POST",
                data: "phone_number="+phone_number.val()
            }).success(function(data){
            });
        });
    });
})();
