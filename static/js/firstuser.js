(function() {
    function showFirstVisitDialog() {
        var cookie = RAPID.readCookie("visited");
        if (cookie === "true") {
            // do nothing, user has visited before
            return;
        }
        var modal = $("#first-visit-dialog");
        modal.on("hide", function() {
            RAPID.createCookie("visited", "true", 30);
        });
        modal.modal();
    };

    function clearFirstVisit() {
        RAPID.eraseCookie("visited");
    };

    RAPID.showFirstVisitDialog = showFirstVisitDialog;
    RAPID.clearFirstVisit = clearFirstVisit;
})();
