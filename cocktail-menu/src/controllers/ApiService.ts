import axios from "axios";
import { Drink } from "@/models/Drink";

// axios.defaults.baseURL = "http://backend:8000"

export default class ApiService {
    async getDrink(): Promise<Drink> {
        const response = await axios.get("/api/cocktail");
        return response.data;
    }
}
