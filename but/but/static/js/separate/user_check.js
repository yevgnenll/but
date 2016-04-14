(function(){
    
    $(document).ready(function(){
        var username = $('#user_id');
        var id_check_url = $('#user_id').data('user-check');
        var signup = $('#signup');

        function invalid_data(signup_btn){
            $('#id_input').text('이미 사용중인 ID입니다').css('font-size', '20px').css('color','#b71c1c');
            signup_btn.prop('disabled', true);
            // signup_btn.addClass('disabled');
        }

        function init_input(){
            $('#id_input').text('5자 이상의 사용하실 아이디를 입력해주세요').css('font-size', '1rem').css('color','#bdbdbd');
        }

        username.keyup(function(){
            if (username.val().length>4){
                $.ajax({

                    url: id_check_url,
                    method: "POST",
                    data: "username="+username.val()

                }).success(function(result_value){

                    if(result_value.status === '403'){
                        invalid_data(signup);
                    } else if(result_value.status === '200') {
                        $('#id_input').text('사용 가능한 ID입니다').css('font-size', '20px').css('color','#4CAF50');
                        signup.removeClass('disabled');
                    } 

                }).error(function(result_value){
                    init_input();
                });
            } else if(username.val().length>0 && username.val().length<=4) {
                $('#id_input').text('사용하실 아이디를 입력해주세요').css('font-size', '0.8rem').css('color','#00acc1');
            } else {
                init_input();
            }
        });
    });

    $(document).ready(function(){
        var email = $('#user_email');
        var email_check_url = $('#user_email').data('email-check');
        var signup = $('#signup');

        function init_email(){
            $('#email_input').text('사용하실 e-mail을 입력해주세요.').css('font-size', '1rem').css('color','#bdbdbd');
        }

        function invalid(signup_btn){
            $('#email_input').text('이미 사용중인 e-mail입니다 다시 확인해주세요').css('font-size', '20px').css('color','#b71c1c');
            signup_btn.prop('disabled', true);
            // signup_btn.addClass('disabled');
        }

        email.keyup(function(){
            if( email.val().indexOf('@')>0 && email.val().indexOf('.')>0){
                $.ajax({
                    url: email_check_url,
                    method: "POST",
                    data: "email="+email.val()
                }).success(function(result_value){
                    if(result_value.status == '403'){
                        invalid(signup);
                    } else if(result_value.status == '200'){
                        $('#email_input').text('사용 가능한 e-mail입니다').css('font-size', '20px').css('color','#4CAF50');
                    } 
                });
            } else if(email.val().indexOf('@')<0 || email.val().indexOf('.')<0) {
                $('#email_input').text('e-mail').css('font-size', '0.8rem').css('color','#00acc1');
            } else {
                init_email();
            }
        });

});        
})();
