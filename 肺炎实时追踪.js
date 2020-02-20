var divPro = document.getElementById("divProId");
divProNodeList = divPro.querySelectorAll("a");
var proMapIfram = document.getElementById("proMapIframId");

var proName = divProNodeList[10];
proName.style.backgroundColor = "red";

for(var i=0; i<divProNodeList.length; i++){
    divProNodeList[i].onmouseover = function (){
        this.style.backgroundColor = "lime";
    }

    divProNodeList[i].onmouseleave = function (){
        this.style.backgroundColor = "#FFCCCC";
        proName.style.backgroundColor = "red";
    }

    divProNodeList[i].onmousedown = function (){
        proMapIfram.src = "./pages/"+this.textContent+"疫情地图.html";
        proName.style.backgroundColor = "#FFCCCC";
        this.style.backgroundColor = "red";
        proName = this;
    }
}
