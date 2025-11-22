export function fetchDestinations(query: string): Promise<any> {
  return fetch(`/api/destinations?search=${encodeURIComponent(query)}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Error fetching destinations: ${response.statusText}`);
      }
      return response.json();
    });
}