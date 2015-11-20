// tamaño del mapa
var width = 700,
    height = 700,
    centered;

// Definimos "svg" como tipo de datos
var svg = d3.select("section").append("svg")
    .attr("width", width)
    .attr("height", height);

svg.append("rect")
    .attr("class", "background")
    .attr("width", width)
    .attr("height", height)
    .on("click", clicked);

// definimos el "path" como as return of geographic features
var path = d3.geo.path()
    .projection(projection);

//agrupa las capas svg
var g = svg.append ("g");

//Tooltip
var tooltip = d3.select("section").append('div')
    .attr('class', 'hidden tooltip');

//Referencia
var color = d3.scale.ordinal()
    .domain(["-49", "-49 a -7", "-7 a -3", "-3 a 1", "-1 a 0", "0", "0 a 3", "3 a 6", "6 a 12", "12 a 20", "20 a 170"])
    .range(["#ca0020", "#dc494b", "#ef9277","#f5c0a9","#f6e4dd", "#ffffff" ,"#e0ebf1","#b3d5e6","#82bbd8","#4396c4","0571b0"]);

var legend = d3.select('svg')
    .append("g")
    .selectAll("g")
    .data(color.domain())
    .enter()
    .append('g')
      .attr('class', 'legend')
      .attr('transform', function(d, i) {
        var height = 20;
        var x = 0;
        var y = i * height;
        return 'translate(' + x + ',' + y + ')';
    });

legend.append('rect')
    .attr('width', 20)
    .attr('height', 20)
    .style('fill', color)
    .style('stroke', color);

legend.append('text')
    .attr('x', 20 + 5)
    .attr('y', 20 - 5)
    .text(function(d) { return d; });


function clicked(d) {
  var x, y, k;

  if (d && centered !== d) {
    var centroid = path.centroid(d);
    x = centroid[0];
    y = centroid[1];
    k = 4;
    centered = d;
  } else {
    x = width / 2;
    y = height / 2;
    k = 1;
    centered = null;
  }

  g.selectAll("path")
      .classed("active", centered && function(d) { return d === centered; });

  g.transition()
      .duration(750)
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
      .style("stroke-width", 1.5 / k + "px");
}

function buscar(){
    tw1 = document.getElementById("tweet1").value;
    tw2 = document.getElementById("tweet2").value;
    camino = "http://localhost:8000/api/request_tweet" +"?tweet1=" +  tw1 +"&tweet2=" +  tw2
    
    d3.json(camino, function(error, topology) {
        debugger
        g.selectAll("path")
        .data(topology.features)
        .enter()
        .append("path")
        .attr("d", path)
        .attr("class",  function(d) {
            var diff = d.properties.varones - d.properties.mujeres;
            if(diff == 0)
                return "path";
            if(diff == -49.0)
                return "cat1";
            if(diff > -49.0 && diff < -7.0)
                return "cat2";
            if(diff >= -7.0 && diff < -3.0)
                return "cat3";
            if(diff >= -3.0 && diff < -1.0)
                return "cat4";
            if(diff == -1.0)
                return "cat5";
            if(diff > -1.0 && diff < 3.0)
                return "cat6";
            if(diff >= 3.0 && diff < 6.0)
                return "cat7";
            if(diff >= 6.0 && diff < 12.0)
                return "cat8";
            if(diff >= 12.0 && diff < 20.0)
                return "cat9";
            if(diff >= 20.0 && diff < 170)
                return "cat10";
        })
        .on('mousemove', function(d) {
            var mouse = d3.mouse(svg.node()).map(function(d) {
                return parseInt(d);
            });
            tooltip.classed('hidden', false)
            .attr('style', 'left:' + (mouse[0] + 15) +
                'px; top:' + (mouse[1] - 35) + 'px')
            .html(
                "<h3>" + d.properties.nombre + "</h3>" +
                "<h6>" + tw1 + ": " + d.properties.varones +"</h6>" +
                "<h6>" + tw2 + ": " + d.properties.mujeres +"</h6>"
                );
        })
        .on('mouseout', function() {
            tooltip.classed('hidden', true);
        })
        .on("click", clicked);
        document.getElementById("title").innerHTML = tw1 + " --VS-- " + tw2;
    });
}

