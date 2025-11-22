<script lang="ts">
    import hash from "hash.js";
    import type { Snippet } from "svelte";

    interface Props {
        name: string;
    }

    let { name }: Props = $props();

    let hue = $derived(
        (parseInt(hash.sha1().update(name).digest("hex").slice(0, 2), 16) /
            255) *
            360,
    );
    let color = $derived(`hsl(${hue}, 25%, 90%)`);

    let displayName = $derived(
        name.split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')
    );
</script>

<a style={`background-color:${color};`} href={`/results?tag=${name}`}>
    {displayName}
</a>

<style lang="scss">
    a {
        all: unset;
        height: 1.5em;
        padding: 0.2em 0.5em;
        border-radius: 0.75em;
        width: auto;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: transform ease-in-out .1s;
    }

    a:hover {
        transform: scale(1.1) translate(-1%, 0%);
    }
</style>
