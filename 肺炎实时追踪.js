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


$.ajax({
    url: "data.json",//json文件位置
    // type: "post",
    dataType: "json", //返回数据格式为json
    success: function(data) {//请求成功完成后要执行的方法
        console.log(data)
    }
})

// $(function (){
//     $("#btn").click(function ()  {
//       $.getJSON("js/userinfo.json", function (data){
//         var $jsontip = $("#jsonTip");
//         var strHtml = "123";
//         //存储数据的变量
//         $jsontip.empty();
//         //清空内容
//         $.each(data, function (infoIndex, info){
//           strHtml += "姓名：" + info["name"] + "<br>";
//           strHtml += "性别：" + info["sex"] + "<br>";
//           strHtml += "邮箱：" + info["email"] + "<br>";
//           strHtml += "<hr>"
//         })
  
//         $jsontip.html(strHtml);
//         //显示处理后的数据
//       })
//     })
//   })
