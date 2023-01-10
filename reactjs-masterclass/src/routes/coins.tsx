import { useEffect, useState } from "react"
import { Link } from "react-router-dom";
import styled from "styled-components"

const Header = styled.header`
    height: 10vh;
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
`;

const CoinsList = styled.ul`

`;

const Coin = styled.li`
    background-color: white;
    color: ${props => props.theme.bgColor};
    margin-bottom: 10px;
    border-radius: 15px;
    padding: 20px;
    a {
        /* padding: 20px; */
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
    const [coins, setCoins] = useState<ICoin[]>([]);
    const [loading, setLoading] = useState(true);
    const [logos, setLogos] = useState();
    useEffect(() => {
        // const getCoins = async () => {
        //     const response = await fetch('https://api.coinpaprika.com/v1/coins');
        //     const json = await response.json();
        //     setCoins(json.slice(0, 100));
        // }
        // getCoins();
        (async () => {
            const response = await fetch('https://api.coinpaprika.com/v1/coins');
            const json = await response.json();
            setCoins(json.slice(0, 100));
            setLoading(false);
        })();
    }, []);

    return (
        <Container>
            <Header>
                <Title>Coins!!</Title>
            </Header>
            {loading ? (<Loading>"Loading..."</Loading>) : (<CoinsList>
                {coins.map((coin) => (
                    <Coin key={coin.id}>
                        <Link to={`/${coin.id}`}>
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
