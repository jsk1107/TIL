import { useEffect, useState } from "react"
import styled from "styled-components"



const Container = styled.div``;

const Header = styled.header`
    background-color: black;
`;

const CoinList = styled.ul``;
const Coin = styled.li``;

const Title = styled.h1`
    color: darkblue;
    text-align: center;
    padding: 20px;
    background-color: blueviolet;
`;



interface Icoin {
    id: string,
    name: string,
    symbol: string
    is_active: boolean,
    is_new: boolean,
    rank: number,
    type: string
}

function Coins() {
    const [coins, setCoins] = useState<Icoin[]>([]);
    useEffect(() => {
        const getCoins = async () => {
            const response = await fetch('https://api.coinpaprika.com/v1/coins');
            const json = await response.json();
            setCoins(json);
        }
        getCoins();
    }, []);
    console.log(coins)
    return (
        <Container>
            <Header>
                <Title> Coin !! </Title>
            </Header>
            <CoinList>
                {coins.map((coin) => <Coin key={coin.id}>{coin.id}</Coin>)}
            </CoinList>
        </Container>
    );
}

export default Coins