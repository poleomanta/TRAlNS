<script lang="ts">
  import { browser } from "$app/environment";
    import { onMount } from "svelte";

  interface Props {
    lat: number;
    lon: number;
  }

  let {
    lat,
    lon
  }: Props = $props();

  let container: HTMLElement | undefined = $state<HTMLLegendElement | undefined>();

  onMount(() => {
    if (!browser) return;
    // @ts-ignore
    const map = L.map(container).setView([lat, lon], 13);
    // @ts-ignore
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    // @ts-ignore
    L.marker([lat, lon]).addTo(map);
  });
</script>

<style lang="scss">
  .map {
    width: 100%;
    height: 20em;
    display: block;
    display: flex;
    justify-content: space-around;
    padding: 1em;
    border-radius: 0.75em;
  }

  .map :global(.marker-text) {
		width:100%;
		text-align:center;
		font-weight:600;
		background-color:#444;
		color:#EEE;
		border-radius:0.5rem;
	}
	
	.map :global(.map-marker) {
		width:30px;
		transform:translateX(-50%) translateY(-25%);
	}
</style>

<div class="map" bind:this={container}></div>