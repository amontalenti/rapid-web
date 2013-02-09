(function() {
    function animateRows() {
        // simple animation to fade in all but the top story
        var rowNum = 1;
        var dur = 500;
        $("tbody tr").each(function() { 
            if (rowNum === 0) { 
                // skip 1st row
                return; 
            } 
            // capture current row
            var elm = $(this); 
            // schedule it to fade in
            setTimeout(function() { 
                elm.fadeIn();
            }, dur); 
            dur += 500;
            rowNum += 1;
        });
    };

    RAPID.animateRows = animateRows;
})();
