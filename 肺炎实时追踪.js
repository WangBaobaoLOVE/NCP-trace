var divPro = document.getElementById("divProId");
divProNodeList = divPro.querySelectorAll("a");
var proMapIfram = document.getElementById("proMapIframId");

var proName = divProNodeList[11];
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


$.getJSON("./data.json", function(data){
    var interColumnChinaDataHtml="";
    var interColumnWorldDataHtml="";

    $.each(data["areaTree"][0]["children"], function(infoIndex, info){

        interColumnChinaDataHtml += "<div class='dataColumn'>" 
        + "<div class='city'>  <a>" + info["name"] + "</a></div>"
        + "<div class='confirm'><a>" + info["total"]["confirm"] + "</a></div>"
        + "<div class='suspect'><a>" + info["total"]["suspect"] + "</a></div>"
        + "<div class='suspect'><a>" + info["total"]["dead"] + "</a></div>"
        + "<div class='confirm'><a>" + info["total"]["heal"] + "</a></div>"
        + "</div>"
    
    })
    $("#dataColumnChinaData").append(interColumnChinaDataHtml);

    $.each(data["areaTree"], function(infoIndex, info){

        interColumnWorldDataHtml += "<div class='dataColumn'>" 
        + "<div class='city'>  <a>" + info["name"] + "</a></div>"
        + "<div class='confirm'><a>" + info["total"]["confirm"] + "</a></div>"
        + "<div class='suspect'><a>" + info["total"]["suspect"] + "</a></div>"
        + "<div class='suspect'><a>" + info["total"]["dead"] + "</a></div>"
        + "<div class='confirm'><a>" + info["total"]["heal"] + "</a></div>"
        + "</div>"
    
    })
    $("#dataColumnWorldData").append(interColumnWorldDataHtml);

})

