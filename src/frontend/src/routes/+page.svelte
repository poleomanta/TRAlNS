<script lang="ts">
    import { leisureTags, tourismTags } from "$lib/tags";
  import Row from "../components/Row.svelte";
  import Search from "../components/Search.svelte";
  import Subtitle from "../components/Subtitle.svelte";
  import Tag from "../components/Tag.svelte";

  const tags = leisureTags.concat(tourismTags);
  tags.sort();
</script>

<img src="/img/munich.jpg" alt="Munich skyline" />
<!--<Title>
  TRAlNS
</Title>-->
<Subtitle>Munich sightseeing made simple</Subtitle>
<Search />
<Row>
  {#each tags as name}
    <Tag {name} />
  {/each}
</Row>
