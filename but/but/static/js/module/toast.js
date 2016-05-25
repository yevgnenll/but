(function(){
    $(document).ready(function(){
        var messages = $("body#body").data("messages").split(";");
        var tags = $("body#body").data("message-tags").split(";");

        for (var i=0; i<messages.length-1; i++){
            toastr.info(messages);
        }
    });
})();
