<script lang="ts">
    import Subtitle from "../../components/Subtitle.svelte";
    import Column from "../../components/Column.svelte";
    import Destination from "../../components/Destination.svelte";
    import { getPlan } from "$lib/planner.svelte";
    import { derived } from "svelte/store";
    import { browser } from "$app/environment";
    import { POST } from "../api/[...endpoint]/+server";
    import { CoordinatesModel } from "$lib/classes";
    import { latLng } from "leaflet";
    import Map from "../../components/Map.svelte";

    let destinations = $derived.by(() => {
        if (browser) return getPlan().destinations;
        return [];
    });

    let route: CoordinatesModel[] | undefined = $state<CoordinatesModel[] | undefined>();

    $effect(() => {
        if (destinations == []) return undefined;
        const r = await fetch("/api/routes", {
            method: "POST",
            body: JSON.stringify(
                getPlan().destinations.map(
                    (dest) => new CoordinatesModel(dest.lat, dest.lon),
                ),
            ),
        });
        console.log(r);
    });

    $effect(() => {
        console.log(JSON.stringify(route, null, 2));
    });
</script>

<Map
    lat={getPlan().destinations[0].lat}
    lon={getPlan().destinations[0].lon}
    {route}
></Map>
<Subtitle>My planned destinations</Subtitle>
<Column>
    {#each destinations as d}
        <Destination destination={d} />
    {/each}
</Column>
