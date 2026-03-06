var pieChart = {
    chart: {
        type: 'pie',
        height: 200,
        width: 200
    },
    plotOptions: {
        pie: {
            allowPointSelect: false,
            dataLabels: {
                enabled: false,
            },
            // enableMouseTracking: false,
            borderWidth: 0,
            states: {
                hover: {
                    enabled: false
                },
                inactive: {
                    opacity: 1,
                },
            }
        }
    },
    tooltip: {
        useHTML: true,
        headerFormat: '<p style="color:#fff;text-align:center;margin:0;font-size:12px;">',
        pointFormat: '{point.percentage:.1f}% ' +
            '<span style="color:#9ab;">({point.y} of ' + diary_entries + ')</span>',
        footerFormat: '</p>',
    }
}

var pieReleaseDates = {
    chart: {
        renderTo: 'pie-release-dates'
    },
    series: [{
        name: 'films',
        colorByPoint: true,
        data: [{
            name: 'current_year',
            y: releases_this_year,
            color: '#00e054'
        }, {
            name: 'older',
            color: '#445566',
            y: older_releases
        }]
    }]
}

var pieRewatches = {
    chart: {
        renderTo: 'pie-rewatches'
    },
    series: [{
        name: 'films',
        colorByPoint: true,
        data: [{
            name: 'rewatches',
            y: rewatches,
            color: '#445566'
        }, {
            name: 'watches',
            color: '#00e054',
            y: new_watches
        }]
    }]
}

pieReleaseDatesChart = jQuery.extend(true, {}, pieChart, pieReleaseDates);
pieRewatchesChart = jQuery.extend(true, {}, pieChart, pieRewatches);

new Highcharts.chart(pieReleaseDatesChart)
new Highcharts.chart(pieRewatchesChart)

// films by week

var days = {
    1: 'M',
    2: 'T',
    3: 'W',
    4: 'T',
    5: 'F',
    6: 'S',
    7: 'S'
}

chartByWeek = {
    chart: {
        renderTo: 'chart-films-by-week',
        type: 'column',
        height: 170,
        width: 900,
    },
    xAxis: {
        categories: Object.keys(filmsByWeek),
        crosshair: false,
        visible: false
    },
    yAxis: {
        min: 0,
        visible: false
    },
    tooltip: {
        headerFormat: '<p style="margin: 0; padding: 5px 7px 0; color: #9AB; font-size: 11px; text-align: center;">',
        pointFormat: '<strong style="color: #fff; font-weight: normal; font-size: 16px;">{point.y} films</strong>',
        footerFormat: '<br>Week {point.key}</p>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0,
            borderWidth: 0,
            groupPadding: 0,
            pointWidth: 15,
            borderRadius: 3,
            point: {
                events: {
                    click: function () {
                        window.open(
                            `https://letterboxd.com/${USERNAME}/films/diary/for/${YEAR}/week/${this.category}`);
                    }
                }
            }
        }
    },
    series: [{
        name: 'Data',
        data: Object.values(filmsByWeek),
        showInLegend: false,
        color: '#2AC8BE',
    }],
};

chartByWeekday = {
    chart: {
        renderTo: 'chart-films-by-weekday',
        type: 'column',
        height: 170,
        width: 231,
    },
    xAxis: {
        categories: Object.keys(filmsByWeekDay),
        crosshair: false,
        visible: true,
        lineWidth: 0,
        labels: {
            formatter: function () {
                return days[this.value];
            },
            style: {
                fontSize: '14px',
                color: 'white'
            }
        },

    },
    yAxis: {
        min: 0,
        visible: false
    },
    tooltip: {
        headerFormat: '<p>',
        pointFormat: '<strong style="color: #fff; font-weight: normal; font-size: 16px;">{point.y} films</strong>',
        footerFormat: '</p>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0,
            borderWidth: 0,
            groupPadding: 0,
            pointWidth: 27,
            borderRadius: 3,
        }
    },
    series: [{
        name: 'Data',
        data: Object.values(filmsByWeekDay),
        showInLegend: false,
        color: '#445566',
        states: {
            hover: {
                color: '#00E054',
            }
        },
    }],
}

// console.log(Object.values(filmsByWeek))
new Highcharts.chart(chartByWeek)
new Highcharts.chart(chartByWeekday)


// button event handlers

$('#btn-highest-rated-films').click(function () {
    $('#highest-rated-films-older').addClass('-hide')
    $('#highest-rated-films-older').removeClass('-show')
    $('#highest-rated-films').addClass('-show')
    $('#highest-rated-films').removeClass('-hide')
    $('#btn-highest-rated-films').addClass('-active')
    $('#btn-highest-rated-films-older').removeClass('-active')
})
$('#btn-highest-rated-films-older').click(function () {
    $('#highest-rated-films').addClass('-hide')
    $('#highest-rated-films').removeClass('-show')
    $('#highest-rated-films-older').addClass('-show')
    $('#highest-rated-films-older').removeClass('-hide')
    $('#btn-highest-rated-films-older').addClass('-active')
    $('#btn-highest-rated-films').removeClass('-active')
})