import { BrowserRouter, Route, Switch } from "react-router-dom";
import Coins from './routes/coins';
import Coin from './routes/coin';

function Router() {
    return (<BrowserRouter>
        <Switch>
            <Route path="/">
                <Coins />
            </Route>
            <Route path='/:coinId'>
                <Coin />
            </Route>
        </Switch>
    </BrowserRouter>);
}

export default Router;