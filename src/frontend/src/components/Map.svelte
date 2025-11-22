<script lang="ts">
  import { browser } from "$app/environment";
  import type { AmenityModel, DestinationModel } from "$lib/classes";
  import { decodePolyline } from "$lib/util";
  import { onMount } from "svelte";
  interface Props {
    lat: number;
    lon: number;
    route?: any;
    destinations?: DestinationModel[];
    amenities?: Record<string, AmenityModel>;
  }

  let { lat, lon, route, destinations, amenities }: Props = $props();

  let container: HTMLElement | undefined = $state<
    HTMLLegendElement | undefined
  >();

  //@ts-ignore
  function renderLine(decodedGeometry) {
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
    if (!destinations || destinations?.length === 0) L.marker([lat, lon]).addTo(map);
    else {
      for (let dest of destinations) {
        // @ts-ignore
        L.marker([dest.lat, dest.lon]).addTo(map);
      }
    }
  });

  const myStyle = {
    "color": "#ea5b06",
    "weight": 7,
    "opacity": 0.65
  };
  $effect(() => {
    if (route == undefined || map == null) return;
    const decodedGeometry = decodePolyline(route.geometry, false);
    //@ts-ignore
    L.geoJSON(renderLine(decodedGeometry), {
      style: myStyle,
    }).addTo(map);
  })

  $effect(() => {
    if (!amenities || map == null || Object.keys(amenities).length === 0) return;
    // @ts-ignore
    let toiletIcon = L.icon({
        iconUrl: 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXRvaWxldC1pY29uIGx1Y2lkZS10b2lsZXQiPjxwYXRoIGQ9Ik03IDEyaDEzYTEgMSAwIDAgMSAxIDEgNSA1IDAgMCAxLTUgNWgtLjU5OGEuNS41IDAgMCAwLS40MjQuNzY1bDEuNTQ0IDIuNDdhLjUuNSAwIDAgMS0uNDI0Ljc2NUg1LjQwMmEuNS41IDAgMCAxLS40MjQtLjc2NUw3IDE4Ii8+PHBhdGggZD0iTTggMThhNSA1IDAgMCAxLTUtNVY0YTIgMiAwIDAgMSAyLTJoOGEyIDIgMCAwIDEgMiAydjgiLz48L3N2Zz4=',
        iconSize: [20, 20],
        iconAnchor: [10, 10],
        popupAnchor: [0, 0],
        shadowUrl: 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAzNiAzNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9Imljb25pZnkgaWNvbmlmeS0tdHdlbW9qaSIgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+PGNpcmNsZSBmaWxsPSIjRTZFN0U4IiBjeD0iMTgiIGN5PSIxOCIgcj0iMTgiPjwvY2lyY2xlPjwvc3ZnPg==',
        shadowSize: [20, 20],
        shadowAnchor: [10, 10],
    });
    // @ts-ignore
    let restIcon = L.icon({
        iconUrl: 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWFybWNoYWlyLWljb24gbHVjaWRlLWFybWNoYWlyIj48cGF0aCBkPSJNMTkgOVY2YTIgMiAwIDAgMC0yLTJIN2EyIDIgMCAwIDAtMiAydjMiLz48cGF0aCBkPSJNMyAxNmEyIDIgMCAwIDAgMiAyaDE0YTIgMiAwIDAgMCAyLTJ2LTVhMiAyIDAgMCAwLTQgMHYxLjVhLjUuNSAwIDAgMS0uNS41aC05YS41LjUgMCAwIDEtLjUtLjVWMTFhMiAyIDAgMCAwLTQgMHoiLz48cGF0aCBkPSJNNSAxOHYyIi8+PHBhdGggZD0iTTE5IDE4djIiLz48L3N2Zz4=',
        iconSize: [20, 20],
        iconAnchor: [10, 10],
        popupAnchor: [0, 0],
        shadowUrl: 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAzNiAzNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9Imljb25pZnkgaWNvbmlmeS0tdHdlbW9qaSIgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+PGNpcmNsZSBmaWxsPSIjRTZFN0U4IiBjeD0iMTgiIGN5PSIxOCIgcj0iMTgiPjwvY2lyY2xlPjwvc3ZnPg==',
        shadowSize: [20, 20],
        shadowAnchor: [10, 10],
    });
    // @ts-ignore
    let waterIcon = L.icon({
        iconUrl: 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWdsYXNzLXdhdGVyLWljb24gbHVjaWRlLWdsYXNzLXdhdGVyIj48cGF0aCBkPSJNNS4xMTYgNC4xMDRBMSAxIDAgMCAxIDYuMTEgM2gxMS43OGExIDEgMCAwIDEgLjk5NCAxLjEwNUwxNy4xOSAyMC4yMUEyIDIgMCAwIDEgMTUuMiAyMkg4LjhhMiAyIDAgMCAxLTItMS43OXoiLz48cGF0aCBkPSJNNiAxMmE1IDUgMCAwIDEgNiAwIDUgNSAwIDAgMCA2IDAiLz48L3N2Zz4=',
        iconSize: [20, 20],
        iconAnchor: [10, 10],
        popupAnchor: [0, 0],
        shadowUrl: 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAzNiAzNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9Imljb25pZnkgaWNvbmlmeS0tdHdlbW9qaSIgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+PGNpcmNsZSBmaWxsPSIjRTZFN0U4IiBjeD0iMTgiIGN5PSIxOCIgcj0iMTgiPjwvY2lyY2xlPjwvc3ZnPg==',
        shadowSize: [20, 20],
        shadowAnchor: [10, 10],
    });
    for (let key in amenities) {
      const amenity = amenities[key];
      switch (amenity.kind) {
        case "WC":
          var icon = toiletIcon;
          break;
        case "REST":
          var icon = restIcon;
          break;
        case "FOUNTAIN":
          var icon = waterIcon;
          break;
      }
      for (const loc of amenity.locations) {
        // @ts-ignore
        L.marker([loc.lat, loc.lon], {icon: icon}).addTo(map)
      }
    }
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
