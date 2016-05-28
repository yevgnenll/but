(function(){
    $(document).ready(function(){

        var send_email = $('#send_email_btn');
        var send_email_url = send_email.data('submit-url');
        var accept_id = send_email.data('acceptid');

        send_email.click(function(){
            console.log(accept_id);
            $.ajax({
                url: send_email_url,
                method: "POST",
                data: {
                    'title': $('#title').val(),
                    'content': $('#email_content').val(),
                    'user_id': accept_id,
                }
            }).success(function(result){

            });
        });
    });
})();
