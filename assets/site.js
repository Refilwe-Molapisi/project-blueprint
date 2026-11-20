
(function(){
  // Mobile menu
  var t=document.querySelector(".menu-toggle"),nav=document.querySelector("nav.main");
  if(t&&nav){t.addEventListener("click",function(){
    var open=nav.classList.toggle("open");
    t.setAttribute("aria-expanded",open?"true":"false");})}
  // Dropdown (works on touch via <details>)
  document.querySelectorAll("details.dropdown").forEach(function(d){
    d.addEventListener("click",function(e){
      if(d.open&&e.target.closest("a"))d.removeAttribute("open");});
    document.addEventListener("click",function(e){
      if(d.open&&!d.contains(e.target))d.removeAttribute("open");});});
  // Year stamp
  document.querySelectorAll("[data-year]").forEach(function(el){
    el.textContent=new Date().getFullYear();});
  // Scroll reveal
  if("IntersectionObserver" in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(en){if(en.isIntersecting){en.target.classList.add("in");io.unobserve(en.target);}});
    },{threshold:.12});
    document.querySelectorAll(".rise").forEach(function(el){io.observe(el);});
  }else{document.querySelectorAll(".rise").forEach(function(el){el.classList.add("in");});}
  // Enquiry form validation
  var form=document.querySelector("form.enquiry");
  if(form){
    var summary=form.querySelector(".error-summary");
    var confirm=form.querySelector(".confirm");
    function need(el,msg){
      var f=el.closest(".field")||el.closest("fieldset");
      if(!f)return true;
      var m=f.querySelector(".msg");
      var bad=!el.value||(el.type==="checkbox"&&!el.checked)||
        (el.tagName==="SELECT"&&!el.value);
      f.classList.toggle("err",bad);
      if(m&&bad)m.textContent=msg||"This field is required.";
      return !bad;
    }
    form.addEventListener("submit",function(e){
      e.preventDefault();
      var ok=true,first=null;
      form.querySelectorAll("[data-req]").forEach(function(el){
        var good=need(el);
        if(!good){ok=false;first=first||el;}
      });
      var email=form.querySelector("input[type=email]");
      if(email&&email.value&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)){
        var f=email.closest(".field");f.classList.add("err");
        var m=f.querySelector(".msg");if(m)m.textContent="Please enter a valid email address.";
        ok=false;first=first||email;
      }
      if(summary){summary.classList.toggle("show",!ok);
        if(!ok&&first){first.focus();return;}}
      if(ok){form.style.display="none";if(confirm){confirm.classList.add("show");
        confirm.scrollIntoView({behavior:"smooth",block:"center"});}}
    });
  }
  // Portal stub forms
  var stub=document.querySelector("form.portal-stub");
  if(stub){stub.addEventListener("submit",function(e){
    e.preventDefault();
    var n=stub.querySelector(".portal-note");
    if(n)n.style.display="block";});}
})();
