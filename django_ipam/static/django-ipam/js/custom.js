/*jslint browser:true */

function dismissAddAnotherPopup(win) {
    "use strict";
    win.close();
    window.location.reload();
}

django.jQuery(function ($) {
    "use strict";
    $('#jstree').on("ready.jstree", function (e, data) {
        // A trick to open the tree automatically
        // till the point of the current node only.
        $('#jstree').jstree(true).select_node(window.current_subnet);
        $('#jstree').jstree(true).deselect_node(window.current_subnet);
    });
    $('#jstree').jstree().bind("activate_node.jstree", function (e, data) {
        // Open the specific subnet page that used clicked on.
        document.location.href = data.node.a_attr.href;
    });
});
