<script lang="ts">
  import IconButton from "./IconButton.svelte";
    import { Send } from "@lucide/svelte";

  interface Props {
    searchText?: string;
  }

  let {
    searchText = $bindable("")
  }: Props = $props();
</script>

<style lang="scss">
  input {
    all: unset;
    background-color: hsl(0, 0%, 90%);
    height: 1.5em;
    padding: .2em .5em;
    border-radius: .75em;
    flex-grow: 1;
  }
  form {
    display: flex;
    gap: .5em;
    width: 100%;
    flex-direction: row;
  }
</style>

<form onsubmit={() => {
  window.location.href = `/results?search=${encodeURIComponent(searchText)}`;
}}>
  <input type="text" placeholder="What do you want to see today..." bind:value={searchText}/>
  <IconButton href={`/results?search=${encodeURIComponent(searchText)}`}>
    <Send/>
  </IconButton>
</form>
