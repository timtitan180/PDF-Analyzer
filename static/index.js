//get buttons idenity
//add an event listener to that button
button = document.getElementById(".button")
button.addEventListener("click",showGif)

//async function(){
//    await Promise(){
//        fetch("https:localhost:4210/").then(response=>{console.log(response.statusCode)})
//    }
//]
//}

    function showGif(){
    document.querySelector("loadingImg").style.visibility = "visible"
    setTimeout(function(){
        document.querySelector("loadingImg").style.visibility = "hidden"
    },1000)
}