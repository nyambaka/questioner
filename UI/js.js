
function tagglenavigation(){
    let set_class=document.getElementById("question-header").getAttribute("class");
    if (set_class == "hidden"){
      document.getElementById("question-header").setAttribute("class","visible");
       document.getElementById("comment-header").setAttribute("class","hidden");
    }
    if (set_class == "visible") {
        document.getElementById("comment-header").setAttribute("class","visible");
        document.getElementById("question-header").setAttribute("class","hidden");
    }

}


