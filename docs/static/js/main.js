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

// MAP

var watchedCountries = {};

$.each(allCountriesWatched, function(iso, country) {
    if (country.count > 0) {
        watchedCountries[iso] = country;
    }
});

var svgMapData = {
    data: {
        count: {
            name: 'Films watched:',
            format: '{0}',
            thousandSeparator: ','
        }
    },
    applyData: 'count',
    values: watchedCountries
};

var watchedMap = new svgMap({
    targetElementID: 'film-world-map',
    data: svgMapData,
    colorMin: '#007733',
    colorMax: '#00E054',
    colorNoData: '#303C44',
    hideFlag: true,
    noDataText: 'No films'
});

var map = document.getElementById('film-world-map');
var svg = map.querySelector('.svgMap-map-image');
var countries = svg.querySelectorAll('.svgMap-country');

function goToCountry(id, openInNewWindow = true) {
    var data = allCountriesWatched[id];
    if (data && data.url) {
        if (typeof YEAR === 'undefined') {
            var url = `https://letterboxd.com/${USERNAME}${data.url}`
        } else {
            var url = `https://letterboxd.com/${USERNAME}/films/diary/for/${YEAR}/country/${data.url.substring(14)}by/rating/`
        }
        if (openInNewWindow) {
            var win = window.open(url , "_blank");
        } else {
            window.location = url;
        }
    }
}

for(var i = 0; i < countries.length; i++) {
    const country = countries[i];

    country.addEventListener('click', function(e) {
        e.preventDefault();
        goToCountry(country.getAttribute('data-id'));	
    });
}

var tooltip = document.querySelector('.svgMap-tooltip');

tooltip.addEventListener('touchstart', function(e) {
    e.preventDefault();
    goToCountry(this.getAttribute('data-id'), false);
});

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