<script lang="ts">
  import type { Snippet } from "svelte";

  interface Props {
    children: Snippet;
    spaceBetween?: boolean;
    centered?: boolean;
  }

  let { children, spaceBetween = false, centered = false }: Props = $props();
</script>

<div class:spaceBetween class:centered>
  {@render children()}
</div>

<style lang="scss">
  div {
    gap: 0.5em;
    display: flex;
    flex-direction: row;
    width: 100%;
    flex-wrap: wrap;
  }
  .spaceBetween {
    justify-content: space-between;
    align-items: center;
  }
  .centered {
    justify-content: center;
    align-items: center;
  }
</style>
