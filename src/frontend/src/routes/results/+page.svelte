<script lang="ts">
    import { DestinationModel } from "$lib/classes";
    import type { PageProps } from "../$types";
    import Destination from "../../components/Destination.svelte";
    import Subtitle from "../../components/Subtitle.svelte";
    import Title from "../../components/Title.svelte";
    import Pagination from "../../components/Pagination.svelte";
    import Column from "../../components/Column.svelte";
    import Row from "../../components/Row.svelte";

    let { data }: PageProps = $props();

    // @ts-ignore
    const destinations = data.destinations as DestinationModel[];
</script>

<Row centered={true}>
    <Title>Things you might like</Title>
</Row>
<Pagination elements={destinations}>
    {#snippet children(destination: DestinationModel)}
        <Destination {destination} />
    {/snippet}
</Pagination>

<style>
</style>
