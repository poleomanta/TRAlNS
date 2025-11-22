import type { PageLoad } from "./$types";

export const load: PageLoad = async ({ params, fetch }) => {
  return {
    destinations: await fetch("/api/destinations").then(res => res.json())
  }
}