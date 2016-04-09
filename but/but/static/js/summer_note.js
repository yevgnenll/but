(function(){
    $(document).ready(function(){

        $('#summernote').summernote({
            lang: 'ko-KR',
            height: 500,
            minHeight: 500,
            maxHeight: null,
            focus: true
        });

        $('.submit_note').click(function(){
            var summernote_content = $('#summernote').summernote('code');
            $('.text-note').val(summernote_content);
            $('.form-note').submit();
        });

    });
})();
