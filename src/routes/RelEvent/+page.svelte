<svelte:head>
	<title>About</title>
	<meta name="description" content="Beta version of prototype" />
	
	<script src="https://d3js.org/d3.v7.js" charset="utf-8"></script>
	
	<script src="https://cdnjs.cloudflare.com/ajax/libs/axios/1.2.1/axios.min.js"></script>	

	<!-- Used for legend -->
	<script src="https://unpkg.com/htl@0.3.1"></script>
	<!-- Slider -->
	<script src="https://cdn.jsdelivr.net/npm/svelte-range-slider-pips@2.2.2/dist/svelte-range-slider-pips.js"></script>
	<!-- Sankey for attributes -->
	<script src="https://unpkg.com/d3-sankey@0.12"></script>
	<!-- MultiSelect -->
	<!-- <script src="https://unpkg.com/browse/svelte-multiselect@10.3.0/"></script> -->

</svelte:head>


<!-- ************************************************************* -->
<!-- ************************************************************* -->
<!--                    IMPORTANT MEMO BOARD                       -->
<!-- Important: Juliet still uses files in bravo! -->
<!-- ************************************************************* -->
<!-- ************************************************************* -->


<!-- ************************************************************* -->
<!-- Initializing first variables in buttons -->
<!-- ************************************************************* -->

<script>
	// Initializing variables for buttons
	var b_seq_col = 'id'
	var b_col = "case"
	var b_attr = "contact"
	var b_seq_rel= "Friendship"


	// *************************************************************
	// Selector multiple
	// *************************************************************
	var flavours = ['description', 'contact', 'bin_duration', 'direction'];

	import MultiSelect from './MultiSelect.svelte';
	
	var options = ['description', 'contact','direction', 'duration', 'working_hours'];
	var values = ['description', 'contact', 'bin_duration', 'direction', 'working_hours'];

	

	import Svelecte from 'svelecte';

	const list = [{ id: 1, name: 'Item 1' }, { id: 2, name: 'Item 2'}];
	let myValue = null;

	// *************************************************************
	// Function to capitalize the first letter of a string
	// *************************************************************
	/**
     * @param {string} string
     */
	function capString(string) {return string.charAt(0).toUpperCase() + string.slice(1).replaceAll('_', ' ');}
	var d_attr = {'description': 'Eventtype', 'contact': 'Contact', 'bin_duration': 'Duration', 'direction':'Direction', 'working_hours': 'Working hours'}

	import {onMount} from "svelte"


	// *************************************************************
	// Slider
	// *************************************************************
  	// slider style sheets
	import css from './Slider.css?inline';
    /* hide */
    const renderCss = `<style>${css}</style>`;

	
</script>


<!-- ************************************************************* -->
<!-- Layout divs -->
<!-- ************************************************************* -->
<div id="layout">
	<div id="menu" class="float-parent-element">
		<div id="menu_case" class="float-child-element-50">
			<div class="float-child-element-menu">
			<div id="case_div" class="scroll_class">
				<svg id=case x=0 y=0 width=100% height=2050 viewBox="0 0 100% 2050"></svg> 
				<!-- For horizontal scrolling use width = 500 instead of 100%. -->
			</div>
			</div>

		</div>
		<div id="menu_seq" class="float-child-element">
		</div>

		<div id="menu_event" class="float-child-element">
		</div>
		<div id="menu_time" class="float-child-element-50">
			<small>Choose sequence relation</small>
			<select id="selectSeqAttr"  bind:value={b_seq_rel}>
				<option value="Friendship">Friendship</option>
				<option value="Lab">Work proximity</option>
				<option value="Outlab">Outside work proximity</option>  
				<option value="All_Seq">All sequence relations</option>
			</select>
			<br>
			<small> Choose color sequences</small>
			<select id="selectSeqCol" bind:value={b_seq_col}>
			</select>
			<br>

			<small>Color events by </small>
			<select id="selectCol"  bind:value={b_col}>
				<option value="case">Case</option>
 				<option value="description">Eventtype</option>
 				<!-- <option value="b_attr">By attribute</option>  Should grey out nodes without attribute. Options: contact, duration, direction -->
				 <option value="contact">Contact</option>
				 <option value="direction">Direction</option>
				 <option value="bin_duration">Duration</option>  
				 <option value="working_hours">Working hours</option>  
				</select>
			<br>
			<button id="but_filter">Apply selections</button>
			<br>
			
			<div class="float-child-element-25"> <small>Filter hours</small> </div>
			 <div id=bounding class="float-child-element-60">
				<div id="slide_hours" class="float-child-element-60-abs"></div>
				<div class="overlay">
					<svg id='bar_hour' class="overlay" width=100% height=50></svg>
				</div>
			 </div>
			<br>
			<div class="float-child-element-25"> <small>Filter dates</small> </div>
				<div id=bounding class="float-child-element-60">
				<div id="slide_dates" class="float-child-element-60-abs"> </div>
				<div class="overlay">
					<svg id='bar_day' class="overlay" width=100% height=50></svg>
				</div>
			</div>
		</div>
	</div>

	<div id="main" class="float-parent-element">
		<!-- <div id="main" class="float-child_" -->
		<div id="main_charts" class="main">
			
			<!-- <p>Sequence relations</p> -->
			<div id="legend_seq"></div>
			<svg id=chart_seq class=chart_seq width=100% height = 200></svg>
			<!-- <p>Event relations</p> -->
			<div id="legend_event"></div>
			<svg id=chart_event class=chart_event width=100% height = 200 ></svg>
			<!-- <p>Attribute view</p> -->
			 <div id= checks_attr>

				{#each ['description', 'contact', 'bin_duration', 'direction', 'working_hours'] as flavour}
					<label id="checks">
						<input
							class="messageCheckbox"
							type="checkbox"
							name="flavours"
							value={flavour}
							bind:group={flavours}
						/>
						<!-- d_attr[flavour] adds names after the checkmarks -->
						{d_attr[flavour]} 
						
					</label>
				{/each}
				
			 </div>
			 <div id=chart_attr class="main"></div>
		</div>
	</div>

	<div id="views" class="float-parent-element">

		<div id="Detail" class="float-child-element-time">
			<p> Detail view</p>
			<div id="detail_div" class="detail_class">
				<svg id=detail x=0 y=0 width=700 height=1500 viewBox="0 0 700 1500">
			</div>
		</div>

		<div id="Timeline" class="float-child-element-time">
			<p>Timeline</p>
			<div id="timeline_div" class="timeline_class">  
				<svg id=timeline_svg x=0 y=0 width=100% height=500></svg>
			</div>
		</div>

	<script>

		// *************************************************************
		// Axios request
		// *************************************************************
		// Data request via axios post and live flask server
		// Need to have server active by using 'python flask/app.py'
		async function post(attr_a = 'all', attr_b=0, attr_filter=0) {
			try {
				const response = await axios.post('http://127.0.0.1:5000//RM_small',  
					// {attr_a: attr_a, attr_seq_rel: attr_seq_rel}
					{attr_a: attr_a, attr_b: attr_b, attr_filter:attr_filter
					}).then(); 
					var out = JSON.parse(response.data.answer)
					return out

			} catch (error) {
				console.log('error')
				console.error(error);
			}}

		// *************************************************************
		// Parallel sets
		// *************************************************************
		// Function to create graph for parallel sets
		// Source: https://observablehq.com/@d3/parallel-sets
		async function graphCreation(data){
			const keys = check_attr//['description', 'direction', 'contact', 'bin_duration', ]//, 'working_hours contact 'bin_duration'] //date 'duration'
			let index = -1;
			const nodes = [];
			const nodeByKey = new d3.InternMap([], JSON.stringify);;
			const indexByKey = new d3.InternMap([], JSON.stringify);;
			const links = [];

			for (const k of keys) {
				for (const d of data) {
				const key = [k, d[k]];
				if (nodeByKey.has(key)) continue;
				const node = {name: d[k], header:k};
				nodes.push(node);
				nodeByKey.set(key, node);
				indexByKey.set(key, ++index);
				}
			}

			for (let i = 1; i < keys.length; ++i) {
				const a = keys[i - 1];
				const b = keys[i];
				const prefix = keys.slice(0, i + 1);
				const linkByKey = new d3.InternMap([], JSON.stringify);
				for (const d of data) {
				const names = keys.map(k => d[k]); // all keys to prevent merging, this way flows can be colored correctly. Just ugly overlapping lines sometimes.
				const d_names = Object.fromEntries(keys.map(k => [k, d[k]])) //flows are not seperated per keys before
				const value = d.value || 1;
				let link = linkByKey.get(names);
				if (link) { link.value += value; continue; }
				link = {
					source: indexByKey.get([a, d[a]]),
					target: indexByKey.get([b, d[b]]),
					sourcename: d[a], // keys[i]
					targetname: d[b],
					names,
					d_names,
					value
				};
				links.push(link);
				linkByKey.set(names, link);
				}
			}
			// return graph
			return {nodes, links, keys};
			}

		// Function to create parallel sets visualization
		async function parallelSets(id, svg, title=null){
			if (check_attr === undefined || check_attr.length <2) {
				console.log('data is empty')
				svg.selectAll("g")
					.data([1])
					.enter()
					.append("text")
					.attr("x", width/2)
					.attr("y", height/2)
					.text("Select more attributes")
					.style("text-anchor", "middle")
				return svg.node();
			}

			// select data and svg
			var output_data = await out_event;
			var b_c = b_col
			var d_temp= {'case': check_attr[0], 'duration': 'bin_duration', 'bin_duration': 'bin_duration', 'description': 'description', 'contact':'contact', 'direction':'direction', 'working_hours': 'working_hours'}
			b_c = d_temp[b_c]

			var sortedList = d3.rollups(output_data.nodes, (d) => d.length, (d) => d[b_c]).sort((a, b) => a[1] < b[1] ?	1 : a[1] > b[1] ? -1 : 0).map(function(d){return d[0]}).slice(0,12) // get 12 categories with most occurances
			var ps_data = output_data.nodes.filter(o => [id].includes(o.case))
			var currentWidth = parseInt(d3.select('#main_charts').style('width'), 10)
				height = 250
				width = currentWidth/4

			// add title above / case number
			if (title){
				svg.selectAll("g")
					.data(title)
					.enter()
					.append("text")
					.attr("x", 13)
					.attr("y", 0)
					.text(title)
					.style("text-anchor", "middle")
				}
			// remove case number from list
			svg.on("click", function(){
				attribute_list.splice(attribute_list.indexOf(id), 1)
				console.log('removing one attribute' , attribute_list)
				plotAttributes(out_event, attribute_list, div_attr, b_col)
			})
			
			var graph = await graphCreation(ps_data);

			var sankey = d3.sankey()
				.nodeSort(null)
				.linkSort(null)
				.nodeWidth(4)
				.nodePadding(1)
				.extent([[10, 5], [width-10, height - 5]])
				
			let c_dict = d3.scaleOrdinal() //c_dict_highlight
						.domain(sortedList)
						.range(d3.schemeSet3)
						.unknown("grey")
	
			// text no events present
			if (ps_data === undefined || ps_data.length == 0) {
				console.log('data is empty')
				svg.selectAll("g")
					.data([1])
					.enter()
					.append("text")
					.attr("x", width/2)
					.attr("y", height/2)
					.text("No events present \n in this selected case")
					.style("text-anchor", "middle")
				return svg.node();
			}

			const {nodes, links} = sankey({
				nodes: graph.nodes.map(d => Object.create(d)),
				links: graph.links.map(d => Object.create(d))
			});

			console.log('nodes', nodes)
			console.log('links', links)

			// Centering text above center or extremes
			function outlining(d){
				if(d.layer == 0){return 'start'}
				else if(d.sourceLinks.length == 0){return 'end'}
				else{return 'middle'}
			}

			function xOutlining(d){
				if(d.layer == 0){return d.x1 + 14}
				else if(d.sourceLinks.length == 0){return d.x0}
				else{return d.x0}
			}
			// create labels // attribute names
			svg.append("g")
				.style("font", "10px sans-serif")
				.selectAll("text")
				.data(nodes)
				.join("text")
				.attr("x", xOutlining)//d => d.x0 < width / 2 ? d.x1 + 6 : d.x0 - 6)
				.attr("y", 0)
				.attr("dy", "0.35em")
				.attr("text-anchor", outlining)//d => d.x0 < width / 2 ? "left" : "middle")
				.text(d => d_attr[d.header])

			// add viewbox
			svg
				.attr("viewBox", [0, 0, width, height])
				.attr("width", width)
				.attr("height", height)
				.attr("style", "max-width: 100%; max-height: 100%;");

			function funcMouseover(event, d) {
				axes.attr("stroke", d => 'grey')
			}
			function funcMouseout(event, d) {
				edges
					.attr("stroke", d => c_dict(d.d_names[b_c]))
			}

			// show attribute values
			var showAttr = function(event, d){
				var width = 300
				var height = 50
				
				const sortAlphaNum = (a, b) => a[0].localeCompare(b[0], 'en', { numeric: true }) //sorting method
				rolls = d3.rollups(ps_data, (p) => p.length, (p) => p[d.header]).sort(sortAlphaNum)

				// X axis
				var x = d3.scaleBand().range([0, width]).domain(rolls.map(d => d[0])).padding(0.2);
				var y = d3.scaleLinear().domain([0,Math.max(...rolls.map(d => d[1]))]).range([height, 0]);

				d3.select("#detail").selectAll("svg > *").remove();				

				var svg = d3.select("#detail")

				// add title above bar
				svg.selectAll("g")
					.data(title)
					.enter()
					.append("text")
					.attr("x", 15)
					.attr("y", 30)
					.text("Case " + id + " " + d_attr[d.header])
					.style("text-anchor", "left")

				var bar_chart = svg.append("g")
					.attr("transform", "translate(" + 30 + "," + height*1.5 + ")") //changed x,y

				// Bars
				var bars = bar_chart
					.selectAll("mybar")
					.data(rolls)
					.enter()
					.append("rect")
						.attr("x", function(d) { return x(d[0]); }) 
						.attr("y", function(d) { return y(d[1]); })
						.attr("width", x.bandwidth())
						.attr("height", function(d) { return height - y(d[1]); })
						.attr("fill", "#66B2D8")

				var axis = d3.axisBottom(x).tickSize(2)
					
				// axis
				bar_chart
					.append("g")
					.attr("transform", "translate(" + 0 + ","+ height+ ")") //changed x,y
					.call(axis)
					.selectAll("text")
						.style("text-anchor", "end")
						.attr("dx", "-.8em")
						.attr("dy", ".15em")
						.attr("transform", "rotate(-55)" );
			}
			
			// create nodes
			var createNodes = function(){
				return svg
					.append("g")
					.selectAll("rect")
					.data(nodes)
					.join("rect")
					.attr("x", d => d.x0)
					.attr("y", d => d.y0)
					.attr("height", d => d.y1 - d.y0)
					.attr("width", d => d.x1 - d.x0)
					.on("mouseover", function(event,d){showAttr(event,d)})
					.append("title")
					.text(d => `${d.name}\n${d.value.toLocaleString()}`);
			}

			// create links
			function createLinks(){
				return svg
					.append("g")
					.attr("fill", "none")
					.selectAll("g")
					.data(links)
					.join("path")
					.attr("d", d3.sankeyLinkHorizontal())
					.attr("stroke", d => c_dict(d.d_names[b_c]))
					.attr("stroke-width", d => d.width)
					.style("mix-blend-mode", "multiply")
					.append("title")
					.text(d => `${d.names.join(" → ")}\n${d.value.toLocaleString()}`);
			}

			// create labels
			svg.append("g")
				.style("font", "10px sans-serif")
				.selectAll("text")
				.data(nodes)
				.join("text")
				.attr("x", d => d.x0 < width / 2 ? d.x1 + 6 : d.x0 - 6)
				.attr("y", d => (d.y1 + d.y0) / 2)
				.attr("dy", "0.35em")
				.attr("text-anchor", d => d.x0 < width / 2 ? "start" : "end")
				.text(d => d.name)
				.append("tspan")
				.attr("fill-opacity", 0.7)
				.text(d => ` ${d.value.toLocaleString()}`); // IMPORTANT

			var axes = createNodes()
			var edges = createLinks()

			edges
				.selectAll("g")
				.style('stroke', '#b8b8b8')

			console.log(edges)
			
			return svg.node();
		}

		// Function to create SVG element
		function createSVG(div){ 
			var currentWidth = parseInt(d3.select('#main_charts').style('width'), 10)
			var svg = div.append('svg').attr('height', 300).attr('width', currentWidth/4)
			var svg = svg.append("g").attr("transform", "translate(0,20)")
			return svg
		}

		async function plotAttributes(){//out_event, attribute_list, div_attr, b_col=b_col){ // b_col is global, should it be here or not?
			// clear previous graph
			div_attr.selectAll("svg").remove();

			// unique list sorted by order event to sort attribute graphs
			var place_holder = 'unknown'
			if (order_str =='Event_Friendship'){	place_holder = "order_f"}
			else if (order_str =="Event_Lab"){			place_holder = "order_l"}
			else if (order_str =="Event_Outlab"){		place_holder = "order_o"}
			else if (order_str =="Event_All_Seq"){		place_holder = "order_a"}

			var awaited = await out_seq // based on out event does not allow for clicking on sequence nodes. 
			attribute_list = [...new Set(awaited.nodes.sort((a, b) => parseFloat(a[place_holder]) - parseFloat(b[place_holder])).map((d)=>d.id))].filter(o => attribute_list.includes(o))
			
			// plot ps for each selected element.
			attribute_list.forEach(function (i){
				parallelSets(i, createSVG(div_attr), i.toString())
			})
		}

		// *************************************************************
		//	Legend
		// *************************************************************
		// Copyright 2021, Observable Inc.
		// Released under the ISC license.
		// https://observablehq.com/@d3/color-legend
		function Swatches(color, {
			columns = null,
			format,
			unknown: formatUnknown,
			swatchSize = 15,
			swatchWidth = swatchSize,
			swatchHeight = swatchSize,
			marginLeft = 15 // changed value
			} = {}) {
			const id = `-swatches-${Math.random().toString(16).slice(2)}`;
			const unknown = formatUnknown == null ? undefined : color.unknown();
			const unknowns = unknown == null || unknown === d3.scaleImplicit ? [] : [unknown];
			const domain = color.domain().concat(unknowns);
			if (format === undefined) format = x => x === unknown ? formatUnknown : x;
		
			function entity(character) {
				return `&#${character.charCodeAt(0).toString()};`;
			}
		
			if (columns !== null) return htl.html`<div style="display: flex; position: relative; align-items: center; margin-left: ${+marginLeft}px; min-height: 33px; font: 10px sans-serif;">
			<style>
		
			.${id}-item {
			break-inside: avoid;
			display: flex;
			align-items: center;
			padding-bottom: 1px;
			}
		
			.${id}-label {
			white-space: nowrap;
			overflow: hidden;
			text-overflow: ellipsis;
			max-width: calc(100% - ${+swatchWidth}px - 0.5em);
			}
		
			.${id}-swatch {
			width: ${+swatchWidth}px;
			height: ${+swatchHeight}px;
			margin: 0 0.5em 0 0;
			}
		
			</style>
			<div style=${{width: "100%", columns}}>${domain.map(value => {
				const label = `${format(value)}`;
				return htl.html`<div class=${id}-item>
				<div class=${id}-swatch style=${{background: color(value)}}></div>
				<div class=${id}-label title=${label}>${label}</div>
				</div>`;
			})}
			</div>
			</div>`;
		
			return htl.html`<div style="display: flex; position: relative; align-items: center; min-height: 33px; margin-left: ${+marginLeft}px; font: 10px sans-serif;">
			<style>
		
			.${id} {
			display: inline-flex;
			align-items: center;
			margin-right: 1em;
			}
		
			.${id}::before {
			content: "";
			width: ${+swatchWidth}px;
			height: ${+swatchHeight}px;
			margin-right: 0.5em;
			background: var(--color);
			}
		
			</style>
			<div>${domain.map(value => htl.html`<span class="${id}" style="--color: ${color(value)}">${format(value)}</span>`)}</div>`;
			}
			// end copy

			function addLegend(c_scale, loc){
				div = document.getElementById(`legend_${loc}`); // select div
				while (div.firstChild) {div.removeChild(div.lastChild);} // remove previous legend
				var swatCol = Swatches(c_scale) // create new legend
				div.appendChild(swatCol) // add new legend
			}


		// *************************************************************
		// Arc Graph
		// *************************************************************
		// Start function with async for data loading
		async function arc(output, svg, b_col, shape="circle", order_str="id", list_high=[], chart_type="seq", hour_filter=[0,24], date_filter=[0,1], node_size=4, ) {
			// clear previous graph
			svg.selectAll("svg > *").remove()
			// load data
			var data = await output;
			var d_nodes = data.nodes
			var d_links = data.links
			var list_high = await list_high;
			var height = 200  // height of axis, corresponds with height of svg.
			currentWidth = parseInt(d3.select('#main_charts').style('width'), 10)
			currentHeight = parseInt(d3.select('#main_charts').style('height'), 10)
			var g = svg.append("g").attr("cursor", "grab");

			console.log('arc nodes', chart_type, d_nodes)
			console.log('arc links', chart_type, d_links)

			var c_value = d3.schemeSet3
			var sortedList = d3.rollups(d_nodes, (d) => d.length, (d) => d[b_col]).sort((a, b) => a[1] < b[1] ?	1 : a[1] > b[1] ? -1 : 0).map(function(d){return d[0]}).slice(0,12) // get 12 categories with most occurances

			var order = [] // gotten from reordering.js see report for more details.
			var location = "id" //name of variable to set x()

			if (order_str =="Friendship"){	location = "order_f"}
			else if (order_str =="Lab"){	location = "order_l"}
			else if (order_str =="Outlab"){	location = "order_o"}
			else if (order_str =="All_Seq"){location = 'id'}
			else if (order_str =='Event_Friendship'){	location = "order_f"}
			else if (order_str =="Event_Lab"){			location = "order_l"}
			else if (order_str =="Event_Outlab"){		location = "order_o"}
			else if (order_str =="Event_All_Seq"){		location = "order_a"}
			else{location = order_str}	


			// Order
			function createOrder(d,i){
				d['location']=d_nodes[i][location]//d_nodes.map(function(d,i){return i}) //d[location]//d_nodes.map(function(d,i){return i}) 
				return d}

			d_nodes = d_nodes.map(createOrder) //  adding selected location keyword like "order_f" into "location"
			order = d_nodes.map(function(d){return d[location]})
			var location = 'location'

			d_nodes.sort((a, b) => parseFloat(a[location]) - parseFloat(b[location]))

			// Filtering
			if(chart_type == "event"){
				// filtering of hours
				d_nodes = data.nodes.filter(o => d3.range(...hour_filter).includes(parseInt(d3.timeFormat("%H")(o.date))))
				
				// filter days
				start_d = d3.min(d_nodes.map(d => d.date))
				end_d = d3.max(d_nodes.map(d => d.date))
				var numberOfDays = d3.timeDay.count(start_d, end_d)
				timeScale = d3.scaleTime().domain([start_d, end_d]).range([0, numberOfDays])
				//https://phparea.com/blog/how-to-filter-data-by-date-range-on-d3-js-line
				d_nodes = d_nodes.filter(function(d) { return d.date >= timeScale.invert(date_filter[0]) && d.date <= timeScale.invert(date_filter[1]);});

				d_nodes.sort((a, b) => parseFloat(a[location]) - parseFloat(b[location]))
				
				// removes spaces between cases keeping only standard 10.
				var min = 0
				function reduceGabs(d,i){ 
					if (i != 0){
						if (d_nodes[i]['case']!=d_nodes[i-1]['case']){min = d_nodes[i]['location'] -d_nodes[i-1]['location'] -10}
						d['location'] = d_nodes[i]['location']-min}}
				
				d_nodes.map(reduceGabs)
			
			}
			// highlighting 
			if(b_col=="id"){
					selectedColorHighlight = list_high // d_nodes.filter(o => list_high.includes(o.id)).map(d => d[b_col]) // using list high color consistant over orderings. In case of filter always start with same color first.
				}
			else if(b_col=="case"){
					selectedColorHighlight = list_high // d_nodes.filter(o => list_high.includes(o.id)).map(d => d[b_col]) // using list high color consistant over orderings. In case of filter always start with same color first.
				}
			else{
				selectedColorHighlight = sortedList//d_nodes.map(function(d){return d[b_col]})
				}

			let c_dict = d3.scaleOrdinal() //c_dict_highlight
						.domain(selectedColorHighlight)
						.range(c_value)
						.unknown("grey")

			addLegend(c_dict, chart_type)

			var order_f_order = d_nodes.map(function(d){return d["order_f"]})
			var order_location = d_nodes.map(function(d){return d["location"]})

			var x = d3.scaleLinear()
				.range([20, currentWidth-20])
				.domain([d3.min(d_nodes.map(function(d){return d[location]})), d3.max(d_nodes.map(function(d){return d[location]}))])

			// https://d3-graph-gallery.com/graph/arc_basic.html
			// Add the circle for the nodes
			var createNodes = function(shape = "circle"){
				if (shape=="circle"){
					return svg
						.selectAll("mynodes")
						.data(d_nodes)
						.enter()
						.append(shape)
						.attr('class', "circle")
						.attr("cx", function(d){ return(x(d[location]))})
						.attr("cy", height-30)
						.attr("r", node_size)
						.style("fill", d => c_dict(d[b_col]))
				}
				else{ //rect
					return svg
						.selectAll("mynodes")
						.data(d_nodes)
						.enter()
						.append(shape)
						// .attr("x", function(d){ return(x(d[location])-node_size)})
						.attr("x", function(d){ return(x(d[location])-0.5*node_size)})
						.attr("y", height-30)
						// .attr("width", node_size*2)
						.attr("width", node_size)
						.attr("height", node_size*2)
						.style("fill", d => c_dict(d[b_col]))
					}
			}
			if (chart_type=='seq'){	
				var createLabels = function(){
					return svg
						.selectAll("mylabels")
						.data(d_nodes)
						.enter()
							.append("text")
							.text(function(d){ return(d.id)})
							.attr("transform", function(d,i){
								var xText = x(d[location])-3
								var yText = height-10 //-20
								return "translate(" + xText + "," + yText + ") "}) //rotate(90)
							.style("font-size", "8px")
			}}
			else if(chart_type=='event'){ // possible to change text with centered instead of left oriented?
				// take median of 
				var med_rol = d3.rollups(d_nodes, (v) => d3.median(v, d=>d[location]),(d) => d['case'] )

				var createLabels = function(){
				return svg
					.selectAll("mylabels")
					.data(med_rol)
					.enter()
						.append("text")
						.text(function(d){ return(d[0])})
						.attr("transform", function(d,i){
							var xText = x(d[1])-5 //-3
							var yText = height-10 //-20
							return "translate(" + xText + "," + yText + ") "}) //rotate(90)
						.style("font-size", "8px")
			}
			}

			
			var createLinks = function(){
				return svg
					.selectAll('mylinks')
					.data(d_links)
					.enter()
					.append('path')
					.attr('d', function (d) {
						start = x(d_nodes.filter(function(n){return n['id'] === d.source }).map(function(n){return n[location]}))    // X position of start node on the X axis
						end = x(d_nodes.filter(function(n){return n['id'] === d.target}).map(function(n){return n[location]}))      // X position of end node
						return ['M', start, height-30,    // the arc starts at the coordinate x=start, y=height-30 (where the starting node is)
							'A',                            // This means we're gonna build an elliptical arc
							(start - end)/2, ',',    // Next 2 lines are the coordinates of the inflexion point. Height of this point is proportional with start - end distance
							(start - end)/10, 0, 0, ',', //Relative height of arc (normal /2)
							start < end ? 1 : 0, end, ',', height-30] // We always want the arc on top. So if end is before start, putting 0 here turn the arc upside down.
							// start < end ? 1 : 1, end, ',', height-30] // We always want the arc on top. So if end is before start, putting 0 here turn the arc upside down.
							.join(' ');
						})
					.style("fill", "none")
					.attr("stroke", "black")
					.attr("stroke-opacity", .2)
			}

			var nodes = createNodes(shape);
			var labels = createLabels();
			var links = createLinks()

			var ArcHoover = function(event,d, there){
				// Highlight the nodes: every node is grey except of him
				nodes.style('fill', "#B8B8B8")
				d3.select(there).style('fill', c_dict(there.__data__[b_col]))
				// Highlight the connections
				links
				.style('stroke', a=>  a.source === d.id || a.target === d.id ? c_dict(there.__data__[b_col]) : '#b8b8b8')
				.attr("stroke-opacity", a=>  a.source === d.id || a.target === d.id ? 1 : 0.2)
				.style('stroke-width', a=>a.source === d.id || a.target === d.id ? 4 : 1)

				// Add attributes to detail view.
				d3.select("#detail")
					.selectAll("svg > *").remove();	

				d3.select("#detail")
					.selectAll("text")
					.data(Object.entries(there.__data__).map(([k, v]) => `${k}: ${v}`))
					.enter()
					.append("text")
						.attr("x", 15)
						.attr("y", function(d,i){return 30+i*25})
						.style("fill", "black")
						.text(function(d){return capString(d)})
						.attr("text-anchor", "left")
						.style("alignment-baseline", "middle")		
			}

			var ArcHooverStop = function(event, d){
				nodes.style("fill", d => c_dict(d[b_col]))
				links
					.style('stroke', 'black')
					.attr("stroke-opacity", .2)
					.style('stroke-width', '1')
			}

			function zoom(svg) {
				var extent = [[0, 0], [currentWidth, height]];

				svg.call(d3.zoom()
					.scaleExtent([1, 40])
					.translateExtent(extent)
					.extent(extent)
					.on("zoom", zoomed));

				function zoomed(event) {
					// apply transformation to range of x axis. And replot the data.
					x.range([20, currentWidth-20].map(function(d){return event.transform.applyX(d)})) // d is list before!!

					nodes.remove()
					labels.remove()
					links.remove()
					nodes = createNodes(shape)
					labels = createLabels()
					links = createLinks()

					// var last_clicked
					// Add the highlighting functionality
					nodes
						.on('mouseover', function(event,d){ArcHoover(event, d, this)})
						// .on('mouseout', function(event,d){ArcHoover(event, d, last_clicked)})
						.on('mouseout', function(event,d){ArcHooverStop(event, d)})

						// on click create chord diagram (event chart)
						.on('click', function(event,d){
								console.log('after zoom d', d)
								out_my_chord = post('chords', d.case)
								// chords(out_my_chord, d3.select('#chart_attr'), title=d.case.toString())
								// pcp(output=output, id=d.case, div=d3.select('#chart_attr'), title=d.case.toString())
								// parallelSets(output=output, id=d.case, div=d3.select('#chart_attr'), title=d.case.toString())
								if (chart_type=='seq'){attribute_list.push(d.id)};
								if (chart_type=='event'){attribute_list.push(d.case)};
								plotAttributes(out_event, attribute_list, div_attr, b_col)
							})
			}}
			zoom(svg)
			
			// First setup of detail view.
			d3.select("#detail")
					.selectAll("text")
					.data([1])
					.enter()
					.append("text")
						.attr("x", 15)
						.attr("y", 30)
						.style("fill", "black")
						.text("Hoover to see more details")
						.attr("text-anchor", "left")
						.style("alignment-baseline", "middle")

			
			// Add the highlighting functionality
			nodes
				.on('mouseover', function(event,d){ArcHoover(event, d, this)})
				.on('mouseout', function(event,d){ArcHooverStop(event, d)})

				// on click create chord diagram (event chart)
				.on('click', function(event,d){
					if (chart_type=='seq'){attribute_list.push(d.id)};
					if (chart_type=='event'){attribute_list.push(d.case)};
					plotAttributes(output, attribute_list, div_attr, b_col)
						})

		}

		// *************************************************************
		// highlighting node list
		// *************************************************************

		async function top12(rol){
			// var sortedList = rol.sort((a, b) => a < b ?	1 : a > b ? -1 : 0).map(function(d){return d[0]}).slice(0,12) //a[1] < b[1] ?	1 : a[1] > b[1] // get 12 nodes with most connections
			var sortedList = rol.sort((a, b) => a[1] < b[1] ?	1 : a[1] > b[1] ? -1 : 0).map(function(d){return d[0]}).slice(0,12) //a[1] < b[1] ?	1 : a[1] > b[1] // get 12 nodes with most connections
			console.log('sortedList', sortedList, rol)
			intList = sortedList.map(str =>{return parseInt(str,10)}) 
			return intList
		}

		async function highlight_selection(output){
			var data = await output;
			var rolls = d3.rollups(data.links, (d) => d.length, (d)=>d['source'].split('_')[0])  //.split('s')[1]// get number of links per source //['source'].split('_')[0]
			var listHighlight = top12(rolls)
			return listHighlight
		}
		

		
		// *************************************************************
		// Slider functions
		// *************************************************************
		function gabs(slider, e, gab){
			// gab between sliders updated to 1 instead of overlapping sliders.
			if (e.detail.activeHandle === 0 && e.detail.values[1] < e.detail.value + gab) {
				slider.$set({ values: [e.detail.values[0],e.detail.values[1]+gab]})
			}
			else if (e.detail.activeHandle === 1 && e.detail.values[0] > e.detail.value - gab) {
				slider.$set({ values: [e.detail.values[0]-gab,e.detail.values[1]]})
			}}

		function maxGabs(slider, e, gab){
			var max_gab = 14// max select x number of days
			console.log('e.detail.values', e.detail.values)
			// gab between sliders updated to 1 instead of overlapping sliders.
			if (e.detail.activeHandle === 0 && e.detail.values[1] < e.detail.value + gab) {
				slider.$set({ values: [e.detail.values[0],e.detail.values[1]+gab]})
			}
			else if (e.detail.activeHandle === 1 && e.detail.values[0] > e.detail.value - gab) {
				slider.$set({ values: [e.detail.values[0]-gab,e.detail.values[1]]})
			}
			// gab between sliders updated to 2 instead of larger gab.
			else if (e.detail.activeHandle === 0 && e.detail.values[1] > e.detail.value + max_gab) {
				slider.$set({ values: [e.detail.values[0],e.detail.values[0]+max_gab]})
				console.log('case 3 detail',[e.detail.values[0],e.detail.values[1]-max_gab])
			}
			else if (e.detail.activeHandle === 1 && e.detail.values[0] < e.detail.value - max_gab) {
				slider.$set({ values: [e.detail.values[1]-max_gab,e.detail.values[1]]})
				console.log('case 4 detail',[e.detail.values[0]+max_gab,e.detail.values[1]])
			}
			console.log('after update', e.detail.values)
		}

		function spaceHour(slider, e, min, max, gab){
			if (e.detail.activeHandle === 0 && e.detail.value >= max) {
				e.detail.values[0] = max - gab;
				slider.$set({ values: [max - gab, e.detail.values[1]]});}
			if (e.detail.activeHandle === 1 && e.detail.value <= min) {
				e.detail.values[1] = min + gab;
				slider.$set({ values: [e.detail.values[0], min + gab]});}
			
			}
		
		var formatTime = d3.timeFormat("%b %d, %Y");
		

		async function sliders(output){
			// source: https://codepen.io/simeydotme/pen/KKNJdbK
			// https://simeydotme.github.io/svelte-range-slider-pips/en/examples/pips/
			// slider Hour
			var sliderHour = new RangeSliderPips({
				target: document.getElementById("slide_hours"),
				props: {min: min_h,	max: max_h, range: true, pushy: true, values: hour_window,
					pips: true, pipstep: 1, all: true, float: true, first: "label", last:"label", id: "label_d_slider",
					formatter: (v) => {if (v<10) {return "0"+v} else{return v}},
				} });

			sliderHour.$on('change', function(e){gabs(sliderHour, e,gab_h)})
			sliderHour.$on('stop', function(e){spaceHour(sliderHour, e, min_h, max_h, gab_h)
				hour_window = e.detail.values
				console.log('updating', e.detail.values, hour_window)
				arc(out_event, svg_event, b_col, shape='rect', order_str=b_event_order, list_high=list, chart_type="event", hour_filter=hour_window, date_filter=date_window)
			}) // global variables 0, 24, 1
			
			// https://observablehq.com/@lorenries/encoding-a-date-range-onto-a-slider-with-d3
			// slider date
			var data = await output;
				start_d = d3.min(data.nodes.map(d => d.date))
				end_d = d3.max(data.nodes.map(d => d.date))
				numberOfDays = d3.timeDay.count(start_d, end_d)
				tScale = d3.scaleTime().domain([start_d, end_d]).range([0, numberOfDays])
				min_d = tScale(start_d)
				max_d = tScale(end_d)
				date_window = [0,1]

			var sliderDate = new RangeSliderPips({
				target: document.getElementById("slide_dates"),
				props: {min: min_d, max: max_d,	range: true, pushy: true, values: date_window,
					pips: true, all: true, float: true, first: "label", last:"label", id: "label_d_slider",
					formatter: function(v){return formatTime(tScale.invert(v))},
				}});

			sliderDate.$on('change', function(e){maxGabs(sliderDate, e, gab_d)})
			sliderDate.$on('stop', function(e){spaceHour(sliderDate, e, min_d, max_d, gab_d)
				date_window = e.detail.values
				console.log('updating', e.detail.values, date_window)
				arc(out_event, svg_event, b_col, shape='rect', order_str=b_event_order, list_high=list, chart_type="event", hour_filter=hour_window, date_filter=date_window)
			})

		}				

		// *************************************************************
		// Small functions
		// *************************************************************
		
		//capitalize first letter
		function capString(string) {return string.charAt(0).toUpperCase() + string.slice(1).replaceAll('_', ' ');}
		function reCapString(string) {return string.charAt(0).toLowerCase() + string.slice(1).replaceAll(' ', '_');}

		// small functions
		async function process(input) {
			out = await input
			out.nodes.forEach(function(d) {d.date = d3.timeParse("%Y-%m-%d %H:%M:%S")(d.date)})
			return out
		}

		function queryChecks(){
			let result = []
			var docs = document.querySelectorAll('.messageCheckbox:checked')
			var len = docs.length
			for (var i=0; i<len; i++) {
				if(docs[i].value){
					result.push(docs[i].value)}
			}
			return result
		}

		var d_attr = {'description': 'Eventtype', 'contact': 'Contact', 'bin_duration': 'Duration', 'direction':'Direction', 'working_hours': 'Working hours'}

		// *************************************************************
		// Variables and reactive statements
		// *************************************************************
		
		var b_seq_col = 'id'
		var b_col = "case"
		var b_attr = "contact"
		var b_seq_rel= "Friendship"
		var b_event_order = "Event_Friendship"
		var s_filter_list = "[[]]"
		var attribute_list = [9]
		// var attribute_list = [...Array(106).keys()];

		//svg
		var svg_seq = d3.select("#chart_seq")//.attr("viewBox", `0 0 300 600`)
		var svg_event = d3.select("#chart_event")//.attr("viewBox", `0 0 300 600`)
		var svg_attr = d3.select("#chart_attribute")
		var div_attr = d3.select('#chart_attr')

		// data
		var out_event = post('event')
		var out_event = process(out_event)
		var out_seq = post('Friendship')
		var list = highlight_selection(out_event)
		console.log('list from highlight selection', list)
		// checks
		var check_attr = queryChecks()
		console.log('+++ check_attr', check_attr)
		

		// slider
		var min_h = 0
		var max_h = 24
		var gab_h = 1
		var hour_window = [9, 17]
		var start_d = 0
		var end_d = 1000
		var min_d = 0
		var max_d = 1000// d3.max(data.nodes.map(d => d.date))
		var gab_d = 1//d3.date()
		var date_window = [0,1]

		sliders(out_event)

		d3.select("#label_d_slider").on("change", function(d){
			console.log('selected my slider label (yay) continue here.')
			var temp = d3.select(this).property("values")
			console.log('temp values', temp)
		})

		//initial arcs
		
		arc(out_seq, svg_seq, b_seq_col, shape='circle', order_str=b_seq_rel, list_high=list, chart_type="seq")
		arc(out_event, svg_event, b_col, shape='rect', order_str=b_event_order, list_high=list, chart_type="event", hour_filter=hour_window, date_filter=date_window) //[possible to also get rectangles so it matches the events in timeline]

		plotAttributes()//out_event, attribute_list, div_attr, b_col)

		// chords(out_chords, div_attr, 'All')
		console.log('date_window', date_window)
		
		//***update arcs using buttons and menues***
		// color sequence attributes
		d3.select('#selectSeqCol').on("change", function(d){
			b_seq_col = d3.select(this).property("value")
			svg_seq.selectAll("svg > *").remove()
			arc(out_seq, svg_seq, b_seq_col, shape='circle', order_str=b_seq_rel, list_high=list, chart_type="seq")
		})
		
		// data of relationships
		d3.select('#selectSeqAttr').on("change", function (d){
            b_seq_rel = d3.select(this).property("value")
			console.log('s_filter_list', s_filter_list)
			out_seq = post('filter', b_seq_rel, attr_filter = s_filter_list)
			arc(out_seq, svg_seq, b_seq_col, shape='circle', order_str=b_seq_rel, list_high=list, chart_type="seq")  
			// update event order too
			b_event_order = "Event_"+b_seq_rel
			arc(out_event, svg_event, b_col, shape='rect', order_str=b_event_order, list_high=list, chart_type="event", hour_filter=hour_window, date_filter=date_window)
        })


		// color nodes of event arc diagram
		d3.select('#selectCol').on("change", function (d){
			let selectedOption = d3.select(this).property("value")
			b_col = selectedOption
			arc(out_event, svg_event, b_col, shape='rect', order_str=b_event_order, list_high=list, chart_type="event", hour_filter=hour_window, date_filter=date_window)
			// }
			plotAttributes(out_event, attribute_list, div_attr, b_col)
		})

		//click to aggregate (unfinished: return and other aggregation)
		d3.select("#but_aggr").on("click", function (d){
			svg_event.selectAll("svg > *").remove()
			console.log('click', d)
			var aggr = post('aggr')
			// console.log(aggr)
			var aggr = process(aggr)
			arc(aggr, svg_event, b_col = 'id', order_str=b_event_order, list_high=list, chart_type="seq")
		})

		d3.select("#but_filter").on("click", function(d){			
			// retrieving values from selection
			var svg_list = d3.select("#case").selectAll("svg")//needs async so it queries svg after it is fully created.
			var filter_list = Array(...svg_list._groups[0]).map((d)=> d.value)
			s_filter_list = JSON.stringify(filter_list)
			console.log('json', (s_filter_list)) ///Note:attention ordering of words no updated in selection.

			out_seq = post('filter', b_seq_rel, attr_filter = s_filter_list)
			arc(out_seq, svg_seq, b_seq_col, shape='circle', order_str=b_seq_rel, list_high=list, chart_type="seq")
		
			out_event = post('filter', 'event', s_filter_list)
			out_event = process(out_event)
			arc(out_event, svg_event, b_col, shape='rect', order_str=b_event_order, list_high=list, chart_type="event", hour_filter=hour_window, date_filter=date_window) //[possible to also get rectangles so it matches the events in timeline]
		})

		 // https://stackoverflow.com/questions/19849738/checkbox-check-uncheck-using-d3#20204162	
		d3.selectAll("#checks").on("change", function(d){
			// console.log('name attr', d.target.value)
			// let checkedValue = document.querySelector('.messageCheckbox').value;
			// console.log('checkedValue checks', checkedValue)
			check_attr = queryChecks()
			plotAttributes(out_event, attribute_list, div_attr, b_col)
		})
		
		var checkedValue = document.querySelector('.messageCheckbox:checked').value;
		console.log('checkedValue', checkedValue) //does not update list

		var cb = document.getElementsByClassName('messageCheckbox')[0]
		console.log('cb,',cb)
		cb.addEventListener('change', function(){some_var = this.checked})

		// *************************************************************
		// Singles, cases
		// Source bar chart: https://observablehq.com/@d3/ordinal-brushing?collection=@d3/d3-brush
		// *************************************************************
		// out.nodes.forEach(function(d) {d.date = d3.timeParse("%Y-%m-%d %H:%M:%S")(d.date)})
		function barChart(svg, data){
			// console.log('barChart data', data)
			var index = 0
			var height = 25  // of one bar chart 
			var trans = 0

			var local_width = parseInt(svg.style('width'), 10)
			var text_width = 0.3*local_width
			var chart_width = 0.65*local_width
			var padding_width = 0.02*local_width

			var sortAlphaNum = (a, b) => a.toString().localeCompare(b.toString(), 'en', { numeric: true }) //sorting method
			
			var SORT_ORDER = {"Strongly agree": 6, "Agree": 5, "Somewhat agree": 4, "Neutral": 3, "Somewhat disagree":2, "Disagree":1, "Strongly disagree":0, "yes":-1, "no":-2, "Unknown": -1000, "TBR": -10000}
			
			function S_ORDER(a, b){
				if(SORT_ORDER[a[0]]<=SORT_ORDER[b[0]])
					return 1
				else
					return 0
			}

			// title case attribute text.
			svg.selectAll("columns")
					.data([1])
					.enter()
					.append("text")
						.attr("x", padding_width)
						.attr("y", height)
						.text("Case attributes")
						.attr("text-anchor", "left")
						// .style("font-size", "px")

			// plotting small barcharts
			for (var el of Object.keys(data[1])){
				// var inner_svg = svg.append('svg').attr("id", "inner")
				var inner_svg = svg.append("svg").attr("id", el) //g is also possible 
				rolls = d3.rollups(data, (d) => d.length, (d) => d[el]).filter(function(d){return d[0] != "TBR" })//.map(function(d){if(d[0]=="TBR"){return ["Unknown",...d.splice(1)]} else {return d}})//.filter(function(d){return d[0] != "TBR" })				
				rolls = rolls.sort(sortAlphaNum) // sorting rolls alphabetically to sort bar charts. Done here for brushing etc.
				// console.log('el, rolls', el, rolls)
				try{rolls = rolls.sort(S_ORDER)}
				catch{console.log('NO sorting', el)}
							
				rolls.forEach(function(d){d[2] = d3.timeParse("%Y-%m-%d")(d[0])})
				rolls.forEach(function(d){d[3] = d3.timeParse("%d days")(d[0])}) //  "0 days 00:00:00"  %H:%M:%S.%f
				
				// X axis
				var x = d3.scaleBand().range([0, chart_width]).domain(rolls.map(d => d[0])).padding(0.2);
				
				// Add Y axis
				var y = d3.scaleLinear().domain([0,Math.max(...rolls.map(d => d[1]))]).range([height, 0]);

				var chart_height = height*2+index*(1.5*height) //(height + ) * index
				var axis_height = chart_height+height

				// case attribute name text.
				inner_svg.selectAll("columns")
					.data([el])
					.enter()
					.append("text")
						.attr("x", padding_width)
						.attr("y", chart_height+height)
						.text(function(d){return capString(d)})
						.attr("text-anchor", "left")
						.style("font-size", "10px")

				// Add a clipPath: everything out of this area won't be drawn.
				var clip = inner_svg.append("defs").append("svg:clipPath") // part of barchart. outside of clip will not be drawn.
					.attr("id", "clip")
					.append("svg:rect")
					.attr("width", chart_width)
					.attr("height", height)
					.attr("x", 0)
      			.attr("y", 0);

				// Add brushing
				// Add the brush feature using the d3.brush function // initialise the brush area: start at 0,0 and finishes at width,height: it means I select the whole graph area // Each time the brush selection changes, trigger the 'updateChart' function
				var brush = d3.brushX().extent([[0, 0], [chart_width,height]])
					.on("start brush end", brushed)
					.on("end.snap", brushended)

				var bar_chart = inner_svg.append("g")
					.attr("transform", "translate(" + text_width + "," + chart_height + ")") //changed x,y
					.attr("clip-path", "url(#clip)")				

				// Bars
				var bars = bar_chart
					.selectAll("mybar")
					.data(rolls)
					.enter()
					.append("rect")
						.attr("x", function(d) { return x(d[0]); }) 
						.attr("y", function(d) { return y(d[1]); })
						.attr("width", x.bandwidth())
						.attr("height", function(d) { return height - y(d[1]); })
						.attr("fill", "#69b3a2") //"#69b3a2" green "#66B2D8" blue
					
				bar_chart
					.append("g")
					.attr("class", "brush")
					.call(brush);

				//axis
				var nr_t = parseInt(x.domain().length/5) // get at most 10 ticks (data length max 106)
				var axis = d3.axisBottom(x).tickValues(x.domain().filter(function(d,i){ return !(i%nr_t)})).tickSize(2)
				inner_svg.append("g").attr("transform", "translate(" + text_width + "," + axis_height + ")").call(axis)
					.selectAll("text")
						.style("font-size", "8px")
					
				inner_svg.property("value", []).dispatch("input"); // set global value for property

				function brushed({selection}) {
					// handle brush function, highlight selected bars orange, 
					// select current bar chart
					var label =  reCapString(d3.select(this.parentNode.parentNode).select("text").text()) // label of selected bar chart
					var inner_svg = d3.select("#case").select( `#${label}`)
					var rect = d3.select(this.parentNode).selectAll("rect") // all bars in bar_chart
					if (selection) {  // color selection and add to svg properties
						rolls = d3.rollups(data, (d) => d.length, (d) => d[label]).filter(function(d){return d[0] != "TBR" })//.map(function(d){if(d[0]=="TBR"){return ["Unknown",...d.splice(1)]} else {return d}}).sort(sortAlphaNum)
						rolls = rolls.sort(sortAlphaNum) // sorting rolls alphabetically to sort bar charts. Done here for brushing etc.
						x = d3.scaleBand().range([0, chart_width]).domain(rolls.map(d => d[0])).padding(0.2);
						
						const range = x.domain().map(x);
						const i0 = d3.bisectRight(range, selection[0]);
						const i1 = d3.bisectRight(range, selection[1]);
						rect.attr("fill", (d, i) => i0 <= i && i < i1 ? "#fdb462" : null); // orange.
						inner_svg.property("value", [label, x.domain().slice(i0, i1)]).dispatch("input"); // selection present in inner_svg.property("value")
						
					} else { // undoing selection
					rect.attr("fill", null); // rect is bigger svg. need to select child elements.
					inner_svg.property("value", []).dispatch("input"); // adding selection (none) to property value
					}
					}

				function brushended({selection, sourceEvent}) {
					// snaps border to selected bars
					if (!sourceEvent || !selection) return;
					const range = x.domain().map(x), bw = x.bandwidth() //padding is about 0.2 bandwidth
						x0 = range[d3.bisectRight(range, selection[0])] - 0.02*bw;
						x1 = range[d3.bisectRight(range, selection[1]) - 1]+ 1.02*bw  ;
					d3.select(this).transition().call(brush.move, x1 > x0 ? [x0, x1] : null);
					}
			
				index +=1 // update index for chart height
			} // end of for loop

		}

		async function single(out_singles){
			//Case attribute view
			var data = await out_singles
				svg = d3.select("#case")

			// button case attribute to color sequence relation nodes
			d3.select("#selectSeqCol")
				.selectAll('myOptions')
					.data(Object.keys(data[1]))
				.enter()
					.append('option')
				.property("selected", function(d){return d === 'id';})
				.text(function(d){return capString(d)})
				.attr("value", function (d) { return d; })

			// Plot bar charts
			barChart(svg, data)
			// histogram(svg, data)
		}

		out_singles = post('singles') //loading data for singles
		single(out_singles) 





		// *************************************************************
		// Timeline
		// *************************************************************
		// Start function with async for data loading
		async function timeline(output, svg_loc) {
			// load data
			var data = await output;
			// parsing date column
			data.forEach(function(d) {
				d.date = d3.timeParse("%Y-%m-%d %H:%M:%S")(d.date) // x axis
			})
			
			var c_values = d3.schemeSet3//[ "#fee391", "#807dba","#bcbddc", ]
			
			// variables from graph
			var selectedGroup = "description"
			// var selectedGroup = yot
			var case_name = "Subject_Id"

			let c_dict = d3.scaleOrdinal()
				.domain(["Voice call", "Short message", "Packet Data"])
				.range(c_values)
		
			console.log('data timeline', data)

			// // margins and size of svg
			var margin = {top: 20, right: 30, bottom: 30, left: 30}, //margin of 300 for legend.
				width = 400 - margin.left - margin.right,
				height = 250 - margin.top - margin.bottom;

			var svg = d3.select(svg_loc)
				.append("svg")
				.attr("width", width + margin.left + margin.right)
				.attr("height", height + margin.top + margin.bottom)
				.append("g")
				.attr("transform", `translate(${margin.left}, ${margin.top})`);

			var x = d3.scaleTime(d3.extent(data, function(d) {return d.date }), [0, width]); //10000
			var y_extent = d3.extent(data, function(d) {return d.Subject_Id })
			var y = d3.scaleLinear([y_extent[1]+3, y_extent[0]-4], [height,0])

			var xAxis = svg.append("g")
				.attr("transform", `translate(0, ${height})`)
				.call(d3.axisBottom(x).ticks(6)) //d3.timeDay.every(1)
				

			var yAxis = svg.append("g")
    			.call(d3.axisLeft(y));

			// Add a clipPath: everything out of this area won't be drawn.
			var clip = svg.append("defs").append("svg:clipPath")
				.attr("id", "clip")
				.append("svg:rect")
				.attr("width", width )
				.attr("height", height )
				.attr("x", 0)
      			.attr("y", 0);

			// Create the scatter variable: where both the circles and the brush take place
			var scatter = svg.append('g')
				.attr("clip-path", "url(#clip)")
			
				// svg.selectAll(".tick line").attr("stroke", "black") //tick lines!!

			// Add dots
			var scatter = svg
				.selectAll("dot")
				.data(data)
				.enter()
				.append("circle")
					.attr("cx", function (d) { return x(d.date); } )
					.attr("cy", function (d) { return y(d.Subject_Id); } )
					.attr("r", 2)
					.style("fill", d => c_dict(d[selectedGroup]))


			var myBrush = d3.brush().on("end", ({selection}) => {
				// let value = [];
				console.log(selection)
				if (selection) {
					const [[x0, y0], [x1, y1]] = selection;
					console.log('x0, x1, ', x0, x1)
					console.log(x)
					// update axis
					x.domain([ x.invert(x0), x.invert(x1) ])
					y.domain([ y.invert(y1), y.invert(y0) ])

				} 
				else {
					// reset axis
					x.domain(d3.extent(data, function(d) {return d.date })); //10000
					// y_extent = d3.extent(data, function(d) {return d.Subject_Id })
					y.domain([y_extent[1]+3, y_extent[0]-4])

				}
				// update xAxis bases on x.domain changes
				xAxis.transition().duration(1000).call(d3.axisBottom(x))
				yAxis.transition().duration(1000).call(d3.axisLeft(y))
				// update points
				console.log('successful zoomed box')

				scatter.remove();

				scatter = svg
					.selectAll("dot")
					.data(data)
					.enter()
					.append("circle")
						.attr("cx", function (d) { return x(d.date); } )
						.attr("cy", function (d) { return y(d.Subject_Id); } )
						.attr("r", 1.5)
						.style("fill", d => c_dict(d[selectedGroup]))

				scatter.attr("transform", d => `translate(${x(d.date)},${y(d.Subject_Id)}`)

				});
				
				var brushArea = svg.append('g');
				brushArea.call(myBrush);
				svg.selectAll('.selection').remove()


				console.log('brushArea', brushArea)
				console.log('myBrush', myBrush)
		} // end of timeline function

		// *************************************************************
		// Running timeline
		// *************************************************************

		var out_time = post('time')
		timeline(out_time, "#timeline_svg")


	</script>

</div>

</div>


{@html renderCss}

<!-- ************************************************************* -->
<!-- CSS style -->
<!-- ************************************************************* -->

<style>
/* https://dev.to/dawnind/3-ways-to-display-two-divs-side-by-side-3d8b */

.float-parent-element { 
    width: 100%; 
} 
.float-child-element { 
    float: left; 
    width: 25%; 
} 
.float-child-element-time{
	float: left; 
    width: 25%; 
	height:250px;
	padding: 1rem 1rem 1rem 1rem;
}

.float-child-element-50 { 
    float: left; 
    width: 50%; 
} 

.float-child-element-60 { 
    float: left; 
    width: 60%; 
	/* position:absolute; */
} 
.float-child-element-60-abs { 
    float: left; 
    width: 30%; 
	position:absolute;
} 
.float-child-element-25 { 
    float: left; 
    width: 25%; 
} 

.float-child-element-menu{
	float: left; 
    width: 90%; 
	height: 200px;
	/* height: 25vh; */
	/* 25 vh is 25 % of view port in main screen. Also changes based on inspector window changes and directly jumps when zooming.*/
	/* padding: 1rem 1rem 1rem 1rem; */
}

.timeline_class {
	float:left;
	/* overflow:scroll; */
	/* resize: both; */
	height:100%;
	width:100%;
	background-color: #F2F1EE;
	border-style: solid;
	margin-bottom: 20px;
}

.detail_class {
	float:left;
	overflow:scroll; 
	resize: both;
	height:100%;
	width:100%;
	background-color: #F2F1EE;
	border-style: solid;
	margin-bottom: 20px;
}

.scroll_class {
	float:left;
	overflow:scroll;
	/* resize: both; */
	height:90%;
	width:100%;
	background-color: #F2F1EE;
	border-style: solid;
	margin-bottom: 10px;
	margin-top: 10px;
	/* padding: 1rem 1rem 1rem 1rem; */
}

.main{
	float: left; 
    width: 100%;
	/* background-color: black */
	background-color: #F2F1EE;
	/*padding: 1rem 1rem 1rem 1rem;*/
}

.overlay {
	/* width: 60%;  */
	z-index: 0;
	margin: -2px;
	/* background: #009938; */
	position: relative;
	}


</style>
