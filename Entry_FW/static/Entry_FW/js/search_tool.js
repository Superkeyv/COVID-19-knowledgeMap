
// search_tip = document.getElementById("search-tip");

// mode = ""

//将搜索提示数据导入到页面中
function html_wrapper(params) {
    s1 = "<nav class='navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow' id='search-tip'>"
    s2 = '</nav>';
    
    search_tip.innerHTML = s1 + params + s2
}




// $(".check_class").click(function (e) {
//     e.preventDefault();

//     console.log("btn-类别查询")
//     x = "<div class='text-ceter'>可选的doc class包括：\n"
//         + "A:有机体； B:解剖学； C:疾病; D:化学药物；"
//         + "E:分析，诊断和治疗技术与设备； F:现象与过程"
//         + "</div>"
//     html_wrapper(x)
//     mode = "check_class"
// });


// $(".check_entry").click(function (e) {
//     e.preventDefault();

//     console.log("btn-实体查询")

//     $.ajax({
//         type: "GET",
//         url: "/keywordrel_data",
//         success: function (response) {

//             nodes_keys = Object.keys(response)
//             x = "<div class='text-ceter'>\n"
//             x+="可选的"

//             for (tmp in nodes_keys) {
//                 x += tmp
//             }

//             x += "</div>"

//             html_wrapper(x)

//             mode = "check_entry"
//         }
//     });
// });


$(".search_btn").click(function (e) { 
    e.preventDefault();
    
    console.log("搜索按钮按下")

    info=document.getElementById("search_input").value;
    
    request_param={
        "mode":mode,
        "info":info
    }

    $.ajax({
        type: "POST",
        url: "/request_doclist",
        data: "data",
        success: function (response) {
            console.log("Service response!!!准备处理数据生成表格")



        }
    });

});
