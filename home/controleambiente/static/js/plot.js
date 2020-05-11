console.log("testeeeeeeee")


//################ valores atuais ##########################
function inicializacao(){

    var lvetor =-1
    var agora = ''
    lvetor = ambiente.length
    agora = ambiente[0].fields.data
    console.log(agora, " ultimo dado")
    var tempN = ambiente[0].fields.temperatura
    var tempM = ambiente[1].fields.temperatura
    console.log(tempN, " ultimo dado")
    console.log((parseFloat(tempN)).toFixed(1))
    $('#horaagora').html(agora)
//console.log('---------')
  //  console.log(arcond)

    console.log(lvetor)
    
     
var curva1 = []
var curva2 = []
var auxY = []
var auxYY = []

var i = 0;


for (i in ambiente){
        
    if (ambiente[i].fields.local == 1){   
        curva1.push(ambiente[i].fields.temperatura)
        auxY.push(ambiente[i].fields.data) 
        var tempN = ambiente[i].fields.temperatura

    }
    if (ambiente[i].fields.local == 0){   
        curva2.push(ambiente[i].fields.temperatura) 
        auxYY.push(ambiente[i].fields.data)  
        var tempM = ambiente[i].fields.temperatura
    }

}

$('#tempn').html(parseFloat(tempN).toFixed(1) + "˚C")
$('#tempm').html(parseFloat(tempM).toFixed(1) + "˚C")


var trace1 = {
  x: auxY,
  y: curva1,
  line: {
      shape: 'linear',
      color: 'rgb(255,192,203)',
      width: 3,
      },
  mode: 'lines',
};

var trace2 = {
  x: auxYY,
  y: curva2,
  line: {
      shape: 'linear',
      color: '#537686',
      width: 3,
      },
  mode: 'lines',
};


var data = [ trace1, trace2, ];

var layout = {
  title:'Temperatura',
  showlegend: false,
  margin: {
    autoexpand: false,
    l: 30,
    r: 20,
    t: 40,
    b: 30
  },
  xaxis: {
    showgrid: false,
    zeroline: false,
    showline: false,
    showticklabels: true,
    
  },
  yaxis: {
    
    autorange: true,
    
      },
  font:{
        family: 'Open Sans Condensed',
        size: 12,
        color: 'rgb(220,220,220)'
      },
  paper_bgcolor:'rgba(0,0,0,0)',
  plot_bgcolor:'rgba(0,0,0,0)',
  
};

Plotly.newPlot('myDiv', data, layout);
       

}

window.onload=inicializacao;