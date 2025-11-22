<script lang="ts" generics="T">
    import type { Snippet } from 'svelte';
    import Row from './Row.svelte';
    import IconButton from './IconButton.svelte';
    import { ChevronLeft, ChevronRight } from '@lucide/svelte';

  interface Props {
    elements: T[];
    children: Snippet<[item: T]>;
  }

  let { elements, children }: Props = $props();

  const count = $derived(elements.length);
  let currentPage = $derived(1);

  const elementsPerPage = 10;
  let currentElements = $derived(
    elements.slice(
      (currentPage - 1) * elementsPerPage,
      currentPage * elementsPerPage,
    ),
  );
</script>

<style lang="scss">
  div.page {
    gap: 0.5em;
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  div.pageNumber {
    width: 5em;
    text-align: center;
  }
</style>

{#snippet pageButtons()}
  <Row centered={true}>
    <IconButton click={() => {
        if (currentPage > 1) {
            currentPage = currentPage - 1;
        }
    }} disabled={currentPage === 1}>
      <ChevronLeft />
    </IconButton>
    <div class="pageNumber">
      {currentPage} of {Math.ceil(count / elementsPerPage)}
    </div>
    <IconButton click={() => {
        if (currentPage < Math.ceil(count / elementsPerPage)) {
            currentPage = currentPage + 1;
        }
    }} disabled={currentPage === Math.ceil(count / elementsPerPage)}>
      <ChevronRight />
    </IconButton>
  </Row>
{/snippet}

<div class="page">
  {@render pageButtons()}
  {#each currentElements as element, index (currentPage * elementsPerPage + index)}
    {@render children(element)}
  {/each}
  {@render pageButtons()}
</div>