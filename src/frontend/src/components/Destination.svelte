<script lang="ts">
    import Tag from "./Tag.svelte";
    import Row from "./Row.svelte";
    import Map from "./Map.svelte";
    import Subtitle from "./Subtitle.svelte";
    import { AmenityModel, DestinationModel } from "$lib/classes";
    import { Armchair, GlassWater, Info, Minus, Plus, Toilet } from "@lucide/svelte";
    import {
        addDestinationToPlan,
        removeDestinationFromPlanByDestination,
        isInPlan,
        getPlan,
        PlanModel,
    } from "$lib/planner.svelte";
    import { onMount } from "svelte";
    import { browser } from "$app/environment";
    import IconButton from "./IconButton.svelte";
    import Spinner from "./Spinner.svelte";

    interface Props {
        destination: DestinationModel;
        showMap?: boolean;
        amenityLoadCallback?: (amenities: Record<string, AmenityModel>) => void;
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

    let infoShown = $state(false)
    let amenitiesByType = $state<Record<string, AmenityModel>>({});
    let loadingAmenities = $state(false);

    const iconForAmenityType: Record<string, typeof Armchair> = {
        "WC": Toilet,
        "REST": Armchair,
        "FOUNTAIN": GlassWater
    }

    const amenityTypes = ["FOUNTAIN", "REST", "WC"];

    async function toggleInfo() {
        infoShown = !infoShown;

        if (infoShown && Object.keys(amenitiesByType).length === 0) {
            loadingAmenities = true;
            const amenities = await fetch(`/api/amenities?lat=${destination.lat}&lon=${destination.lon}`).then(res => res.json());
            loadingAmenities = false;
            // @ts-ignore
            amenitiesByType = Object.fromEntries(amenities.map(x => [x.kind, x]));
            amenityLoadCallback(amenitiesByType);
        }
    }
    let { destination, showMap=true, amenityLoadCallback=(() => {}) }: Props = $props();
</script>

<div class="card">
    {#if showMap}
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
    <Map lat={destination.lat} lon={destination.lon} amenities={amenitiesByType} />
    <Row right={true}>
        <IconButton click={toggleInfo}>
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
    {:else}
    <div class="grid">
        <Subtitle>
            {destination.name}
        </Subtitle>
        <Tag name={destination.tag} />
        <Row right={true}>
            <IconButton click={toggleInfo}>
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
    {#if destination.description}
        <div class="description">
            {destination.description}
        </div>
    {/if}
    {/if}


    {#if infoShown}
        <div class="info">
            {#if loadingAmenities}
            <Spinner/>
            {/if}
            {#each amenityTypes as type}
                {#if amenitiesByType[type]}
                    <Row>
                        {@const Icon = iconForAmenityType[type]}
                        <Icon />
                        <span>
                            {#if type === "WC"} Restroom {/if}
                            {#if type === "REST"} Rest Area {/if}
                            {#if type === "FOUNTAIN"} Drinkable Water {/if}
                        </span>
                        •
                        <span>
                            {amenitiesByType[type].locations.length} nearby
                        </span>
                    </Row>
                {/if}
            {/each}
        </div>
    {/if}
</div>

<style lang="scss">
    div.card {
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
    div.grid {
        display: grid;
        grid-template-columns: 1fr auto auto auto;
        align-items: center;
        gap: 0.5em;
        width: 100%;
    }
</style>
