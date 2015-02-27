var checkClaim = function(callback) {
    $.get("/api/robot/check", function(data) {
        if (data["claim"]) {
            // Robot is currently claimed
            if (confirm("The robot is currently claimed. Continue?")) {
                callback();
            }
            // otherwise, do nothing
        }
        else {
            // Robot is currently not claimed (or there was an error server-side)
            callback();
        }
    });
}

$('robot-start-btn').click(function() {
    checkClaim(function() {
        $.post("/api/claim", {
            user: currentUser
        });
        $.post("/api/start");
    });
});

$('robot-stop-btn').click(function() {
    checkClaim(function() {
        $.post("/api/stop");
    });
});