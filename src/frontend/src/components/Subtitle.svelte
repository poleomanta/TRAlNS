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
  h2 {
    font-family: "Fugaz One", ;
    font-style: normal;
    font-weight: 500;
    font-size: 1.1rem;
    margin: 0;
    max-width: 100%;
    hyphens: auto;
  }
</style>

<h2>
  {@render children()}
</h2>