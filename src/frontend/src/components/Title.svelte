<script lang="ts">
  import type { Snippet } from "svelte";

  interface Props {
    children: Snippet;
  }

  let {
    children
  }: Props = $props();
</script>

<style lang="scss">
  h1 {
    font-family: "Fugaz One", ;
    font-style: normal;
    font-weight: 500;
    font-size: 1.5rem;
    margin: 0;
    max-width: 100%;
    hyphens: auto;
  }
</style>

<h1>
  {@render children()}
</h1>