
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

function setFilters(cel, veget, vegan, nuts, lactose) {
    let filters = document.getElementsByClassName("filter-checkbox")
    let array = [cel,veget,vegan, nuts, lactose]

    console.log(array)
    for(let i=0;i<5;i++){
        filters[i].checked = array[i]
    }
}

function start(max, price, location, cel, veget, vegan, nuts, lactose){
    cel = cel === "True"
    veget = veget === "True"
    vegan = vegan === "True"
    nuts = nuts === "True"
    lactose = lactose === "True"
    let slider = document.getElementsByClassName("slider")[0];
    setSlide(max,price,slider)
    setFilters(cel,veget,vegan, nuts, lactose)
    slider.addEventListener("mouseup",function(){changeSlider(slider)}, false);
}

function submitForm(){
    document.getElementById("myForm").submit();
}