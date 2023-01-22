import { useEffect, useState } from "react"
import { useQuery } from "react-query";
import { Link } from "react-router-dom";
import styled from "styled-components"
import { fetchCoins } from "../api";
import { Helmet } from "react-helmet";
import { useSetRecoilState } from "recoil";
import { isDarkAtom } from "../atoms";

const Header = styled.header`

    height: 15vh;
    display: flex;
    justify-content: center;
    align-items: center;
`;
const Title = styled.h1`
    font-size: 48px;
    color: ${props => props.theme.accentColor};
`;

const Container = styled.div`
    padding: 0px 20px;
    max-width: 480px;
    margin: 0 auto;
`;

const CoinsList = styled.ul`
`;

const Coin = styled.li`
    background-color: ${props => props.theme.libgColor};
    color: ${props => props.theme.textColor};
    margin-bottom: 10px;
    border-radius: 15px;
    border: 1px solid white;
    border-color: ${(props) => props.theme.borderColor};
    /* padding: 20px; */
    a {
        padding: 20px;
        transition: color 0.2s ease-in;
        display: flex;
        align-items: center;
        /* text-align: center */
    }
    &:hover {
        a {
            color: ${(props) => props.theme.accentColor};
        }
    }
`;

const Loading = styled.span`
    text-align: center;
    display: block;
`;

const Img = styled.img`
    width: 25px;
    height: 25px;
    margin-right: 10px;
`;

interface ICoin {
    id: string,
    is_active: boolean,
    is_new: boolean,
    name: string,
    rank: number,
    symbol: string,
    type: string
}

function Coins() {
    // const [coins, setCoins] = useState<ICoin[]>([]);
    // const [loading, setLoading] = useState(true);
    // useEffect(() => {
    //     // const getCoins = async () => {
    //     //     const response = await fetch('https://api.coinpaprika.com/v1/coins');
    //     //     const json = await response.json();
    //     //     setCoins(json.slice(0, 100));
    //     // }
    //     // getCoins();
    //     (async () => {
    //         const response = await fetch('https://api.coinpaprika.com/v1/coins');
    //         const json = await response.json();
    //         setCoins(json.slice(0, 100));
    //         setLoading(false);
    //     })();
    // }, []);

    const { isLoading, data } = useQuery<ICoin[]>("allCoins", fetchCoins)
    const setDarkAtom = useSetRecoilState(isDarkAtom);
    const toggleDarkAtom = () => setDarkAtom((prev) => !prev);

    return (
        <Container>
            <Helmet>
                <title> Coins!! </title>
            </Helmet>
            <Header>
                <Title>Coins!!</Title>
                <button onClick={toggleDarkAtom}> Toggle button </button>
            </Header>
            {isLoading ? (<Loading>"Loading..."</Loading>) : (<CoinsList>
                {data?.map((coin) => (
                    <Coin key={coin.id}>
                        <Link to={{
                            pathname: `/${coin.id}`,
                            state: { name: coin.name }
                        }}>
                            <Img src={`https://coinicons-api.vercel.app/api/icon/${coin.symbol.toLocaleLowerCase()}`}></Img>
                            {coin.name} &rarr;
                        </Link>
                    </Coin>
                ))}
            </CoinsList>)}
        </Container >
    );
}

export default Coins

// Coin URI: https://api.coinpaprika.com/v1/coins 
