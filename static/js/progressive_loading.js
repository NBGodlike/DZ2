/**
 * Created by user on 10.01.2017.
 */
var page = 1;
 var already = false;

 function ajax_get_questions() {
     already = true;
     page += 1;
     $.ajax({
         url: `/course_list/${page}/`,
         type: 'GET',
         success: function (data) {
             course_list.innerHTML += data;
             already = false;
         },
         error: function () {
             console.log('http error');
             already = false;
             page -= 1;
         },
     })
 }

 window.onscroll = function() {
     var scrollHeight = Math.max(
         document.body.scrollHeight, document.documentElement.scrollHeight,
         document.body.offsetHeight, document.documentElement.offsetHeight,
         document.body.clientHeight, document.documentElement.clientHeight
     );
     var scrolled = window.pageYOffset || document.documentElement.scrollTop;
     if (!already && scrollHeight - scrolled <= document.documentElement.clientHeight + 200) {
       ajax_get_questions();
     }
 }
