(function(){
    $(document).ready(function(){

        var submit_btn = $('#comment_submit');

        submit_btn.click(function(){

            $.ajax({
                url: submit_btn.data('submit-url'),
                method: "POST",
                data: {
                    'content': $('#comment_data').val()
                }

            }).success(function(result_value){
                comment = result_value;

                var comment_list = $('#comment_list');
                var comment_ajax_url = comment_list.data('json-path');
                comment_list.append(
                    "<li class='collection-item avatar'>" +
                        "<img src='"+ comment.profile_image + "' alt='" + comment.username +"' class='circle'>" +
                        "<span class='title'>@"+ comment.username + "</span>" +
                        "<p>" + comment.content+ "</p>" +
                    '</li>'
                );

               $('#attach_comment').modal('hide');
            });
        });

    });
    $(document).ready(function(){

        var comment_list = $('#comment_list');
        var comment_ajax_url = comment_list.data('json-path');

        $.ajax({
            url: comment_ajax_url,
            method: "GET"
        }).success(function(result_value){

            if (result_value.length==0){
                comment_list.append(
                    "<li class='collection-item'>아직 댓글이 없습니다</li>"
                );
            } else {
                for(var i=0; i<result_value.length; i++){
                    var comment = result_value[i];

                    comment_list.append(
                        "<li class='collection-item avatar'>" +
                            "<img src='"+ comment.profile_image + "' alt='" + comment.username +"' class='circle'>" +
                            "<span class='title'>@"+ comment.username + "</span>" +
                            "<p>" + comment.content+ "</p>" +
                        '</li>'
                    );
                }
            }
        });
    });

})();
