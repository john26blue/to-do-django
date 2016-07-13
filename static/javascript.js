// Show finished to-do toggle button
$('#showFinished').on('click', function() {
    $(".finished").toggle();
    $(this).button('Hide finished');
})

// Multiple to-dos delete button
var itemCount = 0,
    itemList = new Array();

// GET link for delete view
function getDeleteLink(list) {
    var deleteLink = '?';
    for (i = 0; i < list.length; i++) {
        if (i != 0) deleteLink += '&';
        deleteLink += 'item=' + list[i]; 
    }
    return deleteLink;
}

$('input[type="checkbox"]').on('click', function() {
    var checked = $(this).prop('checked'),
        button = $("#deleteBtn"),
        pk = $(this).attr('primary-key');
        
    if (checked === true) { // Select an item
        itemCount++;
        itemList.push(pk);
        $('#uncheckBtn').show();
        if (itemCount === 1) { // Button is currently disabled. Activate single delete button
            button.removeClass('disabled');
            button.attr('href', '/delete/' + pk);
        } else { // Button is currently activated. Add more item for deleting
            button.addClass('multipleBtn');
            button.attr('href', '/mdelete/' + getDeleteLink(itemList));
        }
    } else { // Uncheck an item
        itemCount--;
        itemList = $.grep(itemList, function(n, i) {
            return n !== pk;
        })
        if (button.hasClass('multipleBtn') === true) { // If currently checking multiple items
            // Back to single delete button if there's only one checked left
            if (itemCount === 1) {
                button.removeClass('multipleBtn');
                button.attr('href', '/delete/' + itemList[0]);
            } else 
                button.attr('href', '/mdelete/' + getDeleteLink(itemList));
        } else {

            // No checked item left
            button.addClass('disabled');
            $('#uncheckBtn').hide();
        }
    }
    console.log(itemList + getDeleteLink(itemList))
})

// Uncheck all button
$('#uncheckBtn').on('click', function() {
    $('input[type="checkbox"]').prop('checked', false);
    $('#deleteBtn').addClass('disabled').attr('href', '#');
    $(this).hide();
    itemCount = 0;
})