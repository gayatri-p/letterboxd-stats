var USERNAME = 'binary_bark'

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

// films by year column charts
var filmsByYearChart = {
    chart: {
        type: 'column',
        height: 170,
        width: 847,
        backgroundColor: 'transparent'
    },
    xAxis: {
        categories: bins,
        crosshair: false,
        visible: false
    },
    yAxis: {
        min: 0,
        title: {
            text: ''
        },
        visible: false
    },
    tooltip: {
        headerFormat: '<p style="color:#fff"><b>{point.key}</b><br/>',
        footerFormat: '',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0,
            borderWidth: 0,
            groupPadding: 0,
            shadow: false,
            pointWidth: 10
        }
    },
    
}

var filmsByReleaseYear = jQuery.extend(true, {}, filmsByYearChart, {
    chart: {
        renderTo: 'films-by-release-year-chart'
    },
    tooltip: {
        pointFormat: '{point.y} films</p>',
    },
    series: [{
        name: 'Data',
        data: count,
        showInLegend: false,
        color: '#2AC8BE'
    }]
})

averageRatingByReleaseYear = jQuery.extend(true, {}, filmsByYearChart, {
    chart: {
        renderTo: 'average-rating-by-release-year-chart'
    },
    tooltip: {
        pointFormat: 'Avg {point.y:.2f}</p>',
    },
    series: [{
        name: 'Data',
        data: ratings,
        showInLegend: false,
        color: '#FFFC87'
    }],
})

new Highcharts.chart((filmsByReleaseYear))
new Highcharts.chart((averageRatingByReleaseYear))


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
            name: 'aaa',
            x: -30,
            align: 'left',
            reserveSpace: true,
            formatter: function() {
                return '<a style="color:#fff;font-size:15px" href="https://letterboxd.com/' + 
                        USERNAME + '/films/genre/'+ this.name + '/">' + this.value + '</a>';
            },
            // style: {
            //     color: 'white',
            //     fontSize: 15,
            // },
            useHTML: true
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

var genreChart = jQuery.extend(true, {}, breakdownChart, {
    chart: {
        renderTo: 'films-by-genre'
    },
    xAxis: {
        categories: genre[0],
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
$('#btn-release-year-films').click(function () {
    $('#release-year-films').addClass('-show')
    $('#release-year-films').removeClass('-hide')
    $('#release-year-ratings').addClass('-hide')
    $('#release-year-ratings').removeClass('-show')
    $('#btn-release-year-films').addClass('-active')
    $('#btn-release-year-ratings').removeClass('-active')
})
$('#btn-release-year-ratings').click(function () {
    $('#release-year-ratings').addClass('-show')
    $('#release-year-ratings').removeClass('-hide')
    $('#release-year-films').addClass('-hide')
    $('#release-year-films').removeClass('-show')
    $('#btn-release-year-ratings').addClass('-active')
    $('#btn-release-year-films').removeClass('-active')
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