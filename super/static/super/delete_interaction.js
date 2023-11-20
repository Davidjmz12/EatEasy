function changeButton() {
    let items = document.getElementsByClassName("delete_ing")
    let submit = document.getElementById("submit_ing")
    if(Array.prototype.slice.call(items).some((item)=> item.checked)){
        submit.style.display="block"
    }
    else{
        submit.style.display="none"
    }
}

function createListeners(){
    let items = document.getElementsByClassName("delete_ing")
    for(let i=0; i<items.length; i++){
        items[i].addEventListener("click",changeButton,false);
    }
}

createListeners()