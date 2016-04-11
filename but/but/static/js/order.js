(function(){
    $(document).ready(function(){
        $('#order_button').click(function(){
            $('#order_form').submit();
        });

        $('#order_complete_button').click(function(){
            $('#order_complete_form').submit();
        });
    });
})();
