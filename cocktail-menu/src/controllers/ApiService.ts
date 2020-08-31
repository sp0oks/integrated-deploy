import axios from "axios";
import { Drink } from "@/models/Drink";

axios.defaults.baseURL = process.env.BACKEND_URL == undefined ? "http://localhost:3000" : process.env.BACKEND_URL;

export default class ApiService {
    async getDrink(): Promise<Drink> {
        const response = await axios.get("/cocktail");
        return response.data;
    }
}
