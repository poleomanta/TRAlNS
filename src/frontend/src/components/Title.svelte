<script lang="ts">
  import type { Snippet } from "svelte";

  interface Props {
    children: Snippet;
  }

  let { children }: Props = $props();
</script>

<h1>
  {@render children()}
</h1>

<style lang="scss">
  h1 {
    font-family: "Fugaz One";
    font-style: normal;
    font-weight: 500;
    font-size: 2rem;
    margin: 0;
    max-width: 100%;
    hyphens: auto;
  }
</style>
