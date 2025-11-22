<script lang="ts">
    import Subtitle from "../../components/Subtitle.svelte";
    import Column from "../../components/Column.svelte";
    import Destination from "../../components/Destination.svelte";
    import { getPlan } from "$lib/planner.svelte";
    import { browser } from "$app/environment";
    import { CoordinatesModel } from "$lib/classes";
    import Map from "../../components/Map.svelte";
    import { onMount } from "svelte";
    import Title from "../../components/Title.svelte";
    import Row from "../../components/Row.svelte";

    let destinations = $derived.by(() => {
        if (browser) return getPlan().destinations;
        return [];
    });

    let route: CoordinatesModel[] | undefined = $state<CoordinatesModel[] | undefined>();

    onMount(async () => {
        const r = await fetch("/api/routes", {
            method: "POST",
            body: JSON.stringify(
                getPlan().destinations.map(
                    (dest) => new CoordinatesModel(dest.lat, dest.lon),
                ),
            ),
        });
        const rjson = await r.json();
        route = rjson.routes[0];
    })

   let amenitiesByType = $state<Record<string, any>>({}); 
</script>

<Row centered={true}>
<Title>My planned destinations</Title>
</Row>
{#if destinations.length == 0}
    <p>No destinations in your plan yet. Go to the search page to add some!</p>
{:else}
    <Map
        lat={destinations[0].lat}
        lon={destinations[0].lon}
        {route}
        destinations={destinations}
        amenities={amenitiesByType}
    ></Map>
    <Column>
        {#each destinations as d}
            <Destination destination={d} showMap={false} amenityLoadCallback={(amenities) => { amenitiesByType = amenities; }} />
        {/each}
    </Column>
{/if}
