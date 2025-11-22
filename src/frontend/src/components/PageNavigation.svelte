<script lang="ts">
    import { House, NotebookPen, SearchIcon } from "@lucide/svelte";


</script>

<style lang="scss">
  nav {
    display: flex;
    flex-direction: row;
    gap: 1em;
    justify-content: center;
    align-items: center;
    background-color: hsl(0, 0%, 95%);
    position: fixed;
    bottom: 0;
    width: fit-content;
    padding: .5em 1em;
    border-radius: 0.5em 0.5em 0 0;
    left: 50%;
    transform: translate(-50%, 0);
    z-index: 100000;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
  }

  a {
    all: unset;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    font-size: .9rem;
  }
</style>

<nav>
  <a href="/">
    <House size={20}/>
    Home
  </a>
  <a href="/results">
    <SearchIcon size={20}/>
    Search
  </a>
  <a href="/plan">
    <NotebookPen size={20}/>
    My Plan
  </a>
</nav>