/***************************** show password in login js****************************/

    $("#basic-addon2").click(function () {
        let passwordField = $("#password");
        let passwordFieldAttr = passwordField.attr("type");

        if (passwordFieldAttr == "password") {
            passwordField.attr("type", "text");
            $(this).html('<i class="fa fa-eye-slash" aria-hidden="true"></i>');
        } else {
            passwordField.attr("type", "password");
            $(this).html('<i class="fa fa-eye" aria-hidden="true"></i>');
        }
    });

////////////////////////////////////////////

function showPassword() {
    var key_attr = $('.inputpassword').attr('type');
    if (key_attr != 'text') {
        $('.checkbox').addClass('show');
        $('.inputpassword').attr('type', 'text');
    } else {
        $('.checkbox').removeClass('show');
        $('.inputpassword').attr('type', 'password');
    }
};

////////////////////////////////////////////

function showPassword2() {
    var key_attr = $('.inputpassword-repetition').attr('type');
    if (key_attr != 'text') {
        $('.checkbox').addClass('show');
        $('.inputpassword-repetition').attr('type', 'text');
    } else {
        $('.checkbox').removeClass('show');
        $('.inputpassword-repetition').attr('type', 'password');
    }
} ;

/*************************************** slider js***************************************/

  //slider-1  
    if ($("#slider_header").length) {
        $(".slider_baner-homepage").owlCarousel({
            items: 1,
            animateOut: 'fadeOut',
            animateIn: 'fadeIn',
            rtl: true,
            loop: true,
            smartSpeed: 500,
            nav: true,
            navText: ["<i class='fal fa-chevron-circle-right'></i>", "<i class='fal fa-chevron-circle-left'></i>"],
            dots: true,
            lazyLoadEager: 3,
         
        })
    };

  //slider-2

    if ($(".slider_product").length) {
        $(".slider_product").owlCarousel({
            margin: 30,
            rtl: true,
            loop: true,
            autoplaytimeout: 4000,
            smartSpeed: 500,
            nav: true,
            navText: ["<i class='fal fa-chevron-circle-right'></i>", "<i class='fal fa-chevron-circle-left'></i>"],
            dots: true,
            lazyLoadEager: 3,
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: 1,
                },
                // breakpoint from 576 up
                576: {
                    items: 2,
                },
                // breakpoint from 768 up
                768: {
                    items: 3,
                },

                992: {
                    items: 3,
                },

                1200: {
                    items: 4,
                }
            }
        })
    };

  //slider-3
    if ($(".slider-product-bestSale-style2").length) {
        $(".slider-product-bestSale-style2").owlCarousel({
            rtl: true,
            loop: true,
            autoplaytimeout: 4000,
            smartSpeed: 1300,
            nav: true,
            navText: ["<i class='fas fa-chevron-right'></i>", "<i class='fas fa-chevron-left'></i>"],
            dots: true,
            lazyLoadEager: 3,
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: 1,
                },
                // breakpoint from 576 up
                576: {
                    items: 2,
                },
                // breakpoint from 768 up
                768: {
                    items: 3,
                },

                992: {
                    items: 4,
                },

                1200: {
                    items:5,
                }
            }
        })
    };


  //slider-4
    if ($(".slider-product-style2").length) {
        $(".slider-product-style2").owlCarousel({
            rtl: true,
            loop: true,
            autoplaytimeout: 4000,
            smartSpeed:  1300,
            nav: true,
            navText: ["<i class='fas fa-chevron-right'></i>", "<i class='fas fa-chevron-left'></i>"],
            dots: true,
            lazyLoadEager: 3,
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: 1,
                },
                // breakpoint from 576 up
                576: {
                    items: 2,
                },
                // breakpoint from 768 up
                768: {
                    items: 3,
                },

                992: {
                    items: 4,
                },

                1200: {
                    items:4,
                }
            }
        })
    };


  //slider-5
    if ($(".slider-sidebar").length) {
        $(".slider-sidebar").owlCarousel({
            rtl: true,
            loop: true,
            autoplaytimeout: 4000,
            smartSpeed: 1300,
            dots: true,
            lazyLoadEager: 3,
            nav: true,
            navText: ["<i class='fas fa-chevron-right'></i>", "<i class='fas fa-chevron-left'></i>"],
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: 1,
                },
                // breakpoint from 576 up
                576: {
                    items: 2,
                },
                // breakpoint from 768 up
                768: {
                    items: 3,
                },

                992: {
                    items: 1,
                },

                1200: {
                    items:1,
                }
            }
        })
 
    };

  //slider-6
    if ($(".slider-off-product").length) {
        $(".slider-off-product").owlCarousel({
            rtl: true,
            loop: true,
            autoplaytimeout: 4000,
            smartSpeed: 1300,
            nav: true,
            navText: ["<i class='fas fa-chevron-right'></i>", "<i class='fas fa-chevron-left'></i>"],
            dots: true,
            lazyLoadEager: 3,
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: 1,
                },
                // breakpoint from 576 up
                576: {
                    items: 2,
                },
        
                1200: {
                    items:2,
                }
            }
        })
    };


  //slider-7
    if ($(".slider-product-toSidebar").length) {
        $(".slider-product-toSidebar").owlCarousel({
            margin: 30,
            rtl: true,
            loop: true,
            autoplaytimeout: 4000,
            smartSpeed: 500,
            nav: true,
            navText: ["<i class='fal fa-chevron-circle-right'></i>", "<i class='fal fa-chevron-circle-left'></i>"],
            dots: true,
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: 1,
                },
                // breakpoint from 576 up
                576: {
                    items: 2,
                },
                // breakpoint from 768 up
                768: {
                    items: 3,
                },

                992: {
                    items: 2,
                },

                1200: {
                    items: 3,
                }
            }
        })
    };

  //slider-8
    if ($(".slider_brand").length) {
        $(".slider_brand").owlCarousel({
            // items: 9,
            center: true,
            margin: 15,
            rtl: true,
            loop: true,
            // autoplay: true,
            autoplaytimeout: 4000,
            smartSpeed: 500,
            nav: true,
            navText: ["<i class='fal fa-chevron-circle-right'></i>", "<i class='fal fa-chevron-circle-left'></i>"],
            dots: true,
            lazyLoadEager: 3,
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: 2,
                },
                400: {
                    items: 3,
                },

                // breakpoint from 576 up
                576: {
                    items: 4,

                },
                // breakpoint from 768 up
                768: {
                    items: 5,
                },

                992: {
                    items: 7,
                },

                1200: {
                    items: 8,
                }
            }
        })
    };


  //slider-9
    if ($("#Related-posts-slider").length) {
        $(".slider-Related-posts").owlCarousel({
            rtl: true,
            loop: true,
            // autoplay: true,
            autoplaytimeout: 4000,
            smartSpeed: 500,
            nav: true,
            navText: ["<i class='fal fa-chevron-circle-right'></i>", "<i class='fal fa-chevron-circle-left'></i>"],
            dots: true,
            lazyLoadEager: 3,
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: 1,
                    margin: 20,

                },
                // breakpoint from 576 up
                576: {
                    items: 1,
                    margin: 20,

                },
                // breakpoint from 768 up
                768: {
                    items: 2,
                    margin: 8,
                },

                992: {
                    items: 3,
                    center: true,
                },

                1200: {
                    items: 3,
                    margin: 10,
                    center: true,
                }
            }
        })
    }
  //slider-10
    if ($("#testimonial-slider").length) {
        $(".slider-show-customers-comment").owlCarousel({
            items: 1,
            rtl: true,
            loop: true,
            autoplay: true,
            autoplaytimeout: 5000,
            smartSpeed: 500,
            nav: true,
            navText: ["<i class='fal fa-chevron-circle-right'></i>", "<i class='fal fa-chevron-circle-left'></i>"],
            dots: true,
        })
    }


  //slider-11
    if ($("#team-slider").length) {
        $(".slider-team").owlCarousel({
            margin: 20,
            rtl: true,
            loop: true,
            smartSpeed: 500,
            navText: ["<i class='fal fa-chevron-circle-right'></i>", "<i class='fal fa-chevron-circle-left'></i>"],
            dots: true,
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: 1,
                },
                // breakpoint from 576 up
                576: {
                    items: 2,
                },
                // breakpoint from 768 up
                768: {
                    items: 3,
                },

                992: {
                    items: 3,
                },

                1200: {
                    items: 4,
                }
            }
        })
    }


/*************************************** countdown js***************************************/
    
if ($("#countdown-1").length) {
    const second = 1000,
        minute = second * 60,
        hour = minute * 60,
        day = hour * 24;
    let countDown = new Date('Sep 19, 2022 00:00:00').getTime(),
        x = setInterval(function () {
            let now = new Date().getTime(),
                distance = countDown - now;
            document.getElementById('days').innerText = Math.floor(distance / (day)),
                document.getElementById('hours').innerText = Math.floor((distance % (day)) / (hour)),
                document.getElementById('minutes').innerText = Math.floor((distance % (hour)) / (minute))
            document.getElementById('seconds').innerText = Math.floor((distance % (minute)) / second);
        }, second)
    }
    
/*************************************** search js***************************************/

$(".icon-search ").click(function () {
    $(".bg-searchform").css({ "opacity": "1", "visibility": " visible","transform": " scaleY(1)" });
});

$(".area-close-search").click(function (e) {
    $(".bg-searchform").css({ "opacity": "0", "visibility": "hidden","transform": " scaleY(0)"  });
});

/*************************************** box cart shopping ***************************************/

$(".icon-shooping-cart").click(function () {
    $(".box-add-to-cart-header").addClass("cart-woocommerce-toogle");
    $(".bg-close").css({ "display": "block" });
});

$(".bg-close").click(function () {
    $(".box-add-to-cart-header").removeClass("cart-woocommerce-toogle");
    $(this).css({ "display": "none" });
});


/*************************************** menu mobile js***************************************/

$(".icon_meni_bar i").click(function () {
    $(".menu_mobile").css({ "right": "0" });
    $(".bg-close").css({ "display": "block" });
});
$(".close_menu_mobile").click(function () {
    $(".menu_mobile").css({ "right": "-100%" });
    $(".bg-close").css({ "display": "none" });
});
$(".bg-close").click(function () {
    $(".menu_mobile").css({ "right": "-100%" });
    $(this).css({ "display": "none" });
});

////////////////////////////////
$("#radio-color-1").click(function () {
    var empty = $('#colorOptionText').text();
    var span = "قرمز";
    if (empty === " ") {
        $("#colorOptionText").append(span);
    }
    else {
        return
    }
});

////////////////////////////////
$(window, document, undefined).ready(function () {

    $('.input').blur(function () {
        var $this = $(this);
        if ($this.val())
            $this.addClass('used');
        else
            $this.removeClass('used');
    });
});
////////////////////////////////
$('#tab1').on('click', function () {
    $('#tab1').addClass('login-shadow');
    $('#tab2').removeClass('signup-shadow');
});

$('#tab2').on('click', function () {
    $('#tab2').addClass('signup-shadow');
    $('#tab1').removeClass('login-shadow');

});

/********************************* multilevel accordion menu mobile js ********************************/

// prevent page from jumping to top from  # href link
$('li.menu-item-has-children > a').click(function (e) {
    e.preventDefault();
});
// remove link from menu items that have children
$("li.menu-item-has-children > a").attr("href", "#");
//  function to open / close menu items
$(".menu-multi-level a").click(function () {
    var link = $(this);
    var closest_ul = link.closest("ul");
    var parallel_active_links = closest_ul.find(".active")
    var closest_li = link.closest("li");
    var link_status = closest_li.hasClass("active");
    var count = 0;
    closest_ul.find("ul").slideUp(function () {
        if (++count == closest_ul.find("ul").length)
            parallel_active_links.removeClass("active");
    });
    if (!link_status) {
        closest_li.children("ul").slideDown();
        closest_li.addClass("active");
    }
})

/****************************** scroll link ******************************/

$('.scrollTo').click(function () {

    $('html, body').animate({
        scrollTop: $($(this).attr('href')).offset().top
    }, 500);
    return false;
});


/****************************** scroll to top ******************************/

$(window).scroll(function () {
    if ($(window).scrollTop() > 200) {
        $("a.scroll-To-top").css({ "visibility": " visible", "transform": "translateY(0)" });
    } else {
        $("a.scroll-To-top").css({ "visibility": " hidden", "transform": "translateY(2rem)" });
    }
});


/**************************** wow animation to scroll ****************************/

$(document).ready(function () {

    if ($("#body-homepage").length) {

        wow = new WOW(
            {
                boxClass: 'wow',      // default
                animateClass: 'animated', // default
                offset: 0,          // default
                mobile: false,       // default
                live: true        // default
            }
        )
        wow.init();
    }
});


/****************************** fancybox photo ******************************/

// add all to same gallery
$(".gallery a").attr("data-fancybox", "mygallery");
// assign captions and title from alt-attributes of images:
$(".gallery a").each(function () {
    $(this).attr("data-caption", $(this).find("img").attr("alt"));
    $(this).attr("title", $(this).find("img").attr("alt"));
});


/******************************  product Gallery and Zoom ******************************/

    if ($(".single-product-zoom").length) {

        // activation carousel plugin
        var galleryThumbs = new Swiper('.gallery-thumbs', {
            spaceBetween: 5,
            freeMode: true,
            watchSlidesVisibility: true,
            watchSlidesProgress: true,
            breakpoints: {
                0: {
                    slidesPerView: 3,
                },
                992: {
                    slidesPerView: 4,
                },
            }
        });
        var galleryTop = new Swiper('.gallery-top', {
            spaceBetween: 10,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            thumbs: {
                swiper: galleryThumbs
            },
        });
        // change carousel item height
        // gallery-top
        let productCarouselTopWidth = $('.gallery-top').outerWidth();
        $('.gallery-top').css('height', productCarouselTopWidth);

        // gallery-thumbs
        let productCarouselThumbsItemWith = $('.gallery-thumbs .swiper-slide').outerWidth();
        $('.gallery-thumbs').css('height', productCarouselThumbsItemWith);

        // activation zoom plugin
        var $easyzoom = $('.easyzoom').easyZoom();

    }

/*************************************** input type number cart ***************************************/

document.addEventListener('DOMContentLoaded', function () {
    var inputs = document.getElementsByClassName('input-number-wrapper')

    function incInputNumber(input, step) {
        var val = +input.value
        if (isNaN(val)) val = 0
        val += step
        input.value = val > 1 ? val : 1
        // If you need to change the input value in the DOM :
        // var newValue = val > 0 ? val : 0;
        // input.setAttribute("value", newValue);
    }

    Array.prototype.forEach.call(inputs, function (el) {
        var input = el.getElementsByTagName('input')[0]

        el.getElementsByClassName('increase')[0].addEventListener('click', function () { incInputNumber(input, 1) })
        el.getElementsByClassName('decrease')[0].addEventListener('click', function () { incInputNumber(input, -1) })
    })

});


/*************************************** animation image about us***************************************/

    if ($(".area-img-about-us").length) {
        /* Store the element in el */
        let el = document.getElementById('tilt')

        /* Get the height and width of the element */
        const height = el.clientHeight
        const width = el.clientWidth

        /*
          * Add a listener for mousemove event
          * Which will trigger function 'handleMove'
          * On mousemove
          */
        el.addEventListener('mousemove', handleMove)

        /* Define function a */
        function handleMove(e) {
            /*
              * Get position of mouse cursor
              * With respect to the element
              * On mouseover
              */
            /* Store the x position */
            const xVal = e.layerX
            /* Store the y position */
            const yVal = e.layerY

            /*
              * Calculate rotation valuee along the Y-axis
              * Here the multiplier 20 is to
              * Control the rotation
              * You can change the value and see the results
              */
            const yRotation = 20 * ((xVal - width / 2) / width)

            /* Calculate the rotation along the X-axis */
            const xRotation = -20 * ((yVal - height / 2) / height)

            /* Generate string for CSS transform property */
            const string = 'perspective(2000px) scale(1) rotateX(' + xRotation + 'deg) rotateY(' + yRotation + 'deg)'

            /* Apply the calculated transformation */
            el.style.transform = string
        }

        /* Add listener for mouseout event, remove the rotation */
        el.addEventListener('mouseout', function () {
            el.style.transform = 'perspective(500px) scale(1) rotateX(0) rotateY(0)'
        })

        /* Add listener for mousedown event, to simulate click */
        el.addEventListener('mousedown', function () {
            el.style.transform = 'perspective(500px) scale(0.9) rotateX(0) rotateY(0)'
        })

        /* Add listener for mouseup, simulate release of mouse click */
        el.addEventListener('mouseup', function () {
            el.style.transform = 'perspective(500px) scale(1.1) rotateX(0) rotateY(0)'
        })

    }

/*************************************** slidtoggle forms checkout ***************************************/


    $('#link-login').click(function (e) {
        e.preventDefault();
        $('.area-form-login').slideToggle(300);

    });


    $('#link-coupon').click(function (e) {
        e.preventDefault();
        $('.area-coupon').slideToggle(300);

    });

    $('#createaccount').click(function () {

        $('.area-create-account').slideToggle(300);

    });


    $('#input-shipping').click(function () {

        $('.area-formShippingFields').slideToggle(300);

    });


    // $('#payment-text2, #payment-text3').collapse('hide');
    $('input[name="inlineRadioOptions"]').change(function () {
        if ($('#inlineRadio1').is(":checked")) {
            $('#payment-text1').collapse('show');
        } else {
            $('#payment-text1').collapse('hide');
        }


        if ($('#inlineRadio2').is(":checked")) {
            $('#payment-text2').collapse('show');
        } else {
            $('#payment-text2').collapse('hide');
        }


        if ($('#inlineRadio3').is(":checked")) {
            $('#payment-text3').collapse('show');
        } else {
            $('#payment-text3').collapse('hide');
        }

    });


/*************************************** shop filter drawer js***************************************/

$("#button-filter-offCavas").click(function () {
    $(".sidebar-product-filter").css({ "left": "0" });
    $(".bg-close").css({ "display": "block" });
});
$(".close-sidebarProductFilter").click(function () {
    $(".sidebar-product-filter").css({ "left": "-100%" });
    $(".bg-close").css({ "display": "none" });
});

$(".bg-close").click(function () {
    $(".sidebar-product-filter").css({ "left": "-100%" });
    $(this).css({ "display": "none" });
});


$("#button-filter-drawer").click(function (e) {
    e.preventDefault();
    $(".container-content-shop").toggleClass("active");

});


/*************************************** sticky addtocart single post js***************************************/

$(window).scroll(function () {
    if ($(window).scrollTop() > 600) {
        var widthWindows = window.innerWidth;
        if (widthWindows >= 992) {
            $(".area-addToCart-sticky-singlePost").css({ "bottom": "0" });
        }
        if (widthWindows < 992) {
            $(".area-addToCart-sticky-singlePost").css({ "bottom": "3.3rem" });
        }
    } else {
        $(".area-addToCart-sticky-singlePost").css({ "bottom": "-100%" });
    }
});

/***************************************  modal reload homepage js***************************************/
$(document).ready(function () {
    $('#modal-subscribe').modal('show');
   
 
});


$(document).ready(function () {
    if ($(".exzoom").length) {
        $('.container').imagesLoaded(function () {
            $("#exzoom").exzoom({
                autoPlay: false,
            });
            $("#exzoom").removeClass('hidden')
        });
    }
});

  /***************************** box side sidebar-account js*****************************/

  $(".icon_meni_bar").click(function () {
    $(".sidebar-account").css({ "right": "0" });
    $(".bg-close").css({ "display": "block" });
});
$(".close_addtocart").click(function () {
    $(".sidebar-account").css({ "right": "-100%" });
    $(".bg-close").css({ "display": "none" });
});

$(".bg-close").click(function () {
    $(".sidebar-account").css({ "right": "-100%" });
    $(this).css({ "display": "none" });
});


 /***************************** category menu homepage-2 js*****************************/

    $(".container-category-menu").click(function () { 

     $(".area-category-menu>.category-drupdown-menu >ul >li").slideToggle();
        });
        




  


   