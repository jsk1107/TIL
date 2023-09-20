import { useEffect, useState } from "react";
import { useLocation, useParams } from "react-router-dom";
import styled from "styled-components";

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

function Coin() {
  // url의 queryString을 가지고온다.
  // key는 Route에서 :coinId 이런식으로 쓰면 coinId가 key가 된다. value는 사용자가 입력한 값
  const { coinId } = useParams<ICoin>();
  const [loading, setLoading] = useState<boolean>(true);
  const { state } = useLocation<IRouteState>();
  const [info, setInfo] = useState({});
  const [priceinfo, setPriceInfo] = useState({});

  useEffect(() => {
    (async () => {
      console.log(1);
      const infoData = await (
        await fetch(`https://api.coinpaprika.com/v1/coins/${state?.name}`)
      ).json();
      console.log(2);
    })();
    (async () => {
      console.log(5);
      const priceData = await (
        await fetch(`https://api.coinpaprika.com/v1/tickers/${state?.name}`)
      ).json();
      console.log(6);
    })();
  }, []);
  return (
    <Container>
      <Header>
        <Title> {state?.name || "Loading..."} </Title>
      </Header>
      {loading ? <Loading>Loading</Loading> : null}
    </Container>
  );
}

export default Coin;
