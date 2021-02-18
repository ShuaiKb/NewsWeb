$(function () {
    pageInit.setWidth();
    pageInit.setSidebar();
})
$(window).resize(function () {
    pageInit.setWidth();
})

/*
 * init page when page load
 */
var pageInit = (function (page) {
    page.setWidth = function () {
        if ($(window).width() < 768) {
            $(".sidebar").css({ left: -220 });
            $(".main-wrap").css({ marginLeft: 0 });
        } else {
            $(".sidebar").css({ left: 0 });
            $(".main-wrap").css({ marginLeft: 220 });
        }
    };
    page.setSidebar = function(){
        $('[data-target="sidebar"]').click(function(){
            var asideLeft = $(".sidebar").offset().left;
            if (asideLeft == 0) {
                $(".sidebar").animate({ left: -220 });
                $(".main-wrap").animate({ marginLeft: 0 });
            }
            else {
                $(".sidebar").animate({ left: 0 });
                $(".main-wrap").animate({ marginLeft: 220 });
            }
        });

        $(".has-sub>a").click(function () {
            $(this).parent().siblings().find(".sub-menu").slideUp();
            $(this).parent().find(".sub-menu").slideToggle();
        })
    }
    return page;
})(window.pageInit || {});
