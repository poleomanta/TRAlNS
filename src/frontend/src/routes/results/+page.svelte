<script lang="ts">
    import { DestinationModel } from "$lib/classes";
    import type { PageProps } from "../$types";
    import Destination from "../../components/Destination.svelte";
    import Subtitle from "../../components/Subtitle.svelte";
    import Title from "../../components/Title.svelte";
    import Pagination from "../../components/Pagination.svelte";
    import Column from "../../components/Column.svelte";
    import Row from "../../components/Row.svelte";
    import Search from "../../components/Search.svelte";
    import { onMount } from "svelte";
    import { page } from "$app/state";

    let { data }: PageProps = $props();

    // @ts-ignore
    const destinations = data.destinations as DestinationModel[];

    let searchText = $state<string>("");
    onMount(() => {
        searchText = page.url.searchParams.get("search") || "";
    });
</script>

<Row centered={true}>
    <Title>Things you might like</Title>
</Row>
<Search bind:searchText={searchText}/>
<Pagination elements={destinations}>
    {#snippet children(destination: DestinationModel)}
        <Destination {destination} />
    {/snippet}
</Pagination>

<style>
</style>
