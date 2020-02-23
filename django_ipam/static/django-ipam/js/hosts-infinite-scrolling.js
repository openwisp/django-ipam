/*browser:true */
/*globals onUpdate*/

function initHostsInfiniteScroll($, current_subnet, address_add_url) {
    "use strict";
    var renderedPages = 5,
        fetchedPages = [],
        busy = false,
        nextPageUrl = "/api/v1/subnet/" + current_subnet + "/hosts",
        lastRenderedPage = 0; //1 based indexing (0 -> no page rendered)
    function addressListItem(addr) {
        if (addr.used) {
            return '<li> <a class="used">' + addr.address + ' </a> </li>';
        }
        return '<li> <a href=\"{% url ipaddress_add_url %}?_to_field=id&amp;_popup=1&amp;ip_address=' +
            addr.address + '&amp;subnet=' + current_subnet + '"onclick="return showAddAnotherPopup(this);\">' +
            addr.address + '</a> </li>';
    }
    function pageContainer(page) {
        var div = $("<div class=\"page\"></div>");
        page.forEach(function (address) {
            div.append(addressListItem(address));
        });
        return div;
    }
    function appendPage() {
        $('.subnet-visual').append(pageContainer(fetchedPages[lastRenderedPage]));
        if (lastRenderedPage >= renderedPages) {
            var removedDiv = $('.subnet-visual div:first');
            $('.subnet-visual').scrollTop($('.subnet-visual').scrollTop() - removedDiv.height());
            removedDiv.remove();
        }
        lastRenderedPage += 1;
        busy = false;
        onUpdate();
    }
    function fetchNextPage() {
        $.ajax({
            type: 'GET',
            url: nextPageUrl,
            success: function (res) {
                fetchedPages.push(res.results);
                nextPageUrl = res.next;
                console.log(nextPageUrl);
                appendPage();
            },
            error: function (error) {
                busy = false;
                throw error;
            },
        });
    }
    function pageDown() {
        busy = true;
        if (fetchedPages.length > lastRenderedPage) {
            appendPage();
        } else if (nextPageUrl !== null) {
            fetchNextPage();
        } else {
            busy = false;
        }
    }
    function pageUp() {
        busy = true;
        if (lastRenderedPage > renderedPages) {
            $('.subnet-visual div:last').remove();
            var addedDiv = pageContainer(fetchedPages[lastRenderedPage - renderedPages - 1]);
            $('.subnet-visual').prepend(addedDiv);
            $('.subnet-visual').scrollTop($('.subnet-visual').scrollTop() + addedDiv.height());
            lastRenderedPage -= 1;
        }
        busy = false;
    }
    function onUpdate() {
        if (!busy) {
            var scrollTop = $('.subnet-visual').scrollTop(),
                scrollBottom = scrollTop + $('.subnet-visual').innerHeight(),
                height = $('.subnet-visual')[0].scrollHeight;
            if (height * 0.75 <= scrollBottom) {
                pageDown();
            } else if (height * 0.25 >= scrollTop) {
                pageUp();
            }
        }
    }
    $('.subnet-visual').scroll(onUpdate);
    onUpdate();
}
