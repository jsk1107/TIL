import { useEffect, useState } from "react";
import {
  Link,
  Route,
  Switch,
  useLocation,
  useParams,
  useRouteMatch,
} from "react-router-dom";
import styled from "styled-components";
import Chart from "./Chart";
import Price from "./Price";
import { useQuery } from "react-query";
import { fetchCoinInfo, fetchCoinTickers } from "../api/fetchCoin";
import { Helmet } from "react-helmet";
import Coins from "./Coins";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHouse } from "@fortawesome/free-solid-svg-icons";

interface ICoin {
  coinId: string;
}

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

const Loading = styled.div`
  text-align: center;
`;

const Title = styled.div`
  color: ${(props) => props.theme.accentColor};
  font-size: 48px;
`;

interface IRouteState {
  name: string;
}

interface ITag {
  coin_counter: number;
  ico_counter: number;
  id: string;
  name: string;
}

interface IInfoData {
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

interface IPriceData {
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
  quotes: {
    USD: {
      ath_date: string;
      ath_price: number;
      market_cap: number;
      market_cap_change_24h: number;
      percent_change_1h: number;
      percent_change_1y: number;
      percent_change_6h: number;
      percent_change_7d: number;
      percent_change_12h: number;
      percent_change_15m: number;
      percent_change_24h: number;
      percent_change_30d: number;
      percent_change_30m: number;
      percent_from_price_ath: number;
      price: number;
      volume_24h: number;
      volume_24h_change_24h: number;
    };
  };
}

const Overview = styled.div`
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
  padding: 10px;
  background: rgba(0, 0, 0, 0.5);
`;

const OverviewContent = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 0.9rem;
  font-weight: bold;
  padding: 10px;
  color: ${(prop) => prop.theme.textColor};

  span:first-child {
    margin-bottom: 5px;
    text-align: center;
    text-transform: uppercase;
    vertical-align: middle;
    font-size: 0.75rem;
  }
`;

const Description = styled.div`
  font-size: 1.1rem;
  font-weight: 400;
  margin: 10px 0;
`;

const Tabs = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 20px 0;
`;

const Tab = styled.div<{ isActive: boolean }>`
  background: ${(props) => props.theme.bgColor};
  color: ${(props) =>
    props.isActive ? props.theme.accentColor : props.theme.textColor};
  background: rgba(0, 0, 0, 0.5);
  border-radius: 10px;
  text-transform: uppercase;
  font-size: 0.9rem;
  font-weight: bold;
  width: 49%;
  text-align: center;
  a {
    padding: 10px 20px;
    display: block;
  }
`;

function Coin() {
  // url의 queryString을 가지고온다.
  // key는 Route에서 :coinId 이런식으로 쓰면 coinId가 key가 된다. value는 사용자가 입력한 값
  const { coinId } = useParams<ICoin>();
  const { state } = useLocation<IRouteState>();
  // useRouteMatch는 현재 링크와 인자로 받은 링크가 동일한지 여부를 확인한다.
  const usePriceMatch = useRouteMatch(`/${coinId}/price`);
  const useChartMatch = useRouteMatch(`/${coinId}/chart`);
  const { isLoading: infoLoading, data: infoData } = useQuery(
    ["info", coinId],
    () => fetchCoinInfo(coinId) // 함수에 인자를 받아야하기 때문에 익명함수를 사용하여 한번 더 패킹해줘야한다.
  );
  const { isLoading: tickersLoading, data: tickersData } = useQuery(
    ["tickers", coinId],
    () => fetchCoinTickers(coinId)
  );

  /* const [loading, setLoading] = useState<boolean>(true);
  const [info, setInfo] = useState<IInfoData>();
  const [priceInfo, setPriceInfo] = useState<IPriceData>();
  useEffect(() => {
    (async () => {
      // coinId로 인자를 주어야한다. useParams은 URL 값을 바로 가지고 오기 때문이다.
      // useLocation을 통해 받은 state를 사용할 경우, Coins.tsx를 통해서 오지 않는이상 값이 들어가 있지 않다.
      // URL로 링크를 타고 바로 들어왔기 때문에 Link 컴포넌트에서 객체를 받을 수 없기 때문이다.
      const infoData = await (
        await fetch(`https://api.coinpaprika.com/v1/coins/${coinId}`)
      ).json();
      setInfo(infoData);
    })();
    (async () => {
      const priceData = await (
        await fetch(`https://api.coinpaprika.com/v1/tickers/${coinId}`)
      ).json();
      setPriceInfo(priceData);
      setLoading(false);
    })();
  }, [coinId]); // coinId가 변하면 re-rendering됨. 하지만 변하지않기때문에(불변) 영원히 바뀌지 않는다. */

  // info fetch와 ticker fetch 둘다 작업이 종료되야만 화면이 렌더링 됨
  // || 연산자는 둘다 false일때 false. 하나라도 true면 true를 반환함
  const loading = infoLoading || tickersLoading;
  return (
    <Container>
      <Helmet>
        <title>{coinId}</title>
      </Helmet>
      <Header>
        <Link to={{ pathname: "/" }}>
          <FontAwesomeIcon icon={faHouse} />
        </Link>
        <Title>
          {state?.name ? state.name : loading ? "Loading" : infoData?.name}
        </Title>
      </Header>
      {loading ? (
        <Loading>Loading</Loading>
      ) : (
        <>
          <Overview>
            <OverviewContent>
              <span>rank:</span>
              <span>{infoData?.rank}</span>
            </OverviewContent>
            <OverviewContent>
              <span>symbol:</span>
              <span>${infoData?.symbol}</span>
            </OverviewContent>
            <OverviewContent>
              <span>open source:</span>
              <span>{infoData?.open_source ? "Yes" : "No"}</span>
            </OverviewContent>
          </Overview>

          <Description>{infoData?.description}</Description>

          <Overview>
            <OverviewContent>
              <span> total supply:</span>
              <span> {tickersData?.quotes.USD.price}</span>
            </OverviewContent>
            <OverviewContent>
              <span> max supply:</span>
              <span> {tickersData?.max_supply} </span>
            </OverviewContent>
          </Overview>
        </>
      )}

      <Tabs>
        <Tab isActive={useChartMatch !== null}>
          <Link to={{ pathname: `/${coinId}/Chart` }}>Chart</Link>
        </Tab>
        <Tab isActive={usePriceMatch !== null}>
          <Link to={{ pathname: `/${coinId}/price` }}>Price</Link>
        </Tab>
      </Tabs>

      <Switch>
        <Route path="/:coinId/Chart">
          <Chart coinId={coinId} />
        </Route>
        <Route path=":/coinId/Price">
          <Price />
        </Route>
      </Switch>
    </Container>
  );
}

export default Coin;
