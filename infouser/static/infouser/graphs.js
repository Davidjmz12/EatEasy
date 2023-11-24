

function renderGraph(ingredients,numbers){
    let miCanvas=document.getElementById("MiGrafica").getContext("2d")
    console.log(miCanvas)
    var dinamicColors = []
    for(var i = 0;i < numbers.length;i++){
        var colorindex= "rgb("+Math.random()*255+","+Math.random()*255+","+Math.random()*255+")"
        dinamicColors.push(colorindex)
    }
    var chart= new Chart(miCanvas, {
        type:"pie",
        data:{
            labels:ingredients,
            datasets:[
                {
                    label:"Mi grafica de ingredientes",
                    borderColor:"rgb(0,0,0)",
                    backgroundColor:dinamicColors,
                    data:numbers
                }
            ]
        }
    })
}