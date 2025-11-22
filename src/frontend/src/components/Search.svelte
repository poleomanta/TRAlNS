<script lang="ts">
  import type { Snippet } from "svelte";

  interface Props {
  }

  let {
  }: Props = $props();
</script>

<style lang="scss">
  input {
    all: unset;
    background-color: hsl(0, 0%, 90%);
    height: 1.5em;
    padding: .2em .5em;
    border-radius: .75em;
  }
</style>

<input type="text" placeholder="What do you want to see today..." />
