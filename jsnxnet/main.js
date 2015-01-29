var G = jsnx.Graph();

G.add_nodes_from([1,2,3,4], {group:0});
G.add_nodes_from([5,6,7], {group:1});
G.add_nodes_from([8,9,10,11], {group:2});

G.add_path([1,2,5,6,7,8,11]);
G.add_edges_from([[1,3],[1,4],[3,4],[2,3],[2,4],[8,9],[8,10],[9,10],[11,10],[11,9]]);

var color = d3.scale.category20();

jsnx.draw(G, {
	element: '#graph',
	layout_attr: {
		charge: -120,
		linkDistance: 20
	},
	node_shape: "image",
	node_attr: {
		"xlink:href": "https://cdn2.iconfinder.com/data/icons/ios-7-icons/50/user_male2-128.png",
		width: 16,
		height: 16,
		x: -8,
		y: -8,
		r: 5,
		title: function(d) { return d.label; },
		id: function(d) { return "node-"+d.node; },
	},
	node_style: {
		fill: function(d) { 
			return color(d.data.group); 
		},
		stroke: 'none',
	},
	edge_style: {
		fill: '#999'
	}
}, true);

function highlight_nodes(nodes, on) {
	nodes.forEach(function(n) {
		d3.select('#node-' + n).style('fill', function(d) {
			return on ? '#EEE' : color( d.data.group );
		});
	});
}

function hide_nodes( nodes, on ) {
	nodes.forEach( function(n) {
		d3.select('#node-' + n).style('opacity', function(d) {
			return on ? 0 : 1;
		});
	})
}

//bind event handlers
d3.selectAll('.node').on('mouseover', function(d) {
//	highlight_nodes(d.G.neighbors(d.node).concat(d.node), true);
	hide_nodes(d.G.neighbors(d.node).concat(d.node), true);
});

d3.selectAll('.node').on('mouseout', function(d) {
//	highlight_nodes(d.G.neighbors(d.node).concat(d.node), false);
	hide_nodes(d.G.neighbors(d.node).concat(d.node), false);
});

d3.selectAll('.node').on('click', function(d) {
	// stampa il grado del nodo
	console.log( "degree(" + d.node +"): "+d.G.neighbors( d.node ).length );
});