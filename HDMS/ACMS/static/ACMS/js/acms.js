/**
 * Created by koyexes on 8/4/2016.
 */

$('#loginModalJs').modal('show');// automatically showing the modal login error when a login error occurs

$('#loginModalJs').on('hidden.bs.modal', function(e){
    $('#loginErrorAlert').alert('close');
    $('#loginModalJs').attr('id', 'loginModal');
    $('#loginForm').trigger('reset');
});

$('#loginModal').on('show.bs.modal', function (e) {
     $("#loginForm").trigger('reset');
});

// works with the homepage icons, changing their color gradient as mouse hovers over their labels
$('.iconLabel').hover(
    function(e){ $(e.target).parent().siblings('img').css({" -ms-filter" :"grayscale(0%)", "filter" : "grayscale(0%)", "-webkit-filter" : "grayscale(0%)"});},
    function(e){ $(e.target).parent().siblings('img').css({" -ms-filter" :"grayscale(100%)", "filter" : "grayscale(100%)", "-webkit-filter" : "grayscale(100%)"});}
);

// resetting all form inputs when form modal closes
$('#patientModalForm').on('hidden.bs.modal', function(e){
   // alert("Hello world");
   $('#patientForm').trigger('reset');
});

