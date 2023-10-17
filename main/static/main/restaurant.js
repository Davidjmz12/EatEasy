function toggleContent(ind){
    let content = document.getElementsByClassName("one-dish-long")[ind]
    let contentShort= document.getElementsByClassName("one-dish-short")[ind]
    if (content.style.display === "none") {
        content.style.display = "";
        contentShort.style.display = "none";
    } else {
        content.style.display = "none";
        contentShort.style.display = ""
    }
}