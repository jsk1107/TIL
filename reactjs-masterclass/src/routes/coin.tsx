import styled from "styled-components"
import { useLocation, useParams } from "react-router-dom";
import { useEffect, useState } from "react";


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

const PriceInfo = styled.div`
    display: flex;
    justify-content: space-between;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 10px 20px;
    border-radius: 10px;
`;

const Price = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;

   span:first-child {
     font-size: 10px;
     font-weight: 400;
     text-transform: uppercase;
     margin-bottom: 5px;
   }
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
            console.log(infoData);
            console.log(priceData);
        })();
    }, [])
    const time = new Date();
    return (
        <Conatainer>
            <Header>
                <Title>
                    {state?.name || "Loading ..."}
                </Title>
            </Header>
            <PriceInfo>
                <Price>
                    <span>Coin Name</span>
                    <span>{priceinfo?.name}</span>
                </Price>
                <Price>
                    <span>USD Price</span>
                    <span>${Math.round(Number(priceinfo?.price_usd))}</span>
                </Price>
                <Price>
                    <span>Update Time </span>
                    <span>
                        {time.getFullYear()} / {time.getMonth() + 1} / {time.getDate()}::
                        {time.getHours()}h:{time.getMinutes()}m
                    </span>
                </Price>
            </PriceInfo>
            <Description>
                {info?.description}
            </Description>

            <PriceInfo>
                <Price>
                    <span>Total Suply</span>
                    <span>{priceinfo?.total_supply}</span>
                </Price>
                <Price>
                    <span>rank</span>
                    <span>{priceinfo?.rank}</span>
                </Price>
            </PriceInfo>

        </Conatainer>

    );
}

export default Coin

