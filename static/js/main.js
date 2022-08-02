// highcharts global settings
Highcharts.setOptions({
    chart: {
        backgroundColor: 'transparent'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    plotOptions: {
        series: {
            animation: false
        }
    },
    exporting: {
        buttons: {
            contextButton: {
                enabled: false
            }
        }
    },
    credits: {
        enabled: false
    }
})

// breakdown charts
var breakdownChart = {
    chart: {
        type: 'bar',
        height: 294,
        width: 300,
    },
    xAxis: {
        lineWidth: 0,
        labels: {
            x: -30,
            align: 'left',
            reserveSpace: true,
            useHTML: true,
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: ''
        },
        visible: false
    },
    tooltip: {
        headerFormat: '',
        pointFormat: '<span style="color:#fff">{point.y} films</span>',
        footerFormat: '',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        series: {
            groupPadding: 0,
            pointPadding: 0.1,
            borderWidth: 0,
            borderRadius: 5
        }
    },
}

function breakdownChartLink(category, value) {
    return '<a style="color:#fff;font-size:15px;text-transform:capitalize" href="https://letterboxd.com/' +
        USERNAME + '/films/' + category + '/' + value.toLowerCase() + '/">' + value + '</a>'
}

var genreChart = jQuery.extend(true, {}, breakdownChart, {
    chart: {
        renderTo: 'films-by-genre'
    },
    xAxis: {
        categories: genre[0],
        labels: {
            formatter: function () {
                return breakdownChartLink('genre', this.value)
            },
        },
    },
    series: [{
        name: 'Data2',
        data: genre[1],
        showInLegend: false,
        color: '#00e054'
    }]
});

var countryChart = jQuery.extend(true, {}, breakdownChart, {
    chart: {
        renderTo: 'films-by-country'
    },
    xAxis: {
        categories: country[0],
        labels: {
            formatter: function () {
                return breakdownChartLink('country', this.value)
            },
        },
    },
    series: [{
        name: 'Data2',
        data: country[1],
        showInLegend: false,
        color: '#2AC8BE'
    }]
});

var languageChart = jQuery.extend(true, {}, breakdownChart, {
    chart: {
        renderTo: 'films-by-language'
    },
    xAxis: {
        categories: language[0],
        labels: {
            formatter: function () {
                return breakdownChartLink('language', this.value)
            },
        },
    },
    series: [{
        name: 'Data2',
        data: language[1],
        showInLegend: false,
        color: '#ff8000'
    }]
});

new Highcharts.chart((genreChart))
new Highcharts.chart((countryChart))
new Highcharts.chart((languageChart))



// button event handlers

$('#open-yir-menu').click(function() {
    $('#yir-menu').addClass('-show')
    $('#yir-menu').removeClass('-hide')

})

$('#btn-most-watched-actors').click(function () {
    $('#actors-by-rating').addClass('-hide')
    $('#actors-by-rating').removeClass('-show')
    $('#actors-most-watched').addClass('-show')
    $('#actors-most-watched').removeClass('-hide')
    $('#btn-most-watched-actors').addClass('-active')
    $('#btn-highest-rated-actors').removeClass('-active')
})
$('#btn-highest-rated-actors').click(function () {
    $('#actors-most-watched').addClass('-hide')
    $('#actors-most-watched').removeClass('-show')
    $('#actors-by-rating').addClass('-show')
    $('#actors-by-rating').removeClass('-hide')
    $('#btn-highest-rated-actors').addClass('-active')
    $('#btn-most-watched-actors').removeClass('-active')
})
$('#btn-directors-most-watched').click(function () {
    $('#directors-by-rating').addClass('-hide')
    $('#directors-by-rating').removeClass('-show')
    $('#directors-most-watched').addClass('-show')
    $('#directors-most-watched').removeClass('-hide')
    $('#btn-directors-most-watched').addClass('-active')
    $('#btn-directors-by-rating').removeClass('-active')
})
$('#btn-directors-by-rating').click(function () {
    $('#directors-most-watched').addClass('-hide')
    $('#directors-most-watched').removeClass('-show')
    $('#directors-by-rating').addClass('-show')
    $('#directors-by-rating').removeClass('-hide')
    $('#btn-directors-by-rating').addClass('-active')
    $('#btn-directors-most-watched').removeClass('-active')
})