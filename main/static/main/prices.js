
function changeSlider(slider) {
    let vSlice = document.getElementById("final_price");
    vSlice.innerHTML = slider.value + "€";
}

function setSlide(max,price,slider){
    console.log(max,price)
    slider.max = max
    slider.value = price
    let vSlice = document.getElementById("final_price");
    vSlice.innerHTML = price + "€";
    changeSlider(slider)
}

function setFilters(cel, veget, vegan) {
    let filters = document.getElementsByClassName("filter-checkbox")
    let array = [cel,veget,vegan]
    for(let i=0;i<3;i++){
        filters[i].checked = array[i]
    }
}

function start(max, price, location, cel, veget, vegan){
    cel = cel === "True"
    veget = veget === "True"
    vegan = vegan === "True"
    let slider = document.getElementsByClassName("slider")[0];
    setSlide(max,price,slider)
    setFilters(cel,veget,vegan)
    slider.addEventListener("mouseup",function(){changeSlider(slider)}, false);
}