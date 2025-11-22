<script lang="ts">
    import hash from "hash.js";
    import type { Snippet } from "svelte";
    import Tag from "./Tag.svelte";
    import Row from "./Row.svelte";
    import Subtitle from "./Subtitle.svelte";
    import { DestinationModel } from "$lib/classes";

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
    {:else}
        <Subtitle>
            {destination.tag}
        </Subtitle>
        {#if destination.website}
            <a href={destination.website}> Destination website </a>
        {/if}
    {/if}
    {#if destination.description}
        <div class="description">
            {destination.description}
        </div>
    {/if}
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
</style>
