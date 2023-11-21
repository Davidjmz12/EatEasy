
function changeSlider(slider) {
    let vSlice = document.getElementById("final_price");
    vSlice.innerHTML = slider.value + "€";
}

function setSlide(max,slider){
    console.log(max)
    slider.max = max
    slider.value = max
    changeSlider(slider)
}

function setFilters(cel, veget, vegan) {
    let filters = document.getElementsByClassName("filter-checkbox")

    let array = [cel,veget,vegan]
    for(let i=0;i<3;i++){
        filters[i].checked = array[i]
    }
}

function start(max, location, cel, veget, vegan){
    cel = cel === "True"
    veget = veget === "True"
    vegan = vegan === "True"
    console.log(max)
    let slider = document.getElementsByClassName("slider")[0];
    setSlide(max,slider)
    setFilters(cel,veget,vegan)
    slider.addEventListener("mouseup",function(){changeSlider(slider)}, false);
}