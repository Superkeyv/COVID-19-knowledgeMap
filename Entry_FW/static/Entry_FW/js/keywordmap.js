var myChart = echarts.init(document.getElementById('keywordmap'))

myChart.showLoading();

$.getJSON("http://localhost:8000/keywordrel_data", function (data) {

    myChart.hideLoading();
    var categories = []
    var col_node = [] //记录所有节点，以及入点出点数目

    for (var i = 0; i < 9; i++) {
        categories[i] = {
            name: '类目' + i
        };
    }

    var links = []
    data.forEach(element => {
        s = element['soureNode']
        t = element['targetNode']
        r = element['relationName']

        if (s in col_node) {
            col_node[s] += 1
        } else {
            col_node[s] = 1
        }
        if (t in col_node) {
            col_node[t] += 1
        } else {
            col_node[t] = 1
        }

        //处理links问题
        links.push({
            source: s,
            target: t,
            name: r,
            des: ''
        })
    });

    //处理节点问题
    var node = []
    var i = 0
    for (const key in col_node) {
        if (col_node.hasOwnProperty(key)) {
            const element = col_node[key];
            l_size = 40
            if (element > 200) l_size += 80
            else l_size += element
            node[i++] = {
                name: key,
                des: '',
                symbolSize: l_size,
                category: i % 9,
            }
        }
    }


    option = {
        // 图的标题
        title: {
            text: 'ECharts 关系图'
        },
        // 提示框的配置
        tooltip: {},
        // 工具箱
        // toolbox: {
        //     // 显示工具箱
        //     show: true,
        //     feature: {
        //         mark: {
        //             show: true
        //         },
        //         // 还原
        //         restore: {
        //             show: true
        //         },
        //         // 保存为图片
        //         saveAsImage: {
        //             show: true
        //         }
        //     }
        // },
        legend: [{
            // selectedMode: 'single',
            data: categories.map(function (a) {
                return a.name;
            })
        }],
        animationDuration: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [{
            name: '关键词',
            // 数据
            data: node,
            links: links,
            categories: categories,

            type: 'graph', // 类型:关系图
            layout: 'force', //图的布局，类型为力导图
            symbolSize: 40, // 调整节点的大小
            roam: true, // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移,可以设置成 'scale' 或者 'move'。设置成 true 为都开启

            //stype2
            label: {
                position: 'right',
                formatter: '{b}'
            },
            lineStyle: {
                color: 'source',
                curveness: 0.3
            },
            circular: {
                rotateLabel: true
            },
            force: {
                repulsion: 100
            }

            //style1
            // edgeSymbol: ['circle', 'arrow'],
            // edgeSymbolSize: [2, 10],
            // edgeLabel: {
            //     normal: {
            //         textStyle: {
            //             fontSize: 20
            //         }
            //     }
            // },
            // force: {
            //     repulsion: 2500,
            //     edgeLength: [10, 50]
            // },
            // draggable: true,
            // lineStyle: {
            //     normal: {
            //         width: 2,
            //         color: '#4b565b',
            //     }
            // },
            // edgeLabel: {
            //     normal: {
            //         show: true,
            //         formatter: function (x) {
            //             return x.data.name;
            //         }
            //     }
            // },
            // label: {
            //     normal: {
            //         show: true,
            //         textStyle: {}
            //     }
            // },

        }]
    };

    myChart.setOption(option);

});