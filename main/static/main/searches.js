if (!document.cookie === "restaurant") {
    document.cookie = "restaurant"
    console.log("Hola")
    console.log(document.cookie)
} else {
    alert(document.cookie)
    console.log("Adios")
}

function selectRestaurant(restaurant) {
    document.cookie = "restaurant=" + restaurant
    console.log("Pasando el valor: " + restaurant)
    document.querySelector("#form_restaurant").value = restaurant
    document.querySelector("#form").submit()
}