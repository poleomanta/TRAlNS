<script>
    import { DestinationModel } from "$lib/classes";
    import Column from "../../components/Column.svelte";
    import Destination from "../../components/Destination.svelte";
    import Subtitle from "../../components/Subtitle.svelte";

    const destinations = [
        new DestinationModel(
            "Steg an der Marienklause",
            "viewpoint",
            null,
            null,
            48.092589,
            11.5502469,
        ),
        new DestinationModel(
            "Torbogen",
            "artwork",
            "ehemaliger Eingang IGA 1986",
            null,
            48.1271504,
            11.5384511,
        ),
        new DestinationModel(
            "elaya hotel munich schwabing",
            "hotel",
            null,
            null,
            48.1833728,
            11.5939383,
        ),
        new DestinationModel(
            "Bavaria",
            "viewpoint",
            null,
            "https://www.schloesser.bayern.de/deutsch/schloss/objekte/mu_ruhm.htm",
            48.1306873,
            11.5459393,
        ),
        new DestinationModel(
            "Spielzeugmuseum",
            "museum",
            null,
            "https://www.spielzeugmuseummuenchen.de/",
            48.1366906,
            11.5768793,
        ),
        new DestinationModel(
            "Mercure Hotel München Neuperlach Süd",
            "hotel",
            null,
            "https://all.accor.com/hotel/0792/index.de.shtml",
            48.0920788,
            11.6442332,
        ),
        new DestinationModel(
            "Römischer Brunnen",
            "attraction",
            null,
            null,
            48.1506744,
            11.5809644,
        ),
        new DestinationModel(
            "Römischer Brunnen",
            "attraction",
            null,
            null,
            48.1505312,
            11.581668,
        ),
        new DestinationModel(
            "Museum Mineralogia München",
            "museum",
            "Besuchereingang: Marianne-von-Werefkin-Weg",
            null,
            48.1481129,
            11.572363,
        ),
        new DestinationModel(
            "Suite Novotel",
            "hotel",
            null,
            "https://all.accor.com/hotel/5229/index.de.shtml",
            48.1798572,
            11.593399,
        ),
        new DestinationModel(
            "Ibis München Parkstadt Schwabing",
            "hotel",
            null,
            "https://all.accor.com/hotel/5239/index.de.shtml",
            48.1796533,
            11.5931791,
        ),
        new DestinationModel(
            "Novotel München City",
            "hotel",
            null,
            "https://all.accor.com/hotel/3280/index.de.shtml",
            48.1293774,
            11.589306,
        ),
    ];
</script>

<Subtitle>Things you might like</Subtitle>
<Column>
    {#each destinations as d}
        <Destination destination={d} />
    {/each}
</Column>
