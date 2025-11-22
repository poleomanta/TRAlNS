import type { PageLoad } from "./$types";
import { unusedTags } from "$lib/tags";


export const load: PageLoad = async ({ url, params, fetch }) => {
  const endpoint = `/api/destinations${(url.searchParams.get("search") || "").length > 0 ? `?query=${encodeURIComponent(url.searchParams.get("search") || "")}` : ""}`;
  let allDestinations = await fetch(endpoint).then(res => res.json());

  const tagParam = url.searchParams.get("tag");
  if (tagParam && tagParam.length > 0) {
    allDestinations = allDestinations.filter((dest: any) => dest.tag === tagParam && !unusedTags.includes(tagParam));
  }

  const textParam = decodeURIComponent(url.searchParams.get("search") || "");
  if (textParam && textParam.length > 0) {
    const lowerTextParam = textParam.toLowerCase();
    allDestinations = allDestinations.filter((dest: any) =>
      dest.name.toLowerCase().includes(lowerTextParam) ||
      (dest.description || "").toLowerCase().includes(lowerTextParam) ||
      dest.tag.toLowerCase().includes(lowerTextParam)
    );
  }

  // remove duplicates:
  const uniqueDestinationsMap = new Map();
  for (const dest of allDestinations) {
    const id = JSON.stringify(dest);
    if (!uniqueDestinationsMap.has(id)) {
      uniqueDestinationsMap.set(id, dest);
    }
  }

  const sortedDestinations = Array.from(uniqueDestinationsMap.values()).sort((a, b) => {
    return a.name.localeCompare(b.name);
  });

  return {
    destinations: sortedDestinations
  }
}