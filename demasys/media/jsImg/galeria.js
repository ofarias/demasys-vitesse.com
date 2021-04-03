window.viewmore_image_display = 'carousel';
window.viewmore_image_scroll = true;
window.productspg_featured_style = 'carousel';
window.productspg_featured_scroll = true;
window.header_style = 'style_6';
window.main_image_display = 'both';
window.header_search_ajax = true;
window.header_sticky = true;
function initMegaMenu(){
  var nav_name = '.nav_shop';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('full_width');
  var menu_bg_url = '';
  jQuery(nav_name).addClass('has_bg').css({'background-image':menu_bg_url, 'background-position':'100% 100%', 'background-repeat':'no-repeat'});
  var menu_height = 300;
  jQuery(nav_name).css({'min-height':menu_height + 'px'});
  var nav_name = '.nav_';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('custom_width');
  var nav_name = '.nav_';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('custom_width');
  var nav_name = '.nav_';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('custom_width');
  var nav_name = '.nav_';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('custom_width');
  var nav_name = '.nav_';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('custom_width');
  var nav_name = '.nav_';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('custom_width');
  var nav_name = '.nav_';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('custom_width');
  var nav_name = '.nav_';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('custom_width');
  var nav_name = '.nav_';
  jQuery(nav_name).parent().addClass('mega_menu').addClass('custom_width');
  var fixMegaMenuPosition = function() {
    jQuery('.mega_menu.custom_width').each(function(index, value) {
      var custom_menu = jQuery(this),
            col_width = 200, //width of a column
            maxcol = 3,      //max columns in a row
            col = 1;         //min num of column
            var nchild = custom_menu.find('>ul.dropdown-menu').children('li.dropdown-parent-submenu').length;
            if ( Math.ceil(nchild / maxcol) > 1 ) {
              col = 3;
            } else {
              col = nchild;
            }
            var cal_width = col_width * col + col*15 +10;
            custom_menu.find('>ul.dropdown-menu').css({'width':cal_width + 'px'});
          });
  }
  fixMegaMenuPosition();
  var fixMegaMenuPositionFullWidth = function() {
    jQuery('.mega_menu.full_width').each(function(index, value) {
      var _container_offet = jQuery('.navigation_wrapper').offset();
      var _cur_offset = jQuery(value).offset();
      var _margin_left = _cur_offset.left - _container_offet.left;
      _margin_left = _margin_left - (jQuery('.navigation_wrapper').outerWidth() - jQuery('.navigation_wrapper').width()) / 2;
      jQuery(value).find('>ul.dropdown-menu').css('width', jQuery('.navigation_wrapper').width()).css('left', '-' + _margin_left + 'px');
    });
  }
  _onresize( fixMegaMenuPositionFullWidth );
  fixMegaMenuPositionFullWidth();
  jQuery('.mega_menu.full_width').on('hover', function() {
    var _container_offet = jQuery('.navigation_wrapper').offset();
    var _cur_offset = jQuery(this).offset();
    var _margin_left = _cur_offset.left - _container_offet.left;
    _margin_left = _margin_left - (jQuery('.navigation_wrapper').outerWidth() - jQuery('.navigation_wrapper').width()) / 2;
    jQuery(this).find('>ul.dropdown-menu').css('width', jQuery('.navigation_wrapper').width()).css('left', '-' + _margin_left + 'px');
  });
}
function _onresize( f ) {
  jQuery(window).on( 'resize', f );
}