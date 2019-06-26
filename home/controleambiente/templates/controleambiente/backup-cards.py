{% load staticfiles %}


<!DOCTYPE html>
<html>
<head>

<link rel="apple-touch-icon" sizes="57x57" href="{% static "img/favicon/apple-icon-57x57.png" %}">
<link rel="apple-touch-icon" sizes="60x60" href="{% static "img/favicon/apple-icon-60x60.png" %}">
<link rel="apple-touch-icon" sizes="72x72" href="{% static "img/favicon/apple-icon-72x72.png" %}">
<link rel="apple-touch-icon" sizes="76x76" href="{% static "img/favicon/apple-icon-76x76.png" %}">
<link rel="apple-touch-icon" sizes="114x114" href="{% static "img/favicon/apple-icon-114x114.png" %}">
<link rel="apple-touch-icon" sizes="120x120" href="{% static "img/favicon/apple-icon-120x120.png" %}">
<link rel="apple-touch-icon" sizes="144x144" href="{% static "img/favicon/apple-icon-144x144.png" %}">
<link rel="apple-touch-icon" sizes="152x152" href="{% static "img/favicon/apple-icon-152x152.png" %}">
<link rel="apple-touch-icon" sizes="180x180" href="{% static "img/favicon/apple-icon-180x180.png" %}">
<link rel="icon" type="image/png" sizes="192x192"  href="{% static "img/favicon/android-icon-192x192.png" %}">
<link rel="icon" type="image/png" sizes="32x32" href="{% static "img/favicon/favicon-32x32.png" %}">
<link rel="icon" type="image/png" sizes="96x96" href="{% static "img/favicon/favicon-96x96.png" %}">
<link rel="icon" type="image/png" sizes="16x16" href="{% static "img/favicon/favicon-16x16.png" %}">
<link rel="manifest" href="{% static "img/favicon/manifest.json" %}">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="msapplication-TileImage" content="{% static "img/ms-icon-144x144.png" %}">
<meta name="theme-color" content="#ffffff">

<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Gamja+Flower" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet">

<link href="{% static "css/weather-icons.min.css" %}" rel="stylesheet" media="screen">

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

    <style>
      .col-sm-3 {
        font-family: 'Open Sans Condensed', sans-serif;
        font-size: 30px;
        display: inline-block
        
      }
      .rowj {

        display: inline-block
        
      }
      
          
          
          html, body {
    height:100%;
} 

body {
    background-color: white;
    background-image: url('http://www.canvaz.com/portrait/charcoal-1.jpg');
    background-size: auto 100%;
    background-repeat: no-repeat;
    background-position: left top;
}
          
      .texto{
        font-family: 'Pacifico', cursive;
        font-size: 30px;
        display: inline-block  
          }
      .info  {
          font-family: 'Open Sans Condensed', sans-serif;
          font-size: 20px;
          color: #AAAAAA
          }
      .jumbotron {
        font-family: 'Gamja Flower', cursive;
        background-color: #2196F3;
        color: #000000;
        vertical-align: baseline;
        
      }
    </style>

<script>

//var ambientes = JSON.parse({{ambientes|safe}})
//var ambiente1 = JSON.parse({{ambiente1|safe}})
var ambienteN20 = JSON.parse({{ambienteN20|safe}})


//################ valores atuais ##########################
function inicializacao(){

    var lvetor =-1
    var agora = ''
    lvetor = ambienteN20.length
    agora = ambienteN20[0].fields.data

    $('#horaagora').html(agora)
    
    console.log(ambienteN20)
}

window.onload=inicializacao;
var maxl = 0
var minl = 100
var lvetor =-1
var agora = ''
lvetor = ambienteN20.length
var l = []


var sen1 = []
var sen2 = []


for (i in ambienteN20){
    
    if (ambienteN20[i].fields.local == 0){
        var elem = {}
        elem.temp = ambienteN20[i].fields.temperatura
        elem.data = ambienteN20[i].fields.data
        sen1.push([elem.data, parseFloat(elem.temp)])

    }
    
    if (ambienteN20[i].fields.local == 1){
        var elem = {}
        elem.temp = ambienteN20[i].fields.temperatura
        elem.data = ambienteN20[i].fields.data
        sen2.push([elem.data, parseFloat(elem.temp)])
    }
}

console.log(sen1)
console.log(sen2)
maxl = 25
minl = 20

//for (aux in ambienteN20){
//    if (ambienteN20[lvetor-1-aux].fields.local == 0){
//        var elem = {}
//        elem.temp = ambienteN20[lvetor-1-aux].fields.temperatura
//        elem.data = ambienteN20[lvetor-1-aux].fields.data
//        l[aux] = [elem.data, parseFloat(elem.temp)]
        
//            if (maxl < parseFloat(elem.temp)){
//                maxl = parseFloat(elem.temp)+1.0
//            }
//            if (minl > parseFloat(elem.temp)){
//                minl = parseFloat(elem.temp)-1.0
//            }    
    
//    }else{
//        var elem = {}
//    }
    
//    }
console.log(l)
//###################### charts #########
      google.charts.load('current', {'packages':['line']});
      google.charts.setOnLoadCallback(drawChart);
      
     function drawChart() {

      var data = new google.visualization.DataTable();
      var data2 = new google.visualization.DataTable();
      
      data.addColumn('string', 'data');
      data.addColumn('number', 'temp.');
      
      data2.addColumn('string', 'data');
      data2.addColumn('number', 'temp.');
      
      data.addRows(sen1);
      data2.addRows(sen2);
      //data.addRows([
        //[1,  37.8],
        //[2,  30.9],
      //]);

      var options = {
          curveType:'function',
        chart: {
          title: '',
          subtitle: ''
          
        },
        legend: {position: 'bottom', textStyle: {color: 'pink', fontSize: 10}},
        width: 400,
        height: 200,
        
        axes: {
            y: {
                all: {
                    range: {
                        max: maxl,
                        min: minl
                    }
                }
            }
        },
      };

      var chart = new google.charts.Line(document.getElementById('line_top_x'));
      //var chart2 = new google.charts.Line(document.getElementById('line_top_x2'));
      
      chart.draw(data, google.charts.Line.convertOptions(options));
      //chart2.draw(data2, google.charts.Line.convertOptions(options));
    }
     
</script>

<title>Pessoal</title>

</head>
<body>




<!- div para colocar backgroud ########################### ->
<div class="container-fluid full">

      
      <div class="container-fluid">
	<div class="row">
		<div class="col-md-6">
			<div class="card bg-default">
				<h5 class="card-header">
					<div class="row texto">
                                          <img src="{% static "img/tete.png" %}" class="rounded-circle" alt="Maria" height="40px">
                                          <span class="align-bottom">Maria Antonia</span>
                                        </div>
                                </h5>  
				<div class="card-body">
                                    <div class="row info text-center">
                                    <div class="col-md-6 text-center>
                                    <!- quadro ########################### ->
                                                <div id="container" style="white-space:nowrap">
                                                    <div id="image" style="display:inline;">
                                                        <i class="wi wi-thermometer"></i>
                                                    </div>

                                                    <div id="texts" style="display:inline; white-space:nowrap;"> 
                                                         {{temp1}}˚C 
                                                    </div>
                                                </div>​
				    <!- fim quadro ###########################
				    </div>
				    <div class="col-md-6 text-center>
                                    <!- quadro ########################### ->
                                                <div id="container" style="white-space:nowrap">
                                                    <div id="image" style="display:inline;">
                                                        <i class="wi wi-humidity"></i>
                                                    </div>

                                                    <div id="texts" style="display:inline; white-space:nowrap;"> 
                                                          {{umid1}}% 
                                                    </div>
                                                </div>​
				    <!- fim quadro ###########################
				    </div>
					<p class="card-text">
				</div>
					</p>
					<div id="line_top_x"></div>
				</div>
				<div class="card-footer">
					Card footer
				</div>
			</div>
		</div>
		
		<!- zep ########################### ->
		
		

	    
<div class"text" id="horaagora">
<p> ultima atualizacao </p>
</div>

</body>
</html> 




