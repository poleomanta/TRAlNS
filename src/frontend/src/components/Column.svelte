<script lang="ts">
  import type { Snippet } from "svelte";

  interface Props {
    children: Snippet;
    spaceBetween?: boolean;
  }

  let { children, spaceBetween = false }: Props = $props();
</script>

<div class:spaceBetween>
  {@render children()}
</div>

<style lang="scss">
  div {
    gap: 0.5em;
    display: flex;
    flex-direction: column;
    width: 100%;
  }
  .spaceBetween {
    justify-content: space-between;
    align-items: center;
  }
</style>
