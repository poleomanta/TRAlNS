<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
    import Search from '../components/Search.svelte';
    import Subtitle from '../components/Subtitle.svelte';
    import Title from '../components/Title.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<style lang="scss">
	:global(*) {
		font-family: "Atkinson Hyperlegible Next", sans-serif;
		font-optical-sizing: auto;
		font-style: normal;
		box-sizing: border-box;
		font-size: 1.1rem;
	}

	:global(body) {
		margin: 0;
	}

	main {
		gap: .5em;
		display: flex;
		flex-direction: column;
		background-color: white;
		min-height: 100vh;
		padding: 2em max(2em, calc((100% - 25em) / 2));
		justify-content: center;
	}
</style>

<main>
	<img src="/img/munich.jpg" alt="Munich skyline" />
	<Title>
		TRAlNS
	</Title>
	<Subtitle>
		Munich sightseeing made simple
	</Subtitle>
	<Search/>
</main>
