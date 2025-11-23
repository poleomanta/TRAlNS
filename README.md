# TRAlNS - Hackatum 2025

Sometimes it's really hard to find stuff to do in the city if you don't want to spend money. Sometimes we just want to chill and exist in our beautiful city without consuming. 

The Really Affordable leisure Navigation Service (TRAlNS) will make this easier! In this platform, users can discover destinations and plan outings. We want to help answer questions like:

- Where can my D-ticket take me for a day trip?
- What free amenities are around this cool spot? (benches, drinking water, toilets, parks)
- What activities can I do with x money in y time?
- What cool and free events are in my area?
- What's going on around my area: demos, citizen exchanges, calls for volunteering, etc?

## Implementation

### Frontend
We use Svelte+TS

### Backend
Python with common OSM libraries (OSMPythonTools, OSMnx) and OpenRouteService.

## Installation

### Prerequisites

- Python >= 3.8
- make
- nvm
- bun
- An OpenRouteService API key

### Usage

After cloning and cd-ing the repo, create a `.env` file with your OpenRouteService API key in the `src/backend` directory (there's an example file),

To run the backend:

```bash
cd src/backend
make setup
make
```

Will begin serving the API endpoints

To run the frontend

```bash
cd src/frontend
make setup
make
```
Will begin serving the frontend.

Enjoy!
