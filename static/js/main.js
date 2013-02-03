// when the DOM loads
$(function() {
    // simple animation to fade in all but the top story
    var rowNum = 0;
    var dur = 0;
    $("tbody tr").each(function() { 
        // capture current row
        var elm = $(this); 
        if (rowNum === 0) { 
            dur += 500;
            rowNum++; 
            return; 
        } 
        // schedule it to fade in
        setTimeout(function() { 
            elm.fadeIn();
        }, dur); 
        dur += 500;
        rowNum++;
    });
});
