import type { PageLoad } from "./$types";

export const load: PageLoad = async ({ url, params, fetch }) => {
  let allDestinations = await fetch("/api/destinations").then(res => res.json());

  const tagParam = url.searchParams.get("tag");
  if (tagParam && tagParam.length > 0) {
    allDestinations = allDestinations.filter((dest: any) => dest.tag === tagParam);
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