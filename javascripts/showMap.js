// tamaño del mapa
var width = 500,
    height = 800;

// Ajustes de proyección para mercator
var projection = d3.geo.mercator()
  // centro del mapa en grados
  .center([-50, -35])
  // zoomlevel
  .scale(800)
  // map-rotation
  .rotate([0,0]);

// Definimos "svg" como tipo de datos
var svg = d3.select("section").append("svg")
    .attr("width", width)
    .attr("height", height);

// definimos el "path" como as return of geographic features
var path = d3.geo.path()
    .projection(projection);

//agrupa las capas svg
var g = svg.append ("g");

//Tooltip
var tooltip = d3.select("section").append('div')
    .attr('class', 'hidden tooltip');

// Carga de datos y visualización del mapa en el canvas
d3.json("tweets.json", function(error, topology) {
    g.selectAll("path")
        .data(topojson.object(topology, topology.objects.BocaVsRiver)
        .geometries)
    .enter()
        .append("path")
        .attr("d", path)
        .attr("class",  function(d) {
            var diff = d.properties.diff;
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
                        "<h6>Boca: " + d.properties.boca +"</h6>" +
                        "<h6>River: " + d.properties.river +"</h6>"
                            );
            })
            .on('mouseout', function() {
                tooltip.classed('hidden', true);
            });
});