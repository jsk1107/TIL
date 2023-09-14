import { Link } from "react-router-dom";
import styled from "styled-components";

const Container = styled.div`
    padding: 20px;
`;

const Header = styled.header`
    font-size: 3rem;
`;

const CoinsList = styled.ul`
    width: 50%;
    height: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
`;

const Coin = styled.li`
    background: white;
    color: ${props => props.theme.bgColor};
    margin: 10px 0;
    border-radius: 5px;

    a {
        display: block;
        padding: 20px;
        transition: color 0.2s ease-in;
    }

`;

const Title = styled.div`
    color: ${props => props.theme.accentColor};
`

const coin = [
    { "id": "btc-bitcoin", "name": "Bitcoin", "symbol": "BTC", "rank": 1, "circulating_supply": 19485131, "total_supply": 19485144, "max_supply": 21000000, "beta_value": 0.896626, "first_data_at": "2010-07-17T00:00:00Z", "last_updated": "2023-09-14T12:41:18Z", "quotes": { "USD": { "price": 26426.246037855784, "volume_24h": 10415754216.13755, "volume_24h_change_24h": -10.18, "market_cap": 514918865886, "market_cap_change_24h": 0.91, "percent_change_15m": 0.06, "percent_change_30m": -0.29, "percent_change_1h": 0.05, "percent_change_6h": 0.56, "percent_change_12h": 0.03, "percent_change_24h": 0.91, "percent_change_7d": 2.9, "percent_change_30d": -9.22, "percent_change_1y": 31.13, "ath_price": 68692.13703693185, "ath_date": "2021-11-10T16:50:00Z", "percent_from_price_ath": -61.54 } } }, { "id": "eth-ethereum", "name": "Ethereum", "symbol": "ETH", "rank": 2, "circulating_supply": 120222579, "total_supply": 120222579, "max_supply": 0, "beta_value": 1.0168, "first_data_at": "2015-08-07T00:00:00Z", "last_updated": "2023-09-14T12:41:18Z", "quotes": { "USD": { "price": 1622.1200133099294, "volume_24h": 4074964242.920333, "volume_24h_change_24h": -2.29, "market_cap": 195015451448, "market_cap_change_24h": 1.45, "percent_change_15m": 0.06, "percent_change_30m": -0.3, "percent_change_1h": -0.21, "percent_change_6h": 0.16, "percent_change_12h": -0.53, "percent_change_24h": 1.45, "percent_change_7d": -0.42, "percent_change_30d": -10.85, "percent_change_1y": 2.08, "ath_price": 4864.113196614236, "ath_date": "2021-11-10T16:05:00Z", "percent_from_price_ath": -66.66 } } }, { "id": "usdt-tether", "name": "Tether", "symbol": "USDT", "rank": 3, "circulating_supply": 83034723503, "total_supply": 86333199612, "max_supply": 0, "beta_value": -0.00146109, "first_data_at": "2015-02-25T00:00:00Z", "last_updated": "2023-09-14T12:41:19Z", "quotes": { "USD": { "price": 1.0002988128650803, "volume_24h": 15866765698.7598, "volume_24h_change_24h": -11.17, "market_cap": 83059535347, "market_cap_change_24h": 0.01, "percent_change_15m": -0.02, "percent_change_30m": 0.02, "percent_change_1h": 0.01, "percent_change_6h": 0.03, "percent_change_12h": -0, "percent_change_24h": 0.01, "percent_change_7d": 0.06, "percent_change_30d": 0.11, "percent_change_1y": -0.05, "ath_price": 1.21549, "ath_date": "2015-02-25T17:04:00Z", "percent_from_price_ath": -17.69 } } }
]
function Coins() {
    return <Container>
        <Header>
            <Title> 코인 </Title>
        </Header>
        <CoinsList>
            {coin.map(data =>
                <Coin key={data.id}>
                    <Link to={data.symbol}> {data.name} </Link>
                </Coin>)}
        </CoinsList>
    </Container>
}

export default Coins;