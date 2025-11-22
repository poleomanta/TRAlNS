<script lang="ts">
    import { DestinationModel } from "$lib/classes";
    import type { PageProps } from "../$types";
    import Destination from "../../components/Destination.svelte";
    import Subtitle from "../../components/Subtitle.svelte";
    import Pagination from "../../components/Pagination.svelte";
    import Column from "../../components/Column.svelte";

    let { data }: PageProps = $props();

    // @ts-ignore
    const destinations = data.destinations as DestinationModel[];
</script>

<Subtitle>Things you might like</Subtitle>
<Pagination elements={destinations}>
    {#snippet children(destination: DestinationModel)}
        <Destination {destination} />
    {/snippet}
</Pagination>
