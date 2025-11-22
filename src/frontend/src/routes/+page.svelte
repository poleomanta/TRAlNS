<script>
  import Row from "../components/Row.svelte";
  import Search from "../components/Search.svelte";
  import Subtitle from "../components/Subtitle.svelte";
  import Tag from "../components/Tag.svelte";
</script>

<img src="/img/munich.jpg" alt="Munich skyline" />
<!--<Title>
  TRAlNS
</Title>-->
<Subtitle>Munich sightseeing made simple</Subtitle>
<Search />
<Row>
  {#each ["hi", "halo"] as name}
    <Tag {name} />
  {/each}
</Row>
