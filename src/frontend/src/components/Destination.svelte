<script lang="ts">
    import hash from "hash.js";
    import type { Snippet } from "svelte";
    import Tag from "./Tag.svelte";
    import Row from "./Row.svelte";
    import Map from "./Map.svelte";
    import Subtitle from "./Subtitle.svelte";
    import { DestinationModel } from "$lib/classes";
    import { Plus } from "@lucide/svelte";
    import { addDestinationToPlan } from "$lib/planner";

    interface Props {
        destination: DestinationModel;
    }

    let { destination }: Props = $props();
</script>

<div>
    {#if destination.name}
        <Subtitle>
            {destination.name}
        </Subtitle>

        <Row spaceBetween={true}>
            <Tag name={destination.tag} />
            {#if destination.website}
                <a href={destination.website}> Destination website </a>
            {/if}
        </Row>
    {/if}

    {#if destination.description}
        <div class="description">
            {destination.description}
        </div>
    {/if}

    <Map lat={destination.lat} lon={destination.lon} />
    <button
        onclick={() => {
            addDestinationToPlan(destination);
        }}><Plus />Add to planned destinations</button
    >
</div>

<style lang="scss">
    div {
        all: unset;
        height: auto;
        padding: 1em 1em;
        border-radius: 0.75em;
        width: auto;
        display: flex;
        flex-direction: column;
        gap: 1em;
        background-color: hsl(0, 0%, 95%);
    }
    .description {
        background-color: hsl(0, 0%, 98%);
    }
    button {
        all: unset;
        cursor: pointer;
        display: flex;
        justify-content: end;
        align-items: center;
        gap: 0.25em;
        flex-direction: row;
        transition: transform ease-in-out 0.5s;
    }
    button:hover {
        transform: scale(1.1) translate(-3%, -3%);
    }
</style>
