<script>
	import Header from './Header.svelte';
	import '../app.css';
</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>


</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		/* padding: 1rem; */
		 /* No top padding to prevent gab between header and main view */
		padding-right: 1rem;
		padding-left: 1rem;
		padding-bottom: 1rem;
		width: 100%;
		/* max-width: 64rem; Creation of border div's on page */
		margin: 0 auto;
		box-sizing: border-box;
	}

</style>
