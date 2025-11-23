<script lang="ts">
  import IconButton from "./IconButton.svelte";
    import { Send } from "@lucide/svelte";

  interface Props {
    searchText?: string;
  }

  let {
    searchText = $bindable("")
  }: Props = $props();

  let lastRequest = $state(0);
  let requestTimer = $state<ReturnType<typeof setTimeout> | null>(null);
  let autocompletions = $state<string[]>([]);
  function inputChange(event: Event) {
    const target = event.target as HTMLInputElement;
    searchText = target.value;

    if (searchText.length < 4) return;
    if (requestTimer) {
      clearTimeout(requestTimer);
    }
    const currentTime = Date.now();
    const timeSinceLastRequest = currentTime - lastRequest;
    const delay = Math.max(0, 1000 - timeSinceLastRequest);
    requestTimer = setTimeout(async () => {
      lastRequest = Date.now();
      const autocompleteResults = await fetch(`/api/autocomplete?query=${encodeURIComponent(searchText)}`);
      const jsonResults = await autocompleteResults.json();
      const mappedResults = jsonResults.features.map((item: any) => item.properties);
      const filteredResults = mappedResults.filter((item: any) => item.locality === "Munich");
      autocompletions = filteredResults.map((item: any) => item.name);
    }, delay);
  }
</script>

<style lang="scss">
  .inputContainer {
    height: 1.5em;
    flex-grow: 1;
    width: 100%;
    position: relative;
    margin-right: .5em;
    margin-top: -.45em;
  }
  input {
    all: unset;
    background-color: hsl(0, 0%, 90%);
    height: 1.5em;
    padding: .2em .5em;
    border-radius: .75em;
    flex-grow: 1;
    width: 100%;
  }
  form {
    display: flex;
    gap: .5em;
    width: 100%;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .inputContainer:focus-within ul, .inputContainer:hover ul {
    display: block;
  }
  ul {
    display: none;
    position: absolute;
    left: 0;
    right: 0;
    top: calc(100% + 8px);
    background: white;
    border-radius: .75em;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    max-height: 7em;
    overflow: auto;
    width: calc(100% + 1em);
    margin: 0;
    list-style: none;
    z-index: 500000;
    padding: 0;
  }
  li {
    padding: .5em .6em;
    cursor: pointer;
    left: 0;
  }
</style>

<form onsubmit={() => {
  window.location.href = `/results?search=${encodeURIComponent(searchText)}`;
}}>
  <div class="inputContainer">
    <input
      type="text"
      placeholder="What do you want to see today..."
      bind:value={searchText}
      oninput={inputChange}
      autocomplete="off"
      aria-autocomplete="list"
      aria-controls="autocomplete-list"
      aria-expanded={autocompletions.length > 0}
    />

    {#if autocompletions.length > 0}
      <ul id="autocomplete-list" role="listbox">
        {#each autocompletions as suggestion, i}
          <li
            role="option"
            onmousedown={(e) => { e.preventDefault(); searchText = suggestion; autocompletions = []; window.location.href = `/results?search=${encodeURIComponent(searchText)}`; }}
          >
            {suggestion}
          </li>
        {/each}
      </ul>
    {/if}
  </div>

  <IconButton href={`/results?search=${encodeURIComponent(searchText)}`}>
    <Send/>
  </IconButton>
</form>
