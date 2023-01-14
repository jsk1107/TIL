import styled from "styled-components"
import { useLocation, useParams } from "react-router-dom";
import { useEffect, useState } from "react";


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
}

function Coin() {
    const { coinId } = useParams<ICoinId>();
    const { state } = useLocation<IState>();
    const [info, setInfo] = useState<IInfo>();
    const [priceinfo, setPriceInfo] = useState<IPrice>();
    useEffect(() => {
        (async () => {
            const infoData = await (await fetch(`https://api.coinpaprika.com/v1/coins/${coinId}`)).json();
            const priceData = await (await fetch(`https://api.coinpaprika.com/v1/ticker/${coinId}`)).json();
            setInfo(infoData);
            setPriceInfo(priceData);
        })();
        console.log(priceinfo);
    }, [])
    return (
        <h1>Coin: {state?.name || "Hi"} {info?.id} {priceinfo?.id}</h1>

    );
}

export default Coin

