import { BrowserRouter, Route, Switch } from "react-router-dom";
import Coins from "./components/Coins";
import Coin from "./components/Coin";

export default function Router() {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/:coinId">
                    <Coin></Coin>
                </Route>
                <Route path="/">

                    <Coins />
                </Route>



            </Switch>
        </BrowserRouter>
    )
}