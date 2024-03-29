import { useEffect, useState } from "react";
import { useQuery } from "react-query";
import { Link } from "react-router-dom";
import styled from "styled-components";
import { fetchCoin } from "../api/fetchCoin";
import { useResetRecoilState, useSetRecoilState } from "recoil";
import { isDarkAtom } from "../atom";

const Container = styled.div`
  padding: 20px;
  max-width: 480px;
  margin: 0 auto;
`;

const Header = styled.header`
  font-size: 3rem;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const CoinsList = styled.ul``;

const Coin = styled.li`
  background: white;
  color: ${(props) => props.theme.textColor};
  margin: 10px 0;
  border-radius: 15px;

  a {
    display: flex;
    align-items: center;
    padding: 20px;
    transition: color 0.2s ease-in;
  }
  &:hover {
    a {
      color: ${(props) => props.theme.accentColor};
    }
  }
`;

const Loading = styled.div`
  text-align: center;
`;

const Title = styled.div`
  color: ${(props) => props.theme.accentColor};
  font-size: 48px;
`;

const Img = styled.img`
  width: 35px;
  height: 35px;
  margin-right: 10px;
`;

interface IUsd {
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
  ath_date: string;
  percent_from_price_ath: number;
}

interface IQuotes {
  USD: IUsd;
}
interface ICoin {
  id: string;
  name: string;
  symbol: string;
  rank: number;
  circulating_supply: number;
  total_supply: number;
  max_supply: number;
  beta_value: number;
  first_data_at: string;
  last_updated: string;
  quotes: IQuotes;
}

function Coins() {
  const { isLoading, data } = useQuery<ICoin[]>("allCoins", fetchCoin);
  const setIsDarkAtom = useSetRecoilState(isDarkAtom);
  const toggleDartAtom = () => setIsDarkAtom((prev) => !prev);
  // const [coins, setCoins] = useState<ICoin[]>([]); // List 내부에 ICoin 타입의 객체가 들어있다는 뜻
  // const [loading, setLoading] = useState<boolean>(true);
  // useEffect(() => {
  //   (async () => {
  //     const response = await fetch("https://api.coinpaprika.com/v1/tickers");
  //     const json = await response.json();
  //     setCoins(json);
  //     setLoading(false);
  //   })();
  // }, []);
  return (
    <Container>
      <Header>
        <button onClick={toggleDartAtom}>theme toggle</button>
        <Title> 코인 </Title>
      </Header>
      {isLoading ? (
        <Loading>Loading</Loading>
      ) : (
        <CoinsList>
          {data?.map((coin) => (
            <Coin key={coin.id}>
              <Link
                to={{
                  pathname: `/${coin.id}`,
                  state: {
                    name: coin.id,
                  },
                }}
              >
                <Img
                  src={`https://coinicons-api.vercel.app/api/icon/${coin.symbol.toLowerCase()}`}
                />
                {coin.name} &rarr;
              </Link>
            </Coin>
          ))}
        </CoinsList>
      )}
    </Container>
  );
}

export default Coins;
