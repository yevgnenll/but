(function(){
    $(document).ready(function(){
        $('#order_button').click(function(){
            $('#order_form').submit();
        });

        $('#order_complete_button').click(function(){
            if($('#dest_address').val()==='' || $('#dest_address').val() === null){
                alert('배송지를 입력해주세요');
                return false;
            }
            $('#order_complete_form').submit();
        });
    });
})();
