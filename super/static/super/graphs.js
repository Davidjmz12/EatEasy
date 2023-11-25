

function renderGraph(ingredients,numbers, type){
    let miCanvas=document.getElementById("MiGrafica").getContext("2d")
    let dinamicColors = []
    for(var i = 0;i < numbers.length;i++){
        var colorindex= "rgb("+Math.random()*255+","+Math.random()*255+","+Math.random()*255+")"
        dinamicColors.push(colorindex)
    }

    let typeGraph,label, backgroundColors

    if(type==="filter"){
        typeGraph = "pie"
        label = "Types of food graph"
        backgroundColors = dinamicColors
    } else if(type === "price") {
        typeGraph = "bar"
        label =  "Price Occurrences"
        backgroundColors = "rgb("+Math.random()*255+","+Math.random()*255+","+Math.random()*255+")"
    } else if(type === "ingredients") {
        typeGraph = "bar"
        label =  "Ingredients Occurrences"
        backgroundColors = "rgb("+Math.random()*255+","+Math.random()*255+","+Math.random()*255+")"
    } else if (type === "city") {
        typeGraph = "pie"
        label =  "City graph"
        backgroundColors = dinamicColors
    }

    let chart= new Chart(miCanvas, {
        type:typeGraph,
        data:{
            labels:ingredients,
            datasets:[
                {
                    label:label,
                    borderColor:"rgb(0,0,0)",
                    backgroundColor:backgroundColors,
                    data:numbers
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        precision: 0,
                    }
                }]
            }
        }

    })
}
