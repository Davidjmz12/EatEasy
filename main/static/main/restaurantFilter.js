

function changeSlider(vSlice,slider) {
    vSlice.innerHTML = slider.value + "€";
}

function setFilters(cel, veget, vegan,filters) {
    let array = [cel,veget,vegan]
    for(let i=0;i<3;i++){
        filters[i].checked = array[i]
    }
}

function setSlice(max,price,vSlice,slider){
    slider.max = max
    slider.value = price
    changeSlider(vSlice,slider)
}
function start_rest(celiac, vegetarian, vegan, max_price, price) {
    let slider = document.getElementsByClassName("slice")[0]
    let filters = document.getElementsByClassName("filter-checkbox")
    let vSlice = document.getElementById("final_price");
    celiac = celiac === "True"
    vegetarian = vegetarian === "True"
    vegan = vegan === "True"
    setSlice(max_price,price,vSlice,slider)
    setFilters(celiac,vegetarian,vegan,filters)
    slider.addEventListener("mouseup",function(){changeSlider(vSlice,slider)}, false);
}