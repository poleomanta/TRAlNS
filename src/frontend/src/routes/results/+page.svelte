<script lang="ts">
    import { DestinationModel } from "$lib/classes";
    import Column from "../../components/Column.svelte";
    import type { PageProps } from "../$types";
    import Destination from "../../components/Destination.svelte";
    import Title from "../../components/Subtitle.svelte";

    let { data }: PageProps = $props();

    // @ts-ignore
    const destinations = data.destinations as DestinationModel[];
</script>

<Title>Things you might like</Title>
<Column>
    {#each destinations as d}
        <Destination destination={d} />
    {/each}
</Column>
