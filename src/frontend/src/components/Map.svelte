<script lang="ts">
  import { browser } from "$app/environment";
    import { decodePolyline } from "$lib/util";
  import { onMount } from "svelte";
  interface Props {
    lat: number;
    lon: number;
    route?: any;
  }

  let { lat, lon, route }: Props = $props();

  let container: HTMLElement | undefined = $state<
    HTMLLegendElement | undefined
  >();

  //@ts-ignore
  function renderLine(route) {
    console.log('rendering line')
    const decodedGeometry = decodePolyline(route.geometry, false);
    let newGeometry = [];
    for (let point of decodedGeometry) newGeometry.push([point[1], point[0]]);
    return {
      type: "Feature",
      properties: {
        name: "Your Route",
      },
      geometry: {
        type: "LineString",
        coordinates: newGeometry,
      },
    };
  }
  
  let map: any = $state<any>(null);

  onMount(() => {
    if (!browser) return;
    // @ts-ignore
    map = L.map(container).setView([lat, lon], 13);

    // @ts-ignore
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);
    // @ts-ignore
    L.marker([lat, lon]).addTo(map);
  });

  const myStyle = {
    "color": "#ea5b06",
    "weight": 7,
    "opacity": 0.65
  };
  $effect(() => {
    if (route == undefined || map == null) return;
    //@ts-ignore
    L.geoJSON(renderLine(route), {
      style: myStyle,
    }).addTo(map);
  })
</script>

<div class="map" bind:this={container}></div>

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
    width: 100%;
    text-align: center;
    font-weight: 600;
    background-color: #444;
    color: #eee;
    border-radius: 0.5rem;
  }

  .map :global(.map-marker) {
    width: 30px;
    transform: translateX(-50%) translateY(-25%);
  }
</style>
