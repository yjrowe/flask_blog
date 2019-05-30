/**
 * 添加评论
 * @param _this
 */
function submitComment(_this) {
    var data = $('#form').serializeArray();

    if (!$.trim(data[0]['value'])) {
        return alert('请填写用户名');
    }

    if (!$.trim(data[1]['value'])) {
        return alert('请填写评论');
    }

    $(_this).attr('disabled', 'disabled');
    
    $.ajax({
        type: 'post',
        url: '/comment',
        data: data,
        dataType: 'json',
        async: false,
        success: function (res) {
            if (!res.status) {
                return alert('评论失败');
            } else {
                window.location.reload()
            }
        }
    })
}