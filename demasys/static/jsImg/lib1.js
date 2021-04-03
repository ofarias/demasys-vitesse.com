function isMobile() {
    var e = navigator.userAgent.toLowerCase();
    if (Modernizr.touch || e.match(/(iphone|ipod|ipad)/) || e.match(/(android)/) || e.match(/(iemobile)/) || e.match(/iphone/i) || e.match(/ipad/i) || e.match(/ipod/i) || e.match(/blackberry/i) || e.match(/bada/i) || e.match(/windows phone/i) || e.match(/webOS/i)) {
        return true
    } else {
        return false
    }
}

function getWidthBrowser() {
    var e;
    if (typeof window.innerWidth == "number") {
        e = window.innerWidth
    } else if (document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)) {
        e = document.documentElement.clientWidth
    } else if (document.body && (document.body.clientWidth || document.body.clientHeight)) {
        e = document.body.clientWidth
    }
    return e
}

function getHeightBrowser() {
    var e;
    if (typeof window.innerHeight == "number") {
        e = window.innerHeight
    } else if (document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)) {
        e = document.documentElement.clientHeight
    } else if (document.body && (document.body.clientWidth || document.body.clientHeight)) {
        e = document.body.clientHeight
    }
    return e
}

function goToPage() {
    $(".action_page").click(function(e) {
        var t = $(this).parent(),
            n = $(".go_page", t).val();
        Shopify.queryParams.page = n;
        location.search = $.param(Shopify.queryParams)
    });
    $(".go_page").on("keypress", function(e) {
        if (e.which == "13") {
            var t = $(this).val();
            Shopify.queryParams.page = t;
            location.search = $.param(Shopify.queryParams)
        }
    })
}

function handleDataAnimate() {
    if (touch == false) {
        $(".animated").each(function() {
            var e = $(this);
            var t = $(this).attr("data-animation-delay");
            var n = 0;
            if (t) {
                n = Number(t)
            } else {
                n = 200
            }
            if (!e.hasClass("visible")) {
                var r = e.attr("data-animation");
                e.appear(function() {
                    setTimeout(function() {
                        e.addClass(r + " visible")
                    }, n)
                }, {
                    accX: 0,
                    accY: -30
                }, "easeInCubic")
            }
        })
    }
}

function handleFocus() {
    $(".form-focus input").focus(function() {
        $(this).parents(".form-focus").addClass("focus")
    }).blur(function() {
        $(this).parents(".form-focus").removeClass("focus")
    })
}

function handleBoxLogin() {
    $("#loginBox input").focus(function() {
        $(this).parents("#loginBox").addClass("focus")
    }).blur(function() {
        $(this).parents("#loginBox").removeClass("focus")
    })
}

function handleDropdown() {
    $(".dropdown-link").on("click", function() {
        if (touch == false && getWidthBrowser() > 980) {
            var e = $(this).attr("href");
            window.location = e
        }
    });
    handleBoxLogin();
    handleFocus()
}

function handleScrollToTop() {
    function e(e) {
        var t = $("#scroll-top");
        t.removeClass("off on");
        if (e == "on") {
            t.addClass("on")
        } else {
            t.addClass("off")
        }
    }
    $(window).scroll(function() {
        var t = $(this).scrollTop();
        var n = $(this).height();
        if (t > 0) {
            var r = t + n / 2
        } else {
            var r = 1
        }
        if (r < 1e3) {
            e("off")
        } else {
            e("on")
        }
    });
    $("#scroll-top").click(function(e) {
        e.preventDefault();
        $("html,body").animate({
            scrollTop: 0
        }, 800, "swing")
    })
}

function handleScreenshotPreview() {
    var e = 100;
    var t = 50;
    $(".screenshot").hover(function(n) {
        $("body").append("<p id='screenshot'><span></span><img src='" + $(this).attr("data-rel") + "' alt='' /></p>");
        if ($(this).hasClass("odd")) {
            $("#screenshot").css("top", n.pageY - e + "px").css("right", n.pageX + t + "px").fadeIn("fast")
        } else if ($(this).hasClass("even")) {
            $("#screenshot").css("top", n.pageY - e + "px").css("left", n.pageX + t + "px").fadeIn("fast")
        }
    }, function() {
        $("#screenshot").remove()
    });
    $(".screenshot").mousemove(function(n) {
        if ($(this).hasClass("odd")) {
            $("#screenshot").css("top", n.pageY - e + "px").css("right", n.pageX + t + "px")
        } else if ($(this).hasClass("even")) {
            $("#screenshot").css("top", n.pageY - e + "px").css("left", n.pageX + t + "px")
        }
    })
}

function alwaysRefreshZoom() {
    if (touch == false) {
        if (window.main_image_display == "zoom" || window.main_image_display == "both") {
            if ($(".elevatezoom").length) {
                var e = $(".elevatezoom .img-zoom");
                e.elevateZoom({
                    gallery: "gallery_main",
                    galleryActiveClass: "active",
                    zoomType: "window",
                    cursor: "pointer",
                    zoomWindowFadeIn: 300,
                    zoomWindowFadeOut: 300,
                    scrollZoom: false,
                    easing: true,
                    loadingIcon: window.loader_gif
                });
                if (window.main_image_display == "both") {
                    $(".elevatezoom .img-zoom").bind("click", function(e) {
                        var t = $(".elevatezoom .img-zoom").data("elevateZoom");
                        $.fancybox(t.getGalleryList(), {
                            closeBtn: false,
                            helpers: {
                                buttons: {}
                            }
                        });
                        return false
                    })
                }
            }
        }
    }
}

function handleImageThumbs() {
    if ($("#gallery_main").length) {
        if (touch) {
            $("#product-image .main-image").on("click", function() {
                var e = [];
                var t = 0;
                var n = $("#product-image .image-thumb");
                n.each(function(n, r) {
                    e.push({
                        href: r.href,
                        title: r.title
                    });
                    if ($(this).hasClass("active")) {
                        t = n
                    }
                });
                $.fancybox(e, {
                    closeBtn: false,
                    index: t,
                    openEffect: "none",
                    closeEffect: "none",
                    nextEffect: "none",
                    prevEffect: "none",
                    helpers: {
                        buttons: {}
                    }
                });
                return false
            })
        } else {
            if (window.main_image_display == "lightbox") {
                $("#product-image .fancybox").on(clickEv, function() {
                    var e = [];
                    var t = 0;
                    var n = $("#product-image .image-thumb");
                    n.each(function(n, r) {
                        e.push({
                            href: r.href,
                            title: r.title
                        });
                        if ($(this).hasClass("active")) {
                            t = n
                        }
                    });
                    $.fancybox(e, {
                        closeBtn: false,
                        index: t,
                        helpers: {
                            buttons: {}
                        }
                    });
                    return false
                })
            }
        }
        $("#product-image").on("click", ".image-thumb", function() {
            var e = $(this);
            if (!e.hasClass("active")) {
                var t = e.parents(".product-image-wrapper");
                var n = e.attr("data-image-zoom");
                var r = e.attr("data-image");
                t.find(".image-thumb").removeClass("active");
                e.addClass("active");
                t.find(".main-image").find("img").attr("data-zoom-image", n);
                t.find(".main-image").find("img").attr("src", r).load(function() {})
            }
            return false
        })
    }
}

function alwaysRefreshZoomQS() {
    if (touch == false) {
        if (window.main_image_display == "zoom" || window.main_image_display == "both") {
            if ($(".elevatezoom_qs").length) {
                var e = $(".elevatezoom_qs .img-zoom");
                e.elevateZoom({
                    gallery: "gallery_main_qs",
                    galleryActiveClass: "active",
                    zoomType: "window",
                    cursor: "pointer",
                    zoomWindowFadeIn: 300,
                    zoomWindowFadeOut: 300,
                    scrollZoom: false,
                    easing: true,
                    loadingIcon: window.loader_gif
                });
                if (window.main_image_display == "both") {
                    $(".elevatezoom_qs .img-zoom").bind("click", function(e) {
                        var t = $(".elevatezoom_qs .img-zoom").data("elevateZoom");
                        $.fancybox(t.getGalleryList(), {
                            closeBtn: false,
                            helpers: {
                                buttons: {}
                            }
                        });
                        return false
                    })
                }
            }
        }
    }
}

function alwaysScrollThumbsQS() {
    if ($("#gallery_main_qs").length) {
        $("#quick-shop-image").on(clickEv, ".image-thumb", function() {
            var e = $(this);
            var t = e.parents(".product-image-wrapper");
            var n = e.attr("data-image-zoom");
            var r = e.attr("data-image");
            t.find(".image-thumb").removeClass("active");
            e.addClass("active");
            t.find(".main-image").find("img").attr("data-zoom-image", n);
            t.find(".main-image").find("img").attr("src", r).load(function() {});
            return false
        })
    }
}

function handleTooltip() {
    if ($(".btooltip").length) {
        $(".btooltip").tooltip()
    }
}

function handleTabs() {
    $("body").on("click", ".nav-tabs a", function(e) {
        e.preventDefault();
        $(this).tab("show")
    })
}

function getRandomInt(e, t) {
    return Math.floor(Math.random() * (t - e + 1)) + e
}

function mockupCaptionVideo() {
    if ($("#home-video").length) {
        if (getWidthBrowser() < 1200) {
            var e = window.general_font_size;
            var t = window.video_heading_size;
            var n = window.video_caption_size;
            var r = getWidthBrowser();
            var i = t * r / 1200;
            var s = n * r / 1200;
            if (i < e) i = e;
            if (s < e) s = e;
            $("#home-video .video_caption").css({
                "font-size": s
            });
            $("#home-video .video_heading").css({
                "font-size": i
            })
        } else {
            var t = window.video_heading_size;
            var n = window.video_caption_size;
            $("#home-video .video_caption").css({
                "font-size": n
            });
            $("#home-video .video_heading").css({
                "font-size": t
            })
        }
        var o = $("#home-video").height() / 2;
        var u = $("#home-video .video_width").height();
        var a = o - u / 2;
        $("#home-video .video_width").css({
            top: a,
            opacity: 1
        })
    }
}

function mockupCaptionSlider() {
    if ($("#home-slider").length) {
        if (getWidthBrowser() < 1200) {
            var e = window.general_font_size;
            var t = window.slideshow_heading_size;
            var n = window.slideshow_caption_size;
            var r = getWidthBrowser();
            var i = t * r / 1200;
            var s = n * r / 1200;
            if (i < e) i = e;
            if (s < e) s = e;
            $("#home-slider .slide-body > .caption").css({
                "font-size": s
            });
            $("#home-slider .slide-body > .caption > h2").css({
                "font-size": i
            });
            $("#home-slider .cameraContent > .camera_caption").css({
                "font-size": s
            });
            $("#home-slider .cameraContent > .camera_caption .header").css({
                "font-size": i
            })
        } else {
            var t = window.slideshow_heading_size;
            var n = window.slideshow_caption_size;
            $("#home-slider .slide-body > .caption").css({
                "font-size": n
            });
            $("#home-slider .slide-body > .caption > h2").css({
                "font-size": t
            });
            $("#home-slider .cameraContent > .camera_caption").css({
                "font-size": n
            });
            $("#home-slider .cameraContent > .camera_caption .header").css({
                "font-size": t
            })
        }
        var o = $("#home-slider").height() / 2;
        $("#home-slider .slide-body > .caption").each(function() {
            var e = $(this).height();
            var t = o - e / 2;
            $(this).css({
                top: t,
                opacity: 1
            })
        });
        var o = $("#home-camera-slider").height() / 2;
        $("#home-slider .cameraContent").each(function() {
            var e = $(this).find(">.camera_caption");
            $(this).show();
            var t = e.height();
            $(this).hide();
            var n = o - t / 2;
            e.css({
                top: n
            })
        })
    }
}

function handleSlideshow() {
    if ($("#home-slider").length) {
        switch (window.show_slideshow) {
            case "camera":
                $("#home-camera-slider").camera({
                    loader: "none",
                    imagePath: window.blank_gif,
                    autoAdvance: window.slideshow_auto,
                    mobileAutoAdvance: window.slideshow_auto,
                    pagination: window.show_slideshow_dots,
                    thumbnails: false,
                    playPause: false
                });
                imagesLoaded("#home-slider", function() {
                    $("#home-slider-overlay").hide();
                    mockupCaptionSlider()
                });
                break;
            case "responsive":
                $("#home-slider").responsiveSlider({
                    autoplay: window.slideshow_auto,
                    interval: window.slideshow_interval,
                    transitionTime: 300
                });
                imagesLoaded("#home-slider", function() {
                    $("#home-slider-overlay").hide();
                    mockupCaptionSlider()
                });
                break;
            case "flexslider":
                $("#home-slider").flexslider({
                    animation: "fade",
                    prevText: "",
                    nextText: "",
                    slideshowSpeed: window.slideshow_interval,
                    slideshow: window.slideshow_auto,
                    controlNav: window.show_slideshow_dots,
                    start: function(e) {
                        $("body").removeClass("loading")
                    }
                });
                imagesLoaded("#home-slider", function() {
                    $("#home-slider-overlay").hide();
                    mockupCaptionSlider()
                });
                break
        }
    }
}

function handleMap() {
    if ($("#contact_map").length) {
        if (jQuery().gMap) {
            $("#contact_map").gMap({
                zoom: window.contact_zoom,
                scrollwheel: window.contact_scroll,
                maptype: window.contact_type,
                markers: [{
                    address: window.contact_address,
                    html: "_address",
                    icon: {
                        image: window.contact_icon,
                        iconsize: [188, 68],
                        iconanchor: [0, 68]
                    }
                }]
            })
        }
    }
}

function handleGridList() {
    $(".grid_list span").click(function() {
        if (!$(this).hasClass("active")) {
            $(".grid_list span").removeClass("active");
            $(this).addClass("active");
            if ($(this).hasClass("grid")) {
                $("#sandBox").removeClass("full_width")
            } else {
                $("#sandBox").addClass("full_width")
            }
        }
    })
}

function handleMenuScroll() {
    var e = $(this).scrollTop();
    if (window.header_style == "style_5") {
        var t = header_top + $("#header").outerHeight()
    } else {
        var t = $("#header").outerHeight()
    }
    if (touch == false && getWidthBrowser() >= 1024) {
        if (e > t) {
            if (!$("#header").hasClass("on")) {
                if (!$("body").hasClass("templateIndex")) {
                    $('<div style="min-height:' + t + 'px"></div>').insertBefore("#header")
                }
                if (window.header_style == "style_3" || window.header_style == "style_4") $("#header").addClass("on").addClass("fadeInDown");
                else $("#header").addClass("on")
            }
        } else {
            if ($("#header").hasClass("on")) {
                if (!$("body").hasClass("templateIndex")) {
                    $("#header").prev().remove()
                }
                if (window.header_style == "style_3" || window.header_style == "style_4") $("#header").removeClass("on").removeClass("fadeInDown");
                else $("#header").removeClass("on")
            }
        }
    }
}

function handleResetMenuScroll() {
    if (touch == false) {
        if (getWidthBrowser() < 1024) {
            if ($("#header").hasClass("on")) {
                if (!$("body").hasClass("templateIndex")) {
                    $("#header").prev().remove()
                }
                if (window.header_style == "style_3" || window.header_style == "style_4") $("#header").removeClass("on").removeClass("fadeInDown");
                else $("#header").removeClass("on")
            }
        } else {
            var e = $(this).scrollTop();
            var t = $("#header").outerHeight();
            if (e > t) {
                if (!$("#header").hasClass("on")) {
                    if (!$("body").hasClass("templateIndex")) {
                        $('<div style="min-height:' + t + 'px"></div>').insertBefore("#header")
                    }
                    if (window.header_style == "style_3" || window.header_style == "style_4") $("#header").addClass("on").addClass("fadeInDown");
                    else $("#header").addClass("on")
                }
            }
        }
    }
}

function handleCartSidebar() {
    jQuery(".cart-controller").click(function(e) {
        e.stopPropagation();
        jQuery(".cart-sidebar").toggleClass("opened");
        jQuery("html,body").toggleClass("cart-opened")
    });
    jQuery("#page").click(function() {
        jQuery(".cart-sidebar").removeClass("opened");
        jQuery("html,body").removeClass("cart-opened")
    })
}
//rt-add
function handleMenuMobile() {
    jQuery("#page").click(function() {
        jQuery(".menu-mobile").removeClass("opened");
        jQuery("html,body").removeClass("menu-opened")
    });
    jQuery("[data-toggle=offcanvas]").click(function(e) {
        e.stopPropagation();
        jQuery(".menu-mobile").toggleClass("opened");
        jQuery("html,body").toggleClass("menu-opened")
    });
    $(".navbar .nav li > .dropdown-link").hover(function() {
        $(this).addClass("hover")
    }, function() {
        $(this).removeClass("hover")
    });
    $(".is-mobile .navbar .nav li > .dropdown-link > span").click(function() {
        var e = $(this).parent();
        window.location = e.attr("href")
    });
    $(".navbar").on("click", ".nav li > .hover > span", function() {
        var e = $(this).parent();
        window.location = e.attr("href")
    });
    if (!window.auto_expand) {
        $(".is-mobile .menu-mobile .nav .fa-angle-down").click(function() {
            var e = $(this).parents(".dropdown-parent-submenu").first();
            if (e.hasClass("is_open")) {
                e.removeClass("is_open")
            } else {
                e.addClass("is_open")
            }
        })
    }
}
//end-rt-add
function resetProductImg() {
    $("#product-image #main-image").load(function() {
        $(".main-image-bg").hide();
        $("#product-image .main-image div").hide()
    })
}

function handleSearch() {
    $(".search-wrapper2 .search-submit").click(function() {
        var e = $(this).parents(".search-form"),
            t = $("#input-ajax", e);
        if ($(this).hasClass("active")) {
            e.submit()
        } else {
            t.css("visibility", "visible");
            $(this).addClass("active");
            t.focus()
        }
    });
    $(".search-wrapper4 .search-submit").click(function() {
        var e = $(this).parent();
        if (e.hasClass("active")) {
            e.removeClass("active");
            $("#header").removeClass("is_search")
        } else {
            e.addClass("active");
            $("#header").addClass("is_search")
        }
    });
    $(document).click(function(e) {
        if (!$(e.target).closest(".search-wrapper2 .search-form").length) {
            if ($(".search-wrapper2 .search-form").is(":visible")) {
                $(".search-wrapper2 .search-form #input-ajax").css("visibility", "hidden");
                $(".search-wrapper2 .search-form .search-submit").removeClass("active")
            }
        }
        if (!$(e.target).closest(".search-wrapper4").length) {
            if ($(".search-wrapper4 .search-table-wraper").is(":visible")) {
                $(".search-wrapper4").removeClass("active");
                $("#header").removeClass("active")
            }
        }
    })
}

function callbackSearchMobile() {
    var e = $(".is-mobile .is-mobile-search .fa-search");
    var t = $(".is-mobile .is-mobile-search .fa-times");
    var n = $(".is-mobile .is-mobile-search .input-search");
    var r = $(".is-mobile .is-mobile-search");
    e.click(function() {
        r.addClass("on");
        n.focus()
    });
    n.click(function() {
        return false
    });
    t.click(function() {
        r.removeClass("on")
    })
}

function ajaxAllProducts() {
    var e = new Array;
    var t = "/collections/all?view=ajax";
    $.ajax({
        type: "GET",
        url: t,
        beforeSend: function() {},
        success: function(t) {
            var n = $(t).find(".p");
            n.each(function() {
                var t = $.trim(this.getAttribute("data-t"));
                var n = $.trim(this.getAttribute("data-h"));
                var r = new Object;
                r.title = t;
                r.handle = n;
                e.push(r)
            })
        },
        dataType: "html"
    });
    return e
}

function handleAjaxSearch() {
    var e = ajaxAllProducts();
    $("#input-ajax").keyup(function() {
        var t = $(this);
        var n = $.trim(t.val().toLowerCase());
        $("#result-ajax").hide();
        if (n.length >= 3) {
            var r = $("#result-ajax .wrapper-ajax").empty();
            for (var i = 0; i < e.length; i++) {
                var s = e[i];
                var o = s.title;
                var u = s.handle;
                if (o.toLowerCase().indexOf(n) > -1) {
                    var a = o.replace(new RegExp("(" + n + ")", "gi"), '<span class="marked">$1</span>');
                    var f = '<li><a href="/products/' + u + '">' + a + "</a></li>";
                    r.append(f)
                }
            }
            if ($("#result-ajax .wrapper-ajax li").length) {
                $("#result-ajax").show()
            }
        } else {
            $("#result-ajax").hide()
        }
    });
    $(this).click(function(e) {
        if (!($(e.target).parent("#result-ajax").length > 0)) {
            $("#result-ajax").hide()
        }
    })
}

function handleCountdown() {
    $(".count_holder_big").each(function() {
        var e = $(this).find(".count_holder_small");
        $(this).hover(function() {
            e.addClass("hover").appendTo("body")
        }, function() {
            e.removeClass("hover").appendTo(this)
        }).mousemove(function(t) {
            var n = t.pageX + 60,
                r = t.pageY - 50,
                i = e.width(),
                s = e.height(),
                o = $(window).width() - (n + i),
                u = $(window).height() - (r + s);
            if (o < 50) n = t.pageX - i - 60;
            e.css({
                left: n,
                top: r
            })
        })
    })
}

function handleSmoothScroll() {
    $("body").on("click", ".smoothscroll", function(e) {
        e.preventDefault();
        var t = $(this).attr("href");
        if ($(t).find(".accordion-toggle").hasClass("collapsed")) {
            $(t).find(".accordion-toggle").trigger("click")
        }
        setTimeout(function() {
            $("html,body").animate({
                scrollTop: $(t).offset().top - 100
            }, 800, "swing")
        }, 300)
    })
}

function notifyIE7Users() {
    if ($("html").hasClass("ie8") || $("html").hasClass("ie7")) {
        if (window.notify_ie8_page) {
            $.ajax({
                type: "GET",
                url: "pages/" + window.notify_ie8_page,
                beforeSend: function() {},
                success: function(e) {
                    var t = $(e).find("#col-main > .page > .page_content");
                    $("body").html(t.html()).show()
                },
                dataType: "html"
            })
        } else {
            var e = "<h1>Unsupported Browser</h1>";
            $("body").html(e).show()
        }
    }
}

function socialSharing() {
    var e = $(".social-sharing"),
        t = e.find("a.share"),
        n = e.attr("data-permalink");
    var r = $(".share-facebook"),
        i = $(".share-twitter"),
        s = $(".share-pinterest"),
        o = $(".share-google");
    if (r.length) {
        $.getJSON("https://graph.facebook.com/?id=" + n + "&callback=?", function(e) {
            if (e.shares) {
                r.find(".share-count").text(e.shares).addClass("is-loaded")
            } else {
                r.find(".share-count").remove()
            }
        })
    }
    if (i.length) {
        $.getJSON("https://cdn.api.twitter.com/1/urls/count.json?url=" + n + "&callback=?", function(e) {
            if (e.count > 0) {
                i.find(".share-count").text(e.count).addClass("is-loaded")
            } else {
                i.find(".share-count").remove()
            }
        })
    }
    if (s.length) {
        $.getJSON("https://api.pinterest.com/v1/urls/count.json?url=" + n + "&callback=?", function(e) {
            if (e.count > 0) {
                s.find(".share-count").text(e.count).addClass("is-loaded")
            } else {
                s.find(".share-count").remove()
            }
        })
    }
    if (o.length) {
        o.find(".share-count").addClass("is-loaded")
    }
    t.on("click", function(e) {
        e.preventDefault();
        var t = $(this),
            n = t.attr("class").replace("-", "_"),
            r = t.attr("href"),
            i = 700,
            s = 400;
        switch (n) {
            case "share-twitter":
                s = 300;
                break;
            case "share-fancy":
                i = 480;
                s = 720;
                break;
            case "share-google":
                i = 500;
                break
        }
        window.open(r, n, "width=" + i + ", height=" + s)
    })
}

function detectOptions() {
    if (getWidthBrowser() < 992) {
        if (jQuery("#product-header-first").is(":empty")) {
            jQuery("#product-header").detach().appendTo("#product-header-first")
        }
    } else {
        if (!jQuery("#product-header-first").is(":empty")) {
            jQuery("#product-header").detach().appendTo("#product-header-last")
        }
    }
}

function initDocumentReady() {
    detectOptions();
    callbackImagesLoaded();
    notifyIE7Users();
    if (window.header_search_ajax) handleAjaxSearch();
    handleTooltip();
    handleCountdown();
    handleTabs();
    handleSearch();
    callbackSearchMobile();
    goToPage();
    handleScreenshotPreview();
    handleMenuMobile();
    handleCartSidebar();
    handleDropdown();
    handleImageThumbs();
    resetProductImg();
    socialSharing();
    $(".noclose").click(function(e) {
        e.stopPropagation()
    });
    handleSlideshow();
    handleMap();
    if (touch == false) {
        if ($("#home-slider").length) {
            imagesLoaded("#home-slider", function() {
                handleDataAnimate()
            })
        } else {
            handleDataAnimate()
        }
    }
    handleScrollToTop();
    handleSmoothScroll();
    alwaysRefreshZoom();
    handleGridList();
    if ($(".product-fancybox-buttons").length) {
        $(".product-fancybox-buttons").fancybox({
            closeBtn: false,
            helpers: {
                buttons: {}
            }
        })
    }
    fakewaffle.responsiveTabs(["xs", "sm"])
}

function callbackImagesLoaded() {
    if ($(".product-image-thumb").length) {
        if (window.viewmore_image_display == "carousel") {
            $(".product-image-thumb").owlCarousel({
                navigation: true,
                pagination: false,
                mouseDrag: false,
                items: 5,
                itemsDesktop: [1199, 4],
                itemsDesktopSmall: [991, 5],
                itemsTablet: [768, 5],
                itemsMobile: [479, 3],
                scrollPerPage: window.viewmore_image_scroll,
                navigationText: ['<span class="btn mini"><i class="fa fa-angle-left"></i></span>', '<span class="btn mini"><i class="fa fa-angle-right"></i></span>']
            })
        }
    }
    if ($("#product-related").length) {
        if (window.productspg_featured_style == "carousel") {
            $("#product-related").owlCarousel({
                navigation: true,
                pagination: false,
                mouseDrag: false,
                items: 4,
                itemsDesktop: [1199, 4],
                itemsDesktopSmall: [991, 4],
                itemsTablet: [768, 3],
                itemsMobile: [479, 2],
                scrollPerPage: window.productspg_featured_scroll,
                navigationText: ['<span class="btn mini"><i class="fa fa-angle-left"></i></span>', '<span class="btn mini"><i class="fa fa-angle-right"></i></span>'],
                beforeMove: function(e) {
                    if (touch == false) {
                        var t = $(e);
                        var n = t.find(".animated");
                        n.removeClass("animated").unbind("appear")
                    }
                }
            })
        }
    }
    $(".featured-collections-child").owlCarousel({
        navigation: true,
        pagination: false,
        mouseDrag: false,
        lazyLoad: true,
        items: 2,
        itemsDesktop: [1199, 2],
        itemsDesktopSmall: [991, 3],
        itemsTablet: [768, 3],
        itemsTabletSmall: [767, 2],
        itemsMobile: [479, 1],
        scrollPerPage: true,
        navigationText: ['<span class="btn medium"><i class="fa fa-angle-left"></i></span>', '<span class="btn medium"><i class="fa fa-angle-right"></i></span>'],
        beforeMove: function(e) {
            if (touch == false) {
                var t = $(e);
                var n = t.find(".animated");
                n.removeClass("animated").unbind("appear")
            }
        }
    });
    if ($("#featured-products").length) {
        if (window.featured_products_home_style == "carousel") {
            $("#featured-products").owlCarousel({
                navigation: true,
                pagination: false,
                mouseDrag: false,
                items: 4,
                itemsDesktop: [1199, 4],
                itemsDesktopSmall: [991, 3],
                itemsTablet: [768, 3],
                itemsTabletSmall: [767, 2],
                itemsMobile: [479, 1],
                scrollPerPage: window.featured_products_home_scroll,
                navigationText: ['<span class="btn medium"><i class="fa fa-angle-left"></i></span>', '<span class="btn medium"><i class="fa fa-angle-right"></i></span>'],
                beforeMove: function(e) {
                    if (touch == false) {
                        var t = $(e);
                        var n = t.find(".animated");
                        n.removeClass("animated").unbind("appear")
                    }
                }
            })
        }
    }
    if ($("#special-offers").length) {
        $("#special-offers").owlCarousel({
            navigation: true,
            pagination: false,
            mouseDrag: false,
            items: 3,
            itemsDesktop: [1199, 3],
            itemsDesktopSmall: [991, 3],
            itemsTablet: [768, 3],
            itemsTabletSmall: [767, 2],
            itemsMobile: [479, 1],
            scrollPerPage: false,
            navigationText: ['<span class="btn medium"><i class="fa fa-angle-left"></i></span>', '<span class="btn medium"><i class="fa fa-angle-right"></i></span>'],
            beforeMove: function(e) {
                if (touch == false) {
                    var t = $(e);
                    var n = t.find(".animated");
                    n.removeClass("animated").unbind("appear")
                }
            }
        })
    }
    if ($("#our-partner").length) {
        $("#our-partner").owlCarousel({
            navigation: true,
            pagination: false,
            mouseDrag: false,
            items: 5,
            itemsDesktop: [1199, 5],
            itemsDesktopSmall: [991, 4],
            itemsTablet: [768, 3],
            itemsTabletSmall: [767, 3],
            itemsMobile: [479, 1],
            scrollPerPage: false,
            navigationText: ['<span class="btn medium"><i class="fa fa-angle-left"></i></span>', '<span class="btn medium"><i class="fa fa-angle-right"></i></span>'],
            beforeMove: function(e) {
                if (touch == false) {
                    var t = $(e);
                    var n = t.find(".animated");
                    n.removeClass("animated").unbind("appear")
                }
            }
        })
    }
    if ($("#latest-posts").length) {
        $("#latest-posts").on("hover", ".latest-post", function() {
            $("#latest-posts .latest-post").removeClass("active");
            $(this).addClass("active")
        })
    }
}
var touch = false,
    clickEv = "click",
    header_top = jQuery("#header").offset().top;
$(window).resize(function() {
    if (window.header_sticky) handleResetMenuScroll();
    detectOptions();
    mockupCaptionSlider();
    mockupCaptionVideo()
});
$(window).scroll(function() {
    if (window.header_sticky) handleMenuScroll()
});
jQuery(document).ready(function(e) {
    if (isMobile()) {
        touch = true;
        e("body").addClass("touch");
        clickEv = "touchstart"
    } else {
        e("body").addClass("notouch");
        if (navigator.appVersion.indexOf("Mac") != -1) {
            if (navigator.userAgent.indexOf("Safari") > -1) {
                e("body").addClass("macos")
            }
        }
    }
    initMegaMenu();
    mockupCaptionVideo();
    initDocumentReady();
    if (window.header_style == "style_2") {
        e("#header .icon_menu").click(function() {
            if (e("#header").hasClass("en_menu")) {
                e("#header").removeClass("en_menu")
            } else {
                e("#header").addClass("en_menu")
            }
        })
    }
})