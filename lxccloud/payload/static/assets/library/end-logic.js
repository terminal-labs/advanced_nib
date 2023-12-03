var pending_build_cluster_name = "";

function update_dom_cluster_spec_widget(data) {
    var text = data['cluster']['text'];
    pending_build_cluster_name = text = data['cluster']['name'];
    $("#target_cluster_spec").html(text);
    $("#target_widget_cp_divider_a").show();
    $("#target_main_cluster_info").show();
}

function pass_callback(data) {

}

function alert_callback(data) {
    alert(JSON.stringify(data));
}

function console_log_callback(data) {
    console.log(JSON.stringify(data));
}

function anyactivebuilds(data) {
    post_json(origin + "/js-api/v1.0/post/anyactivebuilds", {
        "cmd": "pass"
    }, console_log_callback);
}

function page_create_cluster() {
    start_polling_service('anyactivebuilds', anyactivebuilds, 1);
    $('.target_more_info').click(function() {
        var ele_id = this.id;
        post_json(origin + "/js-api/v1.0/post/generalclusterinfo", {
            "name": ele_id
        }, update_dom_cluster_spec_widget);
    });
}

$(document).ready(function() {
    if (pathname == "/create-cluster") {}

    var
        $headers = $('body > h3'),
        $header = $headers.first(),
        ignoreScroll = false,
        timer;
    $('.top.menu .item').tab();

    $("#mymodalg").click(function() {
        $('.ui.modal').modal('show');
    });

    $("#build-now").click(function() {
        post_json(origin + "/js-api/v1.0/post/createcluster", {
            "name": pending_build_cluster_name
        }, pass_callback);
    });

    // Preserve example in viewport when resizing browser
    $(window)
        .on('resize', function() {
            // ignore callbacks from scroll change
            clearTimeout(timer);
            $headers.visibility('disable callbacks');

            // preserve position
            $(document).scrollTop($header.offset().top);

            // allow callbacks in 500ms
            timer = setTimeout(function() {
                $headers.visibility('enable callbacks');
            }, 500);
        });
    $headers
        .visibility({
            // fire once each time passed
            once: false,

            // don't refresh position on resize
            checkOnRefresh: true,

            // lock to this element on resize
            onTopPassed: function() {
                $header = $(this);
            },
            onTopPassedReverse: function() {
                $header = $(this);
            }
        });
});