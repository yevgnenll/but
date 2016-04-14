(function(){
    $(document).ready(function({

        var phone_number = $('#phone_number');
        $('#send_cert_num').click(function(){
            $.ajax({
                url: 
                method: "POST",
                data: "phone_number="+phone_number.val()
            }).success(function(data){
            });
        });
    });
})();
