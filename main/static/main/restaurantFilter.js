

function changeSlider(vSlice,slider) {
    vSlice.innerHTML = slider.value + "€";
}

function setFilters(cel, veget, vegan,nuts,lactose,filters) {
    let array = [cel,veget,vegan,nuts,lactose]
    console.log(array)
    for(let i=0;i<5;i++){
        filters[i].checked = array[i]
    }
}

function setSlice(max,price,vSlice,slider){
    slider.max = max
    slider.value = price
    changeSlider(vSlice,slider)
}
function start_rest(celiac, vegetarian, vegan, nuts, lactose, max_price, price) {
    let slider = document.getElementsByClassName("slice")[0]
    let filters = document.getElementsByClassName("filter-checkbox")
    let vSlice = document.getElementById("final_price");
    celiac = celiac === "True"
    vegetarian = vegetarian === "True"
    vegan = vegan === "True"
    nuts = nuts === "True"
    lactose = lactose === "True"

    setSlice(max_price,price,vSlice,slider)
    setFilters(celiac,vegetarian,vegan,nuts,lactose,filters)
    slider.addEventListener("mouseup",function(){changeSlider(vSlice,slider)}, false);
}

function submitForm(){
    document.getElementById("myForm").submit();
}