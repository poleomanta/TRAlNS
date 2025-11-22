export class DestinationModel {
    name?: string;
    tag: string;
    description?: string;
    website?: string;
    lat: number;
    lon: number;

    constructor(name: string | undefined | null, tag: string, description: string | undefined | null, website: string | undefined | null, lat: number, lon: number) {
        this.name = name !== null ? name : undefined;
        this.tag = tag;
        this.description = description !== null ? description : undefined;
        this.website = website !== null ? website : undefined;
        this.lat = lat;
        this.lon = lon;
    }
}

export class CoordinatesModel {
    lat: number
    lon: number

    constructor(lat: number, lon: number) {
        this.lat = lat;
        this.lon = lon;
    }
}

export class AmenityModel {
    kind: string;
    locations: CoordinatesModel[];
    status: string;

    constructor(kind: string, locations: CoordinatesModel[], status: string) {
        this.kind = kind;
        this.locations = locations;
        this.status = status;
    }
}