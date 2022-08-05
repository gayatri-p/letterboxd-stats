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
            borderRadius: 3,
            groupPadding: 0,
            shadow: false,
            pointWidth: 10,
            point: {
                events: {
                    click: function () {
                        window.open(
                            `https://letterboxd.com/${USERNAME}/films/year/${this.category}`);
                    }
                }
            }
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