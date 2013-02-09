(function() {
    function hackernewsFetch(afterFetch) {
        var apiroot = "http://hndroidapi.appspot.com";
        var path = "/best/format/json/page/";
        var params = "?appid=RAPID&callback=?";
        var url = [apiroot, path, params].join("");

        $.getJSON(url, function(data) {
            var rows = $("table tr");
            $.each(data.items, function(i, item) {
                var row = rows.get(i+1);
                if (typeof row !== "undefined") {
                    row = $(row);
                    var score = row.find("span.label:first");
                    var pubdate = row.find("span.label:last");
                    var link = row.find("a");
                    link.attr("href", item.url);
                    link.html(item.title);
                    score.html(item.score.replace(" points", ""));
                    pubdate.html(item.time);
                }
            });
        });
   }; 

   RAPID.hackernewsFetch = hackernewsFetch;
})();
