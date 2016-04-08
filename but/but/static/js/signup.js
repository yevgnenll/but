(function(){
    
    $(document).ready(function(){

        var my_pass = $('#firstpw');
        var check_pw = $('#secondpw');
        var chk_label = $('#checked');
        var signup = $('#signup');

        check_pw.keyup(function(){
            if (my_pass.val() === check_pw.val()) {
                chk_label.text('correct password').css('font-size', '20px').css('color', '#4CAF50');                
                signup.prop('disabled', false);
            } else {
                chk_label.text('invalid password').css('font-size', '20px').css('color','#b71c1c');
                signup.prop('disabled', true);
            }
        });
    });

})();
