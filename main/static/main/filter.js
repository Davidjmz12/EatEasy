function changeSlider() {
    let slider = document.getElementsByClassName("slice")[0];
    let vSlice = document.getElementById("slider-value");
    vSlice.innerHTML = slider.value;
}


/*
function makeFiltersListeners(){
    let filters = document.getElementsByClassName("filter-checkbox")
    for(let i=0; i<filters.length; i++){
        filters[i].addEventListener("click", function () {
            watching(filters[i],i);
        },false,);
    }

    slider.addEventListener("mouseup",function(){changeSlider(slider)}, false);
}

document.addEventListener("DOMContentLoaded", makeFiltersListeners, false);

*/
