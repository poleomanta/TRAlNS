<script>
    import Subtitle from "../../components/Subtitle.svelte";
    import Column from "../../components/Column.svelte";
    import Destination from "../../components/Destination.svelte";
    import { getPlan } from "$lib/planner.svelte";
    import { derived } from "svelte/store";
    import { browser } from "$app/environment";

    let destinations = $derived.by(() => {
        if (browser) return getPlan().destinations;
        return [];
    });
</script>

<Subtitle>My planned destinations</Subtitle>
<Column>
    {#each destinations as d}
        <Destination destination={d} />
    {/each}
</Column>
