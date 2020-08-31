export class Drink {
    constructor(name: string, img: string, id: number, instructions: string, ingredients: Array<string>) {
        this.name = name;
        this.img = img;
        this.id = id;
        this.instructions = instructions;
        this.ingredients = ingredients;
    }

    name: string;
    img: string;
    id: number;
    instructions: string;
    ingredients: Array<string>;
}
