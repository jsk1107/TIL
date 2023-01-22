import styled from "styled-components"
import { Link, Route, Switch, useLocation, useParams, useRouteMatch } from "react-router-dom";
import { useEffect, useState } from "react";
import Chart from "./Chart";
import Price from "./Price";
import { useQuery } from "react-query";
import { fetchCoinInfo, fetchCoinTickers } from "../api";
import { Helmet } from "react-helmet";

const Conatainer = styled.div`
    padding: 0px 20px;
    max-width: 480px;
    margin: 0 auto;
`;

const Header = styled.header`
    display: flex;
    justify-content: center;
    align-items: center;
`;

const Title = styled.h1`
    font-size: 48px;
    color: ${props => props.theme.accentColor};
`;

const Overview = styled.div`
    display: flex;
    justify-content: space-between;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 10px 20px;
    border-radius: 10px;
`;

const OverviewItem = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    color: ${(props) => props.theme.textColor};

   span:first-child {
     font-size: 10px;
     font-weight: 400;
     text-transform: uppercase;
     margin-bottom: 5px;
   }
`;

const Tabs = styled.div`
    display: grid;
    gap: 10px;
    margin: 25px 10px;
   grid-template-columns: repeat(2, 1fr);
`;

const Tab = styled.span< { isActive: boolean }> `
    text-align: center;
    text-transform: uppercase;
    font-size: 12px;
    font-weight: 400;
    padding: 7px 0px;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.5);
    color : ${(props) => props.isActive ? props.theme.accentColor : props.theme.textColor};
    a{
        display: block;
    }
`;

const Home = styled.div`
    display: flex;
    align-items: flex-end;
    
`;

const Loader = styled.span`
    text-align: center;
    display: block;
`;

const Description = styled.p`
    margin: 20px 0px;
`;

interface ICoinId {
    coinId: string
}

interface IState {
    name: string
}

interface ITag {
    coin_counter: number,
    ico_counter: number,
    id: string,
    name: string
}

interface IInfo {
    id: string;
    name: string;
    symbol: string;
    rank: number;
    is_new: boolean;
    is_active: boolean;
    type: string;
    logo: string;
    tags: ITag[];
    description: string;
    message: string;
    open_source: boolean;
    started_at: string;
    development_status: string;
    hardware_wallet: boolean;
    proof_type: string;
    org_structure: string;
    hash_algorithm: string;
    first_data_at: string;
    last_data_at: string;
}

interface IQutes {
    price: number;
    volume_24h: number;
    volume_24h_change_24h: number;
    market_cap: number;
    market_cap_change_24h: number;
    percent_change_15m: number;
    percent_change_30m: number;
    percent_change_1h: number;
    percent_change_6h: number;
    percent_change_12h: number;
    percent_change_24h: number;
    percent_change_7d: number;
    percent_change_30d: number;
    percent_change_1y: number;
    ath_price: number;
    ath_date: string
    percent_from_price_ath: number
}
interface IPrice {
    id: string;
    name: string;
    symbol: string;
    rank: string;
    price_usd: string;
    price_btc: string;
    volume_24h_usd: string;
    market_cap_usd: string;
    circulating_supply: string;
    total_supply: string;
    max_supply: string;
    percent_change_1h: string;
    percent_change_24h: string;
    percent_change_7d: string;
    last_updated: string;
    quotes: {
        USD:
        IQutes;

    }

}

function Coin() {
    const { coinId } = useParams<ICoinId>();
    const { state } = useLocation<IState>();
    const chartMatch = useRouteMatch("/:coinId/chart");
    const priceMatch = useRouteMatch("/:coinId/price");
    const { isLoading: infoLoading, data: infoData } = useQuery<IInfo>(['info', coinId], () => fetchCoinInfo(coinId), { refetchInterval: 5000, });
    const { isLoading: tickersLoading, data: tickersData } = useQuery<IPrice>(['tickers', coinId], () => fetchCoinTickers(coinId));
    // const [info, setInfo] = useState<IInfo>();
    // const [priceinfo, setPriceInfo] = useState<IPrice>();
    // const [loading, setLoading] = useState(true);
    // useEffect(() => {
    //     (async () => {
    //         const infoData = await (await fetch(`https://api.coinpaprika.com/v1/coins/${coinId}`)).json();
    //         const priceData = await (await fetch(`https://api.coinpaprika.com/v1/ticker/${coinId}`)).json();
    //         setInfo(infoData);
    //         setPriceInfo(priceData);
    //         setLoading(false);
    //     })();
    // }, [coinId]);
    const time = new Date();
    const loading = infoLoading || tickersLoading;
    return (
        <Conatainer>
            <Helmet>
                <title>
                    {state?.name ? state.name : loading ? "Loading..." : infoData?.name}
                </title>
            </Helmet>
            <Header>
                <Title>
                    {state?.name ? state.name : loading ? "Loading..." : infoData?.name}
                </Title>
                <Home>
                    <Link to={`/`}>
                        🏠
                    </Link>
                </Home>
            </Header>
            {loading ? (
                <Loader>Loading...</Loader>
            ) : (
                <>
                    <Overview>
                        <OverviewItem>
                            <span>Coin Name</span>
                            <span>{tickersData?.name}</span>
                        </OverviewItem>
                        <OverviewItem>
                            <span>USD Price</span>
                            <span>${Math.round(Number(tickersData?.quotes.USD.price))}</span>
                        </OverviewItem>
                        <OverviewItem>
                            <span>Update Time </span>
                            <span>
                                {time.getFullYear()} / {time.getMonth() + 1} / {time.getDate()}::
                                {time.getHours()}h:{time.getMinutes()}m
                            </span>
                        </OverviewItem>
                    </Overview>
                    <Description>
                        {infoData?.description}
                    </Description>

                    <Overview>
                        <OverviewItem>
                            <span>Total Suply</span>
                            <span>{tickersData?.total_supply}</span>
                        </OverviewItem>
                        <OverviewItem>
                            <span>rank</span>
                            <span>{tickersData?.rank}</span>
                        </OverviewItem>
                    </Overview>

                    <Tabs>
                        <Tab isActive={chartMatch !== null}>
                            <Link to={`/${coinId}/chart`}> Chart</Link>
                        </Tab>
                        <Tab isActive={priceMatch !== null}>
                            <Link to={`/${coinId}/price`}> Price </Link>
                        </Tab>
                    </Tabs>

                    <Switch>
                        <Route path={`/:coinId/price`}>
                            <Price coinId={coinId} />
                        </Route>
                        <Route path={`/:coinId/chart`}>
                            <Chart coinId={coinId} />
                        </Route>
                    </Switch>
                </>)}
        </Conatainer>

    );
}

export default Coin

