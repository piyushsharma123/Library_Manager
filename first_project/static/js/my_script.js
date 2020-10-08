(function($) {
$( "#id_pay_0" ).click(function() {//pay now window appear and disappear
    console.log(window);
    const status = document.getElementById("id_pay_0").checked;
    const x = document.getElementById("pay_now");
    const elements = document.querySelectorAll(".bill input");
    for(element of elements){
        element.required = true;
        console.log("display",element);
    }
    if (status){
        x.style.display = 'block';
        
    }
});
// $( "#submit_btn").click(function(){
//     console.log("submit is clicked");
//     document.getElementById("user_form").submit();
//     console.log("User form submit");
//     document.getElementById("bill_form").submit();
//     console.log("Bill form submit");
// });
$( "#id_pay_1" ).click(function() {//pay now window appear and disappear
    const status = document.getElementById("id_pay_1").checked;
    const x = document.getElementById("pay_now");
    const elements = document.querySelectorAll(".bill input");
    for(element of elements){
        element.required = false;
        console.log("hide",element);
    }
    if (status){
        x.style.display = 'none';
        
    }
    $( "#id_pay_1" )
});
$( "#clear_file" ).click(function() {//pay now window appear and disappear
    const st = document.getElementById("id_file");
    st.value='';
    const reader = new FileReader();
    reader.addEventListener("load",()=>{
            document.getElementById("blah").setAttribute("src","/static/img/avatars/profile.jpg");
        console.log(this.value);
        });
        reader.readAsDataURL(file);
});
    
    
// $( "#inputfile" ).change(function() {//pay now window appear and disappear
//     $('#blah').attr('src', this.files[0]);
// });
$( "#id_file" ).change(function() {
    file = this.files[0];
    if(file){
        const reader = new FileReader();
        
        reader.addEventListener("load",()=>{
            document.getElementById("blah").setAttribute("src",reader.result);
            console.log(document.getElementById("blah").src);
        });
        reader.readAsDataURL(file);
    }
});
$(".nav li").on("click", function() {
      $(".nav li").removeClass("active");
      $(this).addClass("active");
});   
    

// $( "#pay_1" ).click(mark("pay_now_check"));
// $( "#pay_2" ).click(mark("pay_later_check"));
// function mark(rd){
//     document.getElementById(rd).setAttribute("style","checked:"+!document.getElementById(rd).checked);

// }
})(jQuery);

(function (){
    if (document.getElementById("id_pay_0")){
        document.getElementById("id_pay_0").checked=true;  
    }
})();
$(".alert-del").on('click', function(e) {

  if (confirm("Press Ok to Delete!")){
    console.log("deleted")
  }
  else{
      e.preventDefault();
  }
});