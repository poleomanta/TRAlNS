<script lang="ts">
    import Tag from "./Tag.svelte";
    import Row from "./Row.svelte";
    import Map from "./Map.svelte";
    import Subtitle from "./Subtitle.svelte";
    import { DestinationModel } from "$lib/classes";
    import { Info, Minus, Plus } from "@lucide/svelte";
    import {
        addDestinationToPlan,
        removeDestinationFromPlanByDestination,
        isInPlan,
        getPlan,
        PlanModel,
    } from "$lib/planner.svelte";
    import { onMount } from "svelte";
    import { browser } from "$app/environment";
    import { disableScrollHandling } from "$app/navigation";
    import IconButton from "./IconButton.svelte";

    interface Props {
        destination: DestinationModel;
    }

    let plan = $state(new PlanModel([]));
    onMount(() => {
        if (!browser) return;
        plan = getPlan();
    });
    function refreshPlan() {
        plan = getPlan();
    }
    // @ts-ignore
    let inPlan = $derived.by(() => {
        if (!browser) return false;
        plan;
        return isInPlan(destination);
    });

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
    <Row right={true}>
        <IconButton>
            <Info />
        </IconButton>
        {#if !inPlan}
            <IconButton
                click={() => {
                    addDestinationToPlan(destination);
                    refreshPlan();
                }}
                ><Plus />
            </IconButton>
        {:else}
            <IconButton
                click={() => {
                    removeDestinationFromPlanByDestination(destination);
                    refreshPlan();
                }}
                ><Minus />
            </IconButton>
        {/if}
    </Row>
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
        transition: transform ease-in-out 0.2s;
    }
    button:hover {
        transform: scale(1.1) translate(-3%, -3%);
    }
</style>
