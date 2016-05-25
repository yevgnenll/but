(function(){
    $(document).ready(function(){

        var order_button = $('#order_button');

        order_button.click(function(){
            var stock = Number(order_button.data('rest-stock'));
            var buy_count = Number($('#buy_count').val());

            if(stock < buy_count){
                alert('재고가 ' + (buy_count - stock) + '개 부족합니다');
                return false; 
            }

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
