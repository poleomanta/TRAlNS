<script lang="ts">
    import type { DestinationModel } from "$lib/classes";
    import type { PageProps } from "../$types";
    import Destination from "../../components/Destination.svelte";
    import Subtitle from "../../components/Subtitle.svelte";

    let { data }: PageProps  = $props();

    // @ts-ignore
    const destinations = data.destinations as DestinationModel[];
</script>

<Subtitle>Things you might like</Subtitle>
<div>
    {#each destinations as d}
        <Destination destination={d} />
    {/each}
</div>
