<script>
	// import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="text-column">
	<h1>Visualizing Event Sequences</h1>

	<h3>Explanation of data and components in the visualization. </h3>

	<!-- https://github.com/d3/d3-sankey/blob/master/src/sankey.js -->

	<p>
		MIT univerity gathered the phone logs of a hundred people for an academic year. 
		With (anynomized) information regarding calls, messages, and data usage.
		Below a list of tasks is given to see if you can find an answer or explanation. Sometimes the answer is not clear from the data. 


	</p>

	<h3>
		Tasks
	</h3>
	<p>Try to select Sloan affiliation (a research group) and compare against the other student groups.</p>
			<p>Can you find the people (case-Id’s) who dropped out of the experiment?</p>
		
		
		<p>For fun: Can you create an event attribute visualization with the more than 8 colors?</p>
		<p>Disclaimer: TBR are missing values.
		</p>
	<h3>Other tasks</h3>
	<p>
		Q1 Why would some people have few digital communications like calls and
text messages?</p><p>
– Does the person work part-time?</p><p>
– Does the person have few friends or are they lonely?</p><p>
– Does the person prefer in-person communication?</p><p>
Q2 If present, what are the communication style patterns in events?</p><p>
– Does first communication lower the threshold and allow for con-
tinued communication?</p><p>
– Or does it occur like conversations, shortly following messages</p><p>
with larger pauses in between?</p><p>
– Or just once in a while a single message.</p><p>
Q3 Do people exhibit a strong preference for either calls or messages? (How
are outgoing voice calls and messages distributed?)</p><p>
Q4 Are people dissatisfied with their friend groups more hesitant to contact
anyone? Is there a difference between strangers and friends?</p><p>
Q5 Do groups or affiliations exhibit different behavior? Are there differences between inter- and intra-group communication?</p><p>
Q6 Do phone use and communication styles match</p><p>
– For everyone</p><p>
– In groups / affiliations</p><p>
– Between friends</p><p>
– Are there people who accommodate another’s communication style?</p><p>
How does this affect them?</p><p>
Q7 When somebody is contacted often by people outside of contact, is this
person something like a broker?</p><p>
– Do they have some responsibilities at work meaning they get contacted for work-related things?</p><p>
– Does the person have outgoing calls to numbers outside of contactsbesides directly calling back after a (missed) call? Then the person
might just not store contacts in their phone.</p><p>
Q8 Do friends reciprocate friendships or is it one-sided?</p><p>
– In general: can people distinguish friendships?</p><p>
– Is there one person bad at distinguishing friends?</p><p>
– Others found shared location outside of working hours could be agood indicator of friendships. Does this person spend time outside
of work hours with people?</p><p>
Q9 Does proximity to work or friends ease friendship?</p><p>
Q10 Do people socialize and create friendships mainly within groups or affiliations?</p><p>
Q11 Are longer calls more effective than shorter calls? Do they have fewer</p><p>
follow-up calls? Do longer calls then total to a lower total duration?</p><p>
Could also be less efficient and contain social talks.
	</p>

	
	
</div>

<!-- 
<section>
	<h1>
		<span class="welcome">
			<picture>
				<source srcset={welcome} type="image/webp" />
				<img src={welcome_fallback} alt="Welcome" />
			</picture>
		</span>

		to your new<br />SvelteKit app
	</h1>

	<h2>
		try editing <strong>src/routes/+page.svelte</strong>
	</h2> -->

	<!-- <Counter />
</section> -->

<!-- <style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style> -->
