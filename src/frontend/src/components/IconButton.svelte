<script lang="ts">
  import type { Snippet } from "svelte";

  import { NoOp } from "$lib/placeholders";

  interface Props {
    up?: () => void;
    down?: () => void;
    click?: () => void;
    visible?: boolean;
    style?: string;
    tabindex?: number;
    href?: string;
    children?: Snippet;
  }

  let {
    up = NoOp,
    down = NoOp,
    click = NoOp,
    visible = true,
    style = "",
    tabindex = 0,
    href = "",
    children
  }: Props = $props();

  // svelte-ignore non_reactive_update
  // isLink is set once and never changed
  let button = $state<HTMLElement | null>(null);

  function clickInternal(e: MouseEvent) {
    e.stopPropagation();
    click();
  }

  function leaveInternal() {
    if (!button) return;
    button.blur();
    up();
  }
  function upInternal() {
    if (!button) return;
    button.blur();
    up();
  }
</script>

<style lang="scss">
  button, a {
    all: unset;
    border-radius: 50%;
    display: flex;
    align-items: center;
    padding: .5em;
    cursor: pointer;
    position: relative;
    transition: all ease-in-out .3s;
  }

  button.hidden, a.hidden {
    visibility: hidden;
  }

  div.circle {
    position: absolute;
    background-color: blue;
    z-index: -1;
    border-radius: 50%;
    left: 50%;
    top: 50%;
    width: 0%;
    height: 0%;
    transition: all ease-in-out .3s;
    pointer-events: none;
  }

  button:hover div.circle, button:focus div.circle, a:hover div.circle, a:focus div.circle {
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
  }

  button:active div.circle, a:active div.circle {
    width: 125%;
    height: 125%;
    left: -12.5%;
    top: -12.5%;
  }
</style>

{@render buttonSnippet()}

{#snippet buttonSnippet()}
  {#if href !== ""}
    <a
      bind:this={button}
      class:hidden={!visible}
      href={href}
      style={style}
      tabindex="{tabindex}"
    >
      <div class="circle"></div>
      {@render children?.()}
    </a>
  {:else}
    <button
      bind:this={button}
      onclick={clickInternal}
      onmousedown={down}
      onmouseleave={leaveInternal}
      onmouseup={upInternal}
      class:hidden={!visible}
      type="button"
      style={style}
      tabindex="{tabindex}"
    >
      <div class="circle"></div>
      {@render children?.()}
    </button>
  {/if}
{/snippet}