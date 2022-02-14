export interface Person {
    name: string;
    height: Number;
    mass: Number;
    birth_date: Date;
    created_at: Date;
    updated_at: Date;
    hair_color: string;
    skin_color: string;
    eye_color: string;
    gender: string;
    homeworld: string;
    specie: string;
    vehicles: string[];
    films: string[];
    url: string;
}

export interface People {
    count: number;
    next?: string;
    prev?: string;
    results: Person[];
}
