let chart;


// traffic prediction
async function predictTraffic(){

let vehicles = document.getElementById("vehicles").value;

const response = await fetch("http://127.0.0.1:5000/predict_traffic",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({vehicles:vehicles})
})

const data = await response.json();

document.getElementById("result").innerText =
"Predicted congestion: " + data.predicted_congestion;

loadForecast(vehicles)

}


// forecast future congestion
async function loadForecast(v){

const response = await fetch("http://127.0.0.1:5000/forecast",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({vehicles:v})
})

const data = await response.json()

document.getElementById("forecast").innerText =
"Future congestion prediction: " + data.future_congestion

}


// load dataset graph
async function loadTrafficStats(){

const response = await fetch("http://127.0.0.1:5000/traffic_stats")

const data = await response.json()

const ctx = document.getElementById("trafficChart")

chart = new Chart(ctx,{
type:"line",
data:{
labels:data.vehicles,
datasets:[{
label:"Traffic Congestion",
data:data.congestion,
borderColor:"blue",
backgroundColor:"lightblue",
fill:true,
tension:0.3
}]
}
})

}

loadTrafficStats()


// map
var map = L.map('map').setView([17.3850,78.4867],12)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
maxZoom:19
}).addTo(map)


// heatmap data
var heatData = [
[17.3850,78.4867,0.9],
[17.4010,78.4890,0.7],
[17.3713,78.4804,0.8],
[17.4474,78.3762,0.6],
[17.4399,78.4983,0.75],
[17.4500,78.3900,0.85]
]

var heat = L.heatLayer(heatData,{
radius:25,
blur:15,
maxZoom:17
}).addTo(map)